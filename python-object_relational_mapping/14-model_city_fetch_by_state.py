#!/usr/bin/python3
"""A script that lists all City objects from the database hbtn_0e_14_usa"""
from model_city import Base, City
from model_state import State
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
    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
