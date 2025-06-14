"""
Database configuration and setup for the AI Personal Assistant.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.core.config import settings

# Create the database engine
if settings.database_url.startswith("sqlite"):
    # SQLite specific configuration
    engine = create_engine(
        settings.get_database_url(),
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=settings.debug  # Log SQL queries in debug mode
    )
else:
    # PostgreSQL or other database configuration
    engine = create_engine(
        settings.get_database_url(),
        echo=settings.debug
    )

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for our models
Base = declarative_base()


def get_db():
    """
    Dependency that provides a database session.
    This will be used with FastAPI's dependency injection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """Drop all database tables (use with caution!)."""
    Base.metadata.drop_all(bind=engine) 