#!/usr/bin/python3
"""
Script demonstrates how to query a database using sqlalchmey
Script demonstrates how to query a database using sqlalchmey
Script demonstrates how to query a database using sqlalchmey
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:"
            f"3306/{sys.argv[3]}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    # The query
    query = session.query(State).order_by(State.id)

    for state in query:
        print(f'{state.id}: {state.name}')
