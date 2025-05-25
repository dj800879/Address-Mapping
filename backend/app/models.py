from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class QueryHistory(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    miles = Column(Float, nullable=False)
    kilometers = Column(Float, nullable=False)
