from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Flight, Passenger, Reservation


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
        
        # passenger_details = session.query(Passenger).filter_by(id=rez.passenger_id).first()
        # if passenger_details:
        #     print(f"""
        #         Passenger: {passenger_details.first_name} {passenger_details.last_name}""")

        flight_details = session.query(Flight).filter_by(id=rez.flight_id).first()
        if flight_details:
            print(f"""        Flying on: {flight_details.airline}\n        Flight #: {flight_details.flight_number}""")

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
    pass
