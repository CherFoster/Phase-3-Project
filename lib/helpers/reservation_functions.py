from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Flight, Passenger, Reservation
from datetime import datetime


engine = create_engine("sqlite:///db/flights.db")
session = Session(engine, future=True)

all_reservations = session.query(Reservation).all()

# Change to view airlines reservations
def view_all_reservations():
    for rez in all_reservations:
        print(f"""
        Reservation:
        ---------------
        Confirmation: {rez.confirmation}
        Date: {rez.date}
        Class: {rez.flight_class}""")
        
        # passenger_details = session.query(Passenger).filter_by(id=rez.passenger_id).first()
        # if passenger_details:
        #     print(f"""
        #         Passenger: {passenger_details.first_name} {passenger_details.last_name}""")

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
        print("")
    else:
        print("No matching confirmation number found.")

def create():
    print("Create a new reservation:")
    print("")
    confirmation = input("Confirmation number: ")
    date_str = input("Date (YYYY-MM-DD): ")
    flight_class = input("Flight class: ")
    flight_id = input("Flight ID: ")

    date = datetime.strptime(date_str, "%Y-%m-%d")

    flight = session.query(Flight).filter_by(id=flight_id).first()
    if flight:
        airline = flight.airline
        flight_number = flight.flight_number

    new_reservation = Reservation(confirmation=confirmation, date=date, flight_class=flight_class, flight_id=flight_id)
    session.add(new_reservation)
    session.commit()
    print("Reservation created successfully.")
    print("Reservation Details:")
    print(f"Confirmation: {new_reservation.confirmation}")
    print(f"Date: {new_reservation.date}")
    print(f"Class: {new_reservation.flight_class}")
    print(f"Airline: {airline}")
    print(f"Flight #: {flight_number}")

def delete():
    print("Delete an exiting reservation:")
    print("")
    print("Enter the ID of the reservation you want to delete: ")
    inputed = int(input())
    delete_rez = session.query(Reservation).get(inputed)
    session.delete(delete_rez)
    session.commit()
    print("")
    print("Reservation successfully deleted.")
