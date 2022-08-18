from sqlalchemy import Boolean, PrimaryKeyConstraint, String, Integer, Column, Float
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from database import Base

class Food(Base):
    __tablename__ = "jmstracker_backend"

    id = Column(Integer, primary_key=True, index=True)
    food_type = Column(String)
    amount = Column(Float, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))