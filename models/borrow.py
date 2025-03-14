from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from lib.models import Base

class Borrow(Base):
    __tablename__ = 'borrows'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    borrow_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)

    # Relationships (optional but handy for queries)
    book = relationship("Book")
    member = relationship("Member")

    def __repr__(self):
        return (
            f"<Borrow(id={self.id}, book_id={self.book_id}, member_id={self.member_id}, "
            f"borrow_date={self.borrow_date}, return_date={self.return_date})>"
        )
