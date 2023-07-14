#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Flight, Passenger, Reservation
from pyfiglet import Figlet

engine = create_engine("sqlite:///db/flights.db")
session = Session(engine, future=True)

def greeting():
    print("")
    print(Figlet(font = "cyberlarge").renderText("Flight Info"))

def navigate_back():
    selection = 0
    while selection != 1:
        print('''
                Would you like to do another search?
                    1) Yes
                    2) No - Go back to Main Menu
              ''')
        selection = int(input("               Enter number : ")) 

        if selection == 1:
            print("")

        if selection == 2:
            main()


def main():
    choice = 0
    while choice != 4:
        print("                Welcome Aboard")
        print('''
                What information are you looking for?
              
                    1) Flights
                    2) Passenger Information
                    3) Reservations
                    4) Deplane (Exit) 
              ''')
        choice = int(input("               Enter number : ")) 

        if choice == 1:
            flight_choice = 0
            while flight_choice != 4:
                print(Figlet(font = "standard").renderText("Flights"))
                print('''
                    1) View all flights
                    2) Search by airline
                    3) Search by origin
                    4) Search by destination  
                      ''')
                flight_choice = int(input("               Enter number : "))
                all_flights = session.query(Flight).all()
                if flight_choice == 1:
                    # Set() keeps track of airline names already printed
                    all_airlines = set() 
                    for flight in all_flights:
                        if flight.airline not in all_airlines:
                            print(flight.airline)
                            all_airlines.add(flight.airline)
                    print("")
                    view_airline = input("Enter the name of the airline : ")
                    print("")
                    airline_name = session.query(Flight).filter(Flight.airline.ilike(f"%{view_airline}%")).all()
                    
                    if airline_name:
                        for info in airline_name:
                            print(f"Flight Number: {info.flight_number}")
                            print(f"Origin: {info.origin}")
                            print(f"Destination: {info.destination}")
                            print(f"Departure Time: {info.departure_time}")
                            print(f"Arrival Time: {info.arrival_time}")
                            print("")

                    navigate_back()
                            
                        

if __name__ == '__main__':
    greeting()
    main()