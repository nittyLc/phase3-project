from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

# Base for models to inherit from
Base = declarative_base()

# Import models only once here
from lib.models.book import Book
from lib.models.member import Member
from lib.models.borrow import Borrow
