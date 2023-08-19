from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.src.core.config import settings

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if settings.API_ENV == 'development':
    # TEST SQLITE
    logger.info(f"ENV: {settings.API_ENV} sqlite")
    SQLALCHEMY_DATABASE_URI = "sqlite:///../app.sqlite"
    engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if settings.API_ENV == 'production':
    # PRODUCTION
    logger.info(f"ENV: {settings.API_ENV} postgresql")
    # SQLALCHEMY_DATABASE_URI = "postgresql://user:password@postgresserver/db"
    
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base = declarative_base() # Not necessary
