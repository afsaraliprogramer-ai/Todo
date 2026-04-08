from pydantic import BaseModel , EmailStr , Field

class Auth(BaseModel):
    email : EmailStr 
    password : str = Field(min_length=8)




