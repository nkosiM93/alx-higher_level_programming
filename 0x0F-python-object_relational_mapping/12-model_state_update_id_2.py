#!/usr/bin/python3
"""Script changes the name of a queried State"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                        f"@localhost:3306/{sys.argv[3]}",
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query
    ns = session.query(State).filter_by(id=2).one()

    if ns:
        # Change the name
        ns.name = "New Mexico"

        # Commit the changes
        session.commit()
    else:
        print("Not found")

    session.close()
