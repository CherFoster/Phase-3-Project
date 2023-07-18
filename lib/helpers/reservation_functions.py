from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Flight, Passenger, Reservation
from datetime import datetime

engine = create_engine("sqlite:///db/flights.db")
session = Session(engine, future=True)

all_reservations = session.query(Reservation).all()

def view_all_reservations():
    for rez in all_reservations:
        print(f"""
        Reservation:
        ---------------
        Confirmation: {rez.confirmation}
        Date: {rez.date}
        Class: {rez.flight_class}""")
        
        passenger_details = session.query(Passenger).filter_by(id=rez.passenger_id).first()
        if passenger_details:
            print(f"        Passenger: {passenger_details.first_name} {passenger_details.last_name}")

        flight_details = session.query(Flight).filter_by(id=rez.flight_id).first()
        if flight_details:
            print(f"""        Airline: {flight_details.airline}\n        Flight #: {flight_details.flight_number}""")

def search():
    print("")
    confirmation_search = input("Search by confirmation number: ")
    print("")
    searched = session.query(Reservation).filter(Reservation.confirmation == confirmation_search).all()
    
    if searched:
        for number in searched:
            print(f"""
             ---------------
             Confirmation: {number.confirmation}
             Date: {number.date}
             Class: {number.flight_class}""")
            passenger_details = session.query(Passenger).filter_by(id=number.passenger_id).first()
            if passenger_details:
                print(f"             Passenger: {passenger_details.first_name} {passenger_details.last_name}")

            flight_details = session.query(Flight).filter_by(id=number.flight_id).first()
            if flight_details:
                print(f"             Airline: {flight_details.airline}\n             Flight #: {flight_details.flight_number}")
        print("")
    else:
        print("No matching confirmation number found.")

def create():
    print("Create a new reservation:")
    print("")
    confirmation = input("Confirmation number (6 Characters max, all caps): ")
    date_str = input("Date (YYYY-MM-DD): ")
    first_name = input("Passenger's First Name: ")
    last_name = input("Passenger's Last Name: ")
    phone_number = input("Phone number: ")
    flight_class = input("Flight class: ")
    flight_id = input("Flight ID: ")

    date = datetime.strptime(date_str, "%Y-%m-%d")

    flight = session.query(Flight).filter_by(id=flight_id).first()
    if flight:
        airline = flight.airline
        flight_number = flight.flight_number

    new_passenger = Passenger(first_name=first_name, last_name=last_name, phone_number=phone_number)
    session.add(new_passenger)
    session.commit()

    new_reservation = Reservation(confirmation=confirmation, date=date, flight_class=flight_class, flight_id=flight_id, passenger=new_passenger)
    session.add(new_reservation)
    session.commit()
    print("Reservation created successfully.")
    print("")
    print("Reservation Details:")
    print("---------------")
    print(f"Confirmation: {new_reservation.confirmation}")
    print(f"Date: {new_reservation.date}")
    print(f"Passenger: {new_reservation.passenger.first_name} {new_reservation.passenger.last_name}")
    print(f"Phone number: {new_reservation.passenger.phone_number}")
    print(f"Class: {new_reservation.flight_class}")
    print(f"Airline: {airline}")
    print(f"Flight #: {flight_number}")
    print(f"Origin: {flight.origin}")
    print(f"Destination: {flight.destination}")

def delete():
    print("Delete an exiting reservation:")
    print("")
    print("Enter the ID of the reservation you want to delete: ")
    inputed = int(input())
    delete_rez = session.query(Reservation).get(inputed)

    # Delete passenger associated with the reservation
    if delete_rez:
        passenger = delete_rez.passenger

    session.delete(delete_rez)
    session.delete(passenger)
    session.commit()
    print("")
    print("Reservation successfully deleted.")
