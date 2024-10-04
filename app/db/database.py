from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

databaseEngine = create_engine(settings.DATABASE_URL, pool_size= 10, max_overflow= 30)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=databaseEngine)

Base = declarative_base()

def get_db():
    db = LocalSession()

    try:
        yield db
    finally:
        db.close()