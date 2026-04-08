from sqlalchemy.orm import Session
from models.message import Message
from fastapi import HTTPException , status
from schemas.message import MessageReq 


def get_user_message(db: Session, message_id: int, user_id: int):
    message = db.query(Message).filter(
        Message.id == message_id,
        Message.owner_id == user_id
    ).first()

    if message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Message not found"
        )

    return message

def get_message(current_user : int , db:Session):
    data = db.query(Message).filter(Message.owner_id == current_user).order_by(Message.id.desc()).all()
    return data


def create_message(current_user : int , message:MessageReq , db : Session):
    new_mess = Message(
        message = message.message,
        owner_id = current_user
    )
    db.add(new_mess)
    db.commit()
    db.refresh(new_mess)
    return new_mess

def edit_message(current_user:int , message_id : int , message:MessageReq , db : Session):
    old_message = get_user_message(db , message_id , current_user)
    old_message.message = message.message
    db.commit()
    db.refresh(old_message)
    return old_message

def completed_message(current_user : int , message_id : int ,  db : Session):
    old_message = get_user_message(db, message_id, current_user)
    old_message.is_completed = not old_message.is_completed
    db.commit()
    db.refresh(old_message)
    return old_message

def deleted_message(current_user : int , message_id : int , db : Session):
    old_message = get_user_message(db, message_id, current_user)
    db.delete(old_message)
    db.commit()