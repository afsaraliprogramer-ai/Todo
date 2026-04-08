from fastapi import FastAPI 
from routes.user import route as user
from routes.message import route as message
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allowed frontend
    allow_credentials=True,
    allow_methods=["*"],         # GET, POST, etc.
    allow_headers=["*"],         # all headers
)

app.include_router(user , prefix="/auth")
app.include_router(
    message,
    prefix="/message",
)