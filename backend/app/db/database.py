from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_url = settings.DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://")
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

print("DB URL:", settings.DATABASE_URL)