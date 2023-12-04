#!/usr/bin/python3
"""
Module contains code that extracts all State objects
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost:3306/{sys.argv[3]}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id)
    for state in results:
        print(f"{state.id}: {state.name}")
