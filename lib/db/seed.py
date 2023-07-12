from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Flight, Passenger, Reservation
import random, datetime

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

    random_hour = random.randint(0, 23)  
    random_minute = random.randint(0, 59) 

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
        flight = Flight(
            airline = random.choice(list_of_airlines),
            flight_number = random.randint(100, 9999),
            origin = f"{fake.city()}",
            destination = f"{fake.city()}",
            departure_time = datetime.time(random_hour, random_minute),
            arrival_time = datetime.time(random_hour, random_minute)
        )
        flights.append(flight)
        session.add(flight)
        session.commit()
    



    passengers = []
    # phone=random.randint(1000000000, 9999999999)


    reservations = []

















    session.close()