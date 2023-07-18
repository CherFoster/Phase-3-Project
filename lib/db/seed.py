from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Flight, Passenger, Reservation
import random
import string

if __name__ == "__main__":
    engine = create_engine("sqlite:///flights.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    # Delete methods to clear the database before each seeding
    session.query(Flight).delete()
    session.query(Passenger).delete()
    session.query(Reservation).delete()
    
    # For Flight Class:
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

    for _ in range(75):
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

        session.add(flight)
        session.commit()
        flights.append(flight)

    # Retrieves all instances of the Flight class
    all_flights = session.query(Flight).all()

    # For Passenger Class:
    passengers = []

    for _ in range(100):
        passenger = Passenger(
            first_name = f"{fake.first_name()}",
            last_name = f"{fake.last_name()}",
            phone_number = f"{fake.phone_number()}",
            flight_id = random.choice(all_flights).id
        )

        session.add(passenger)
        session.commit()
        passengers.append(passenger)
   
    all_passengers = session.query(Passenger).all()
    
    # For Reservation Class:
    reservations = []

    classes_list = {
        1 : "First Class",
        2 : "Business Class",
        3 : "Premium Economy Class",
        4 : "Economy Plus",
        5 : "Coach"
    }

    # Generates random confirmation numbers
    def generate_confirmation_number(length=6):
        characters = string.ascii_uppercase + string.digits
        confirmation_number = ''.join(random.choices(characters, k=length))
        return confirmation_number
    
    for _ in range(100):
        for type in classes_list:
            type = random.choice(list(classes_list.keys()))
            confirmation_number = generate_confirmation_number()

            reservation = Reservation(
                confirmation = confirmation_number,
                date = fake.date_between(start_date='today', end_date='+1y'),
                flight_class = classes_list[type],
                flight_id = random.choice(all_flights).id,
                passenger_id = random.choice(all_passengers).id          
        )

        session.add(reservation)
        session.commit()
        reservations.append(reservation)
