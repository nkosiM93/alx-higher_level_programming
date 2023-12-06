#!/usr/bin/python3
"""Prints State object with same name as passed from command line"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                        f"@localhost:3306/{sys.argv[3]}",
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    states = session.query(State).order_by(State.id)

    if states:
        for state in states:
            if sys.argv[4] == state.name:
                print(f"{state.id}")
                sys.exit()
        print("Not Found")
    else:
        print()
