#!/usr/bin/python3
"""Script prints all city objects"""
import sys
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                        f"@localhost:3306/{sys.argv[3]}",
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    Base.metadata.create_all(eng)

    newState = State(name="California", cities=[City(name="San Francisco")])
    session.add(newState)
    session.commit()
    session.close()
