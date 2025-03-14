from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    copies_available = Column(Integer, default=1)

    # Relationship to Borrow
    borrows = relationship("lib.models.borrow.Borrow", back_populates="book")

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', copies_available={self.copies_available})>"
