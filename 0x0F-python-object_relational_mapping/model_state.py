#!/usr/bin/python3
"""Module conatains a class that represents a user"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column
from sqlalchemy import create_engine
import sys


engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                       f"@localhost:3306/{sys.argv[3]}",
                       pool_pre_ping=True)

Base = declarative_base()


class State(Base):
    """Object representation of a User"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
