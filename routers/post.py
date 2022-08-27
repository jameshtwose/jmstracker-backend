from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import models, schemas, oauth2
from database import get_db


router = APIRouter(
    prefix="/foods",
    tags=["foods"]
)

@router.get("/", response_model=List[schemas.Food])
def get_foods(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    foods = db.query(models.Food).filter(models.Food.owner_id == current_user.id).all()
    return foods


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Food)
def create_foods(food: schemas.FoodCreate, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    
    new_food = models.Food(owner_id=current_user.id, **food.dict())
    db.add(new_food)
    db.commit()
    db.refresh(new_food)

    return new_food


@router.get("/{id}", response_model=schemas.Food)
def get_food(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    food = db.query(models.Food).filter(models.Food.id == id).first()

    if food is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"food with id: {id} does not exist")
        
    if food.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    return food


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_food(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    food_query = db.query(models.Food).filter(models.Food.id == id)
    food = food_query.first()

    if food is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"food with id: {id} does not exist")
    
    if food.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
        

    food_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Food)
def update_food(id: int, updated_food: schemas.FoodCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):

    food_query = db.query(models.Food).filter(models.Food.id == id)
    food = food_query.first()
    if food is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"food with id: {id} does not exist")

    if food.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    food_query.update(updated_food.dict(), synchronize_session=False)

    db.commit()

    return food_query.first()