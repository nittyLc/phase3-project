from sqlalchemy import Column, Integer, String
from lib.models import Base

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Member(id={self.id}, name='{self.name}', email='{self.email}')>"
