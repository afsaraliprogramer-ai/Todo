from sqlalchemy import Column , Integer , String , Boolean
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):

    __tablename__ = "user"
    id = Column(Integer , primary_key=True , index=True)
    email = Column(String , index=True)
    password = Column(String)
    is_active = Column(Boolean , default=True)
    mess = relationship("Message" , back_populates="owner")

