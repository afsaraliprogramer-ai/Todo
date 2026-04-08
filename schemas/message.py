from pydantic import BaseModel

class MessageReq(BaseModel):
    message : str

class Completed(BaseModel):
    is_completed : bool

class MessageRes(BaseModel):
    id : int
    message : str
    is_completed : bool

    class Config:
        from_attributes = True