#!/usr/bin/python3
"""Lists all States and corresponding cities"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
import sys


if __name__ == "__main__":
    eng = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                        f"@localhost:3306/{sys.argv[3]}",
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query
    list_States = session.query(State).all()

    # Display the results
    if list_States:
        for state in list_States:
            print(f"{state.id}. {state.name}")
            if state.cities:
                for city in state.cities:
                    print(f"    {city.id}. {city.name}")
    session.close()
