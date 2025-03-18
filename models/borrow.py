from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from lib.models import Base
from datetime import datetime

class Borrow(Base):
    __tablename__ = 'borrows'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)

    # Relationships
    member = relationship("lib.models.member.Member", back_populates="borrows")
    book = relationship("lib.models.book.Book", back_populates="borrows")

    def __repr__(self):
        return f"<Borrow(member_id={self.member_id}, book_id={self.book_id}, borrow_date={self.borrow_date}, return_date={self.return_date})>"
