from sqlalchemy import Column , Integer , String , Boolean , ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer , primary_key=True , index=True)
    mess = Column(String)
    is_completed = Column(Boolean , default=False)
    owner_id = Column(Integer , ForeignKey("user.id"))
    owner = relationship("User" , back_populates="mess")