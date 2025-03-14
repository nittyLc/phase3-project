from sqlalchemy import Column, Integer, String
from lib.models import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', isbn='{self.isbn}')>"
