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