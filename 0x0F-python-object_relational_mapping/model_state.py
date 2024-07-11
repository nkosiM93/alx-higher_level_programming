#!/usr/bin/python

"""
Module creates a State object
"""

from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:"\
                       f"{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
Base = declarative_base()

class State(Base):
    """State class, represents a state"""

    __tablename__ = "states"

    id = Column(Integer, unique=True, autoincrement=True, 
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
