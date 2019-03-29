#!/usr/bin/python3
"""
script to list all State objects with 'a' in name
"""


from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    search = argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()
    print(session.query(State).\
        filter(State.name == func.binary(search)).\
        order_by(State.id).first().id)

    session.close()
