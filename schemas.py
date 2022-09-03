from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    

class FoodBase(BaseModel):
    food_type: str
    amount: float


class FoodCreate(FoodBase):
    pass


class Food(FoodBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]

class Info(BaseModel):
    product_name: str
    barcode: int
    carbohydrates_100g: Optional[float]
    energy_kcal_100g: Optional[float]
    fat_100g: Optional[float]
    fruits_vegetables_nuts_estimate_from_ingredients_100g: Optional[float]
    nutrition_score_fr_100g: Optional[float]
    proteins_100g: Optional[float]
    salt_100g: Optional[float]
    saturated_fat_100g: Optional[float]
    sodium_100g: Optional[float]
    sugars_100g: Optional[float]
    fiber_100g: Optional[float]
    carbon_footprint_from_known_ingredients_100g: Optional[float]
    nova_group_100g: Optional[float]
    energy_kj_100g: Optional[float]
    vitamin_b1_100g: Optional[float]
    vitamin_k_100g: Optional[float]
    biotin_100g: Optional[float]
    magnesium_100g: Optional[float]
    phosphorus_100g: Optional[float]
    vitamin_b9_100g: Optional[float]
    vitamin_e_100g: Optional[float]
    vitamin_pp_100g: Optional[float]
    calcium_100g: Optional[float]
    vitamin_b12_100g: Optional[float]
    vitamin_b2_100g: Optional[float]
    vitamin_d_100g: Optional[float]

    class Config:
        orm_mode = True