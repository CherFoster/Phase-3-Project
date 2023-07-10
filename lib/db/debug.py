from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import (Flight, Passenger, Reservation)

if __name__ == '__main__':
    engine = create_engine("sqlite:///flights.db")
    session = Session(engine, future=True)

    import ipdb; ipdb.set_trace()