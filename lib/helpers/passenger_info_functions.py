from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Flight, Passenger

engine = create_engine("sqlite:///db/flights.db")
session = Session(engine, future=True)

all_passengers = session.query(Passenger).order_by(Passenger.last_name).all()

def view_all_passengers():
    for pax in all_passengers:
        print(f"First name: {pax.first_name} \nLast name: {pax.last_name}")
        print(f"Phone number: {pax.phone_number}")

        flight_details = session.query(Flight).filter_by(id=pax.flight_id).first()
        if flight_details:
            print(f"Flying on: {flight_details.airline} \nFlight #: {flight_details.flight_number} ")
        print("")

def view_pax_count():
    print("")
    flight_number = input("Enter the flight number: ")
    passengers = session.query(Passenger).join(Flight).filter(Flight.flight_number == flight_number).all()
    print("")

    if passengers:
        print(f"Passengers for Flight #{flight_number}:")
        print("")
        for passenger in passengers:
            print(f"First name: {passenger.first_name}\nLast name: {passenger.last_name}")
            print(f"Phone number: {passenger.phone_number}")
            print("")
    else:
        print("Flight number not found.")

def search_by_last_name():
    print("")
    search_names = input("Search by last name: ")
    print("")
    searched = session.query(Passenger).filter(Passenger.last_name == search_names).all()
    
    if searched:
        for person in searched:
            print(f"First name: {person.first_name} \nLast name: {person.last_name}")
            print(f"Phone number: {person.phone_number}")
            print("")
    else:
        print("No passengers found with the given last name.")
