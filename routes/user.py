from fastapi import APIRouter , Depends  ,status , Response , Request
from schemas.user import Auth
from core.db import get_db
from sqlalchemy.orm import Session
from repository.user import create_account , check_account , delete_account
from utils.current_user import get_current_user

route = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)



@route.post("/sign" , status_code=status.HTTP_201_CREATED)
async def sign(user :Auth , db : Session = Depends(get_db)):
    return create_account(user , db)

@route.post("/login")
async def login(user :Auth , response : Response ,db : Session = Depends(get_db)):
    return check_account(user ,  response , db)

@route.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logged out successfully"}


@route.delete("/" , status_code= status.HTTP_204_NO_CONTENT)
async def delete(user_id :int =Depends(get_current_user) , db : Session=Depends(get_db)):
    delete_account(user_id , db)
    return

