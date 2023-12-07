#!/usr/bin/python3
"""Script deletes an entry"""
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
    ns = session.query(State).all()

    if ns:
        for state in ns:
            if 'a' in state.name:
                session.delete(state)

        # Commit the changes
        session.commit()
    else:
        print("Not found")

    session.close()
