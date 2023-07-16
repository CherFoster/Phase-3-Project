from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Flight

engine = create_engine("sqlite:///db/flights.db")
session = Session(engine, future=True)

all_flights = session.query(Flight).all()

def view_all_flights():
    for flights in all_flights:
        print(f"""
        {flights.airline}
        ---------------
        Flight Number: {flights.flight_number}
        Origin: {flights.origin}
        Destination: {flights.destination}
        Departure Time: {flights.departure_time}
        Arrival Time: {flights.arrival_time}""")
        print("")

def view_by_airline():
    # Set() keeps track of airline names already printed
    all_airlines = set() 
    for airline in all_flights:
        if airline.airline not in all_airlines:
            print(airline.airline)
            all_airlines.add(airline.airline)
    print("")
    view_airline = input("Enter the name of the airline : ")
    print("")
    airline_name = session.query(Flight).filter(Flight.airline.ilike(f"%{view_airline}%")).all()
                    
    if airline_name:
        for info in airline_name:
            print(f"""
                    {info.airline}
                    ---------------
                    Flight Number: {info.flight_number}
                    Origin: {info.origin}
                    Destination: {info.destination}
                    Departure Time: {info.departure_time}
                    Arrival Time: {info.arrival_time}""")
            print("")
    else:
        print("No airlines found with that name.")

def view_by_origin():
    for origin in all_flights:
        print(origin.origin)
    print("")
    view_origin = input("Enter the city you are flying out from : ")
    print("")
    origin_name = session.query(Flight).filter(Flight.origin.ilike(f"%{view_origin}%")).all()
    
    if origin_name:
        for origin in origin_name:
            print(f"""
            {origin.airline} || Origin: {origin.origin}
            ---------------
            Flight Number: {origin.flight_number}
            Destination: {origin.destination}
            Departure Time: {origin.departure_time}
            Arrival Time: {origin.arrival_time}""")
            print("")

    else:
        print("No flights found with that origin.")

def view_by_destination():
    for destination in all_flights:
        print(destination.destination)
    print("")
    view_destination = input("Enter the city you are flying to : ")
    print("")
    destination_name = session.query(Flight).filter(Flight.destination.ilike(f"%{view_destination}%")).all()

    if destination_name:
        for destination in destination_name:
            print(f"""
            {destination.airline} || Destination: {destination.destination}
            ---------------
            Flight Number: {destination.flight_number}
            Origin: {destination.origin}
            Departure Time: {destination.departure_time}
            Arrival Time: {destination.arrival_time}""")
            print("")

    else:
        print("No flights found with that destination.")

