#!/usr/bin/python3
"""A script that deletes \
    all State objects with a name containing the letter a"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    jid = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(argv[1], argv[2], argv[3]),
                        pool_pre_ping=True)

    Base.metadata.create_all(jid)
    yeat = sessionmaker(bind=jid)
    session = yeat()
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()
    session.close()
