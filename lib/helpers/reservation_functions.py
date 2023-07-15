from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Flight, Passenger, Reservation

engine = create_engine("sqlite:///db/flights.db")
session = Session(engine, future=True)

all_reservations = session.query(Reservation).all()