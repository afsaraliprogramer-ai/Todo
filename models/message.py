from sqlalchemy import Column , Integer , String , Boolean , ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer , primary_key=True , index=True)
    message = Column(String , nullable=False)
    is_completed = Column(Boolean , default=False)
    owner_id = Column(Integer , ForeignKey("users.id"))
    owner = relationship("User" , back_populates="mess")