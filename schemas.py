from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Food(BaseModel):
    id: int
    food_type: str
    amount: float
    created_at: datetime
    
    class Config:
        orm_mode = True
