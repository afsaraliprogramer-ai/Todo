from fastapi import HTTPException , status , Response
from schemas.user import Auth
from sqlalchemy.orm import Session
from models.user import User
from utils.hashing import hash_password , verify_password
from utils.jwtToken import generate_token 
from core.config import settings


def create_account(user : Auth , db : Session)->dict:
    old_user = db.query(User).filter(User.email == user.email).first()
    if old_user and old_user.is_active:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="User already exist")
    hash_pass = hash_password(user.password)
    new_user = User(
        email = user.email,
        password = hash_pass
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message" : "Successfully create account"}


def check_account(user : Auth ,response : Response , db : Session)->dict:
    old_user = db.query(User).filter(User.email == user.email , User.is_active == True).first()
    if old_user is None or not verify_password(user.password, old_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials"
        )
    if not old_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account inactive"
        )
    token =  generate_token({"sub" : str(old_user.id)})
    response.set_cookie(
        key = "access_token",
        value = token,
        httponly=True,
        secure=False,
        samesite="lax"
    )
    return {"message" : "Successfully login"}
    



def delete_account(user_id : int , db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Account already deleted")
    user.is_active = False
    db.commit()
        
