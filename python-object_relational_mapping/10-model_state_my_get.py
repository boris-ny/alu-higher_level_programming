#!/usr/bin/python3
"""A script that prints the State object with the name passed as argument"""

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
    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
