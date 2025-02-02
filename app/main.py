from fastapi import FastAPI # Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
#from fastapi.params import Body
#from pydantic import BaseModel
#from typing import Optional, List
#from random import randrange


from . import models #schemas, utils
from .database import engine #get_db
#from sqlalchemy.orm import Session
from .routers import post, user, auth, vote
from .config import settings

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}




