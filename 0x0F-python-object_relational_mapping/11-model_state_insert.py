#!/usr/bin/python3
"""Is a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.schema import MetaData


if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    word = "Louisiana"
    session.add(State(name=word))
    session.commit()

    new_state = session.query(State).filter(State.name.like(word)).first()

    print("{}".format(new_state.id))

    session.close
