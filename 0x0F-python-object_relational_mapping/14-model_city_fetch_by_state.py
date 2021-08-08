#!/usr/bin/python3
"""Is a script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa"""

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.schema import MetaData


if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State
    from model_city import City

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    states_cities = session.query(City).join(State).order_by(City.id)

    for data in states_cities:
        print("{}: ({}) {}".format(data.state.name, data.id, data.name))

    session.close()
