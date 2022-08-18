from typing import List
from fastapi import FastAPI, Depends, Request, Form, status
import os
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine, get_db



from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://127.0.0.1:5500/docs/index.html",
    "https://78eviu.deta.dev",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "welcome"}

@app.post("/add")
def add_food(request: Request, food: str = Form(...), amount: float = Form(...), db: Session = Depends(get_db)):
    new_food = models.Food(food_type=food, amount=amount)
    db.add(new_food)
    db.commit()
    
    return new_food

@app.get("/all-foods", response_model=List[schemas.Food])
def get_all_foods(db: Session = Depends(get_db)):
    return db.query(models.Food).all()