from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
import models, schemas
from database import get_db


router = APIRouter(
    prefix="/info",
    tags=["info"]
)

@router.get("/", response_model=List[schemas.Info])
def get_foods_information(db: Session = Depends(get_db)):
    
    nutritional_information = db.query(models.Info).all()
    return nutritional_information