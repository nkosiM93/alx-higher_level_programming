#!/usr/bin/python3
"""Script adds a new state to the database"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                        f"@localhost:3306/{sys.argv[3]}",
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    new_State = State(name="Louisiana")
    session = Session()

    session.add(new_State)
    session.commit()
    ns = session.query(State).filter_by(name='Louisiana').first()
    print(f"{ns.id}")

    session.close()
