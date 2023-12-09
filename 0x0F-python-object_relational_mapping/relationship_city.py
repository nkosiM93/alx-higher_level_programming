#!/usr/bin/python3
"""City class is contained here"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class City(Base):
    """Models a table of cities"""

    # Class attributes that represent the different columns
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")
