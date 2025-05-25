from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router
from app.database import Base, engine
from app.limiter import limiter

app = FastAPI(title="Delivery Distance API")

# 🔐 Rate limiting middleware
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# 🔐 CORS Middleware — allow your deployed frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://address-mapping.vercel.app",  # 🔁 Replace with your actual Vercel frontend URL
        "http://localhost:5173"  # still allow local dev
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📦 Create tables
Base.metadata.create_all(bind=engine)

# 🔁 Include routes
app.include_router(router)
