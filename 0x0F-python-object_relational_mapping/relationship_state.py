#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance
"""
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.orm import relationship

class State(Base):
    """
    State class that inherits from Base

    Attributes:
        id: Id state
        name: Name of state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
