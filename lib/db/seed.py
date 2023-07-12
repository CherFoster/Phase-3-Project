from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Flight, Passenger, Reservation
import random

if __name__ == "__main__":
    engine = create_engine("sqlite:///flights.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()