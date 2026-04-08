from pydantic import BaseModel

class MessageReq(BaseModel):
    mess : str

class Completed(BaseModel):
    is_completed : bool

class MessageRes(BaseModel):
    id : int
    mess : str
    is_completed : bool

    class Config:
        from_attributes = True