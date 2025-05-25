from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from app.database import SessionLocal
from app.utils import geocode_address, calculate_distance
from app.models import QueryHistory
from app.limiter import limiter
import re

# ✅ Moved to the top to avoid NameError
router = APIRouter()

# ✅ Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Input validation schema
class DistanceRequest(BaseModel):
    source: str = Field(..., min_length=2, max_length=255)
    destination: str = Field(..., min_length=2, max_length=255)

# ✅ Basic sanitization
def sanitize_input(value: str) -> str:
    value = re.sub(r"[;'\"]", "", value)
    return value.strip()

# ✅ POST /distance endpoint with rate limiting
@router.post("/distance")
@limiter.limit("5/minute")
def get_distance(request: Request, data: DistanceRequest, db: Session = Depends(get_db)):
    try:
        source = sanitize_input(data.source)
        destination = sanitize_input(data.destination)

        lat1, lon1 = geocode_address(source)
        lat2, lon2 = geocode_address(destination)
        km, mi = calculate_distance(lat1, lon1, lat2, lon2)

        history = QueryHistory(
            source=source,
            destination=destination,
            kilometers=km,
            miles=mi
        )
        db.add(history)
        db.commit()
        db.refresh(history)

        return {"kilometers": km, "miles": mi}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ✅ GET /history endpoint
@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    queries = db.query(QueryHistory).order_by(QueryHistory.id.desc()).all()
    return [
        {
            "id": q.id,  # ✅ Include ID so frontend delete works
            "source": q.source,
            "destination": q.destination,
            "kilometers": q.kilometers,
            "miles": q.miles
        }
        for q in queries
    ]

# ✅ DELETE /history/{query_id} endpoint
@router.delete("/history/{query_id}")
def delete_query(query_id: int, db: Session = Depends(get_db)):
    query = db.query(QueryHistory).filter(QueryHistory.id == query_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")

    db.delete(query)
    db.commit()
    return {"message": "Query deleted successfully"}
