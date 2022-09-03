from sqlalchemy import ForeignKey, Boolean, PrimaryKeyConstraint, String, Integer, Column, Float
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

from database import Base

class Food(Base):
    __tablename__ = "jmstracker_backend"

    id = Column(Integer, primary_key=True, nullable=False)
    food_type = Column(String)
    amount = Column(Float, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    owner_id = Column(Integer, ForeignKey(column="users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


class Info(Base):
    __tablename__ = "nutritional_information"

    product_name = Column(String, nullable=False, unique=True)
    barcode = Column(Integer, primary_key=True, nullable=False)
    carbohydrates_100g = Column(Float, default=False)
    energy_kcal_100g = Column(Float, default=False)
    fat_100g = Column(Float, default=False)
    fruits_vegetables_nuts_estimate_from_ingredients_100g = Column(Float, default=False)
    nutrition_score_fr_100g = Column(Float, default=False)
    proteins_100g = Column(Float, default=False)
    salt_100g = Column(Float, default=False)
    saturated_fat_100g = Column(Float, default=False)
    sodium_100g = Column(Float, default=False)
    sugars_100g = Column(Float, default=False)
    fiber_100g = Column(Float, default=False)
    carbon_footprint_from_known_ingredients_100g = Column(Float, default=False)
    nova_group_100g = Column(Float, default=False)
    energy_kj_100g = Column(Float, default=False)
    vitamin_b1_100g = Column(Float, default=False)
    vitamin_k_100g = Column(Float, default=False)
    biotin_100g = Column(Float, default=False)
    magnesium_100g = Column(Float, default=False)
    phosphorus_100g = Column(Float, default=False)
    vitamin_b9_100g = Column(Float, default=False)
    vitamin_e_100g = Column(Float, default=False)
    vitamin_pp_100g = Column(Float, default=False)
    calcium_100g = Column(Float, default=False)
    vitamin_b12_100g = Column(Float, default=False)
    vitamin_b2_100g = Column(Float, default=False)
    vitamin_d_100g = Column(Float, default=False)