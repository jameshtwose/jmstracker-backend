from typing import List
from fastapi import FastAPI, Depends, Request, Form, status
import os
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine, get_db
from routers import post, user, auth

# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

origins = ["https://jameshtwose.github.io", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "welcome"}