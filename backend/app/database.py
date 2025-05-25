from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://address_mapping_user:IoZKb7nYZk6e0S8uheCzoMCksNnMy2Yi@dpg-d0paroemcj7s73duehig-a/address_mapping"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()