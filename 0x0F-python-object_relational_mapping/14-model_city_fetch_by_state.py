#!/usr/bin/python3
"""Script prints all city objects"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                        f"@localhost:3306/{sys.argv[3]}",
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query
    ns = session.query(City.name, City.id, State.name).\
                 join(State).filter(City.state_id == State.id).all()

    if ns:
        for n, i, sn in ns:
            print(f"{sn}: ({i}) {n}")
    session.close()
