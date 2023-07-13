from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Flight, Passenger, Reservation
import random

if __name__ == "__main__":
    engine = create_engine("sqlite:///flights.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete methods to clear the database before each seeding
    session.query(Flight).delete()
    session.query(Passenger).delete()
    session.query(Reservation).delete()

    fake = Faker()

    flights = []

    list_of_airlines = [
        "United",
        "Southwest",
        "Frontier",
        "Jet Blue",
        "Spirit",
        "American",
        "Delta",
        "Alaska",
        "SkyWest",
        "Lufthansa"
    ]

    for _ in range(10):
        departure_time = fake.time_object()
        arrival_time = fake.time_object()

        flight = Flight(
            airline = random.choice(list_of_airlines),
            flight_number = random.randint(100, 9999),
            origin = f"{fake.city()}",
            destination = f"{fake.city()}",
            departure_time = departure_time.strftime("%H:%M"),
            arrival_time = arrival_time.strftime("%H:%M")
        )
        flights.append(flight)
        session.add(flight)
        session.commit()
    



    # passengers = []
    # phone=random.randint(1000000000, 9999999999)


    # reservations = []

















    # session.close()