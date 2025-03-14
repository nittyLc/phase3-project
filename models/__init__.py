from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (adjust if needed)
DATABASE_URL = "sqlite:///library.db"

# Create engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Base class for models
Base = declarative_base()

# Import all models to ensure Alembic picks them up
from .book import Book
from .member import Member
from .borrow import Borrow

