from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Relationship to Borrow
    borrows = relationship("lib.models.borrow.Borrow", back_populates="member")

    def __repr__(self):
        return f"<Member(name='{self.name}', email='{self.email}')>"
