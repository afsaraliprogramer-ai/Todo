from fastapi import Depends , HTTPException , Request , status
from utils.jwtToken import check_token


def get_current_user(request : Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token not found"
        )

    user_id = check_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_id