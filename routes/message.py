from fastapi import APIRouter , Depends , status
from sqlalchemy.orm import Session
from schemas.message import MessageReq , MessageRes 
from typing import List
from core.db import get_db
from utils.current_user import get_current_user
from repository.message import get_message , create_message ,edit_message , completed_message , deleted_message


route = APIRouter(
    prefix="/message",
    tags=["Message"]

)


@route.get("/" , response_model=List[MessageRes])
async def get_message_route(current_user : int = Depends(get_current_user) , db : Session = Depends(get_db)):
    return get_message(current_user , db)


@route.post("/" , response_model=MessageRes)
async def create_message_route(message : MessageReq , current_user :int = Depends(get_current_user) , db :Session = Depends(get_db)):
    return create_message(current_user, message , db)

@route.patch("/edit/{id}" , response_model=MessageRes)
async def edit_message_route(id :int , message : MessageReq ,current_user :int = Depends(get_current_user), db :Session = Depends(get_db)):
    return edit_message(current_user ,id , message , db)

@route.patch("/completed/{id}" , response_model=MessageRes)
async def completed_message_route(id :int  ,current_user : int = Depends(get_current_user), db :Session = Depends(get_db)):
    return completed_message(current_user , id ,  db)

@route.delete("/{id}" , status_code=status.HTTP_204_NO_CONTENT )
async def delete_message_route(id :int , current_user : int = Depends(get_current_user) ,db :Session = Depends(get_db)):
    deleted_message(current_user , id , db)
    return






