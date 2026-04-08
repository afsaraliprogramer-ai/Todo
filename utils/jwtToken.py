from jose import JWTError , jwt
from core.config import settings
from datetime import datetime , timedelta , timezone
from fastapi import HTTPException , status

def generate_token(data : dict) ->str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.MINUTES)
    to_encode["exp"] = expire
    return jwt.encode(to_encode , settings.SECRET_KEY , algorithm=settings.ALGORITHM)


def check_token(token : str) ->int:
    try:
        payload = jwt.decode(token , settings.SECRET_KEY , algorithms=[settings.ALGORITHM])
        user_id = (payload.get("sub"))
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Invalid token")
        return int(user_id)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="expire token")
