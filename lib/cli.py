#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Flight, Passenger, Reservation
from pyfiglet import Figlet
import sys
import importlib

engine = create_engine("sqlite:///db/flights.db")
session = Session(engine, future=True)

sys.path.append('./helpers')

flight_info_functions = importlib.import_module('flight_info_functions')
passenger_info_functions = importlib.import_module('passenger_info_functions')

def greeting():
    print("")
    print(Figlet(font = "starwars").renderText("AirBook"))

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
            greeting()
            main()

def exit():
    print(Figlet(font = "cybermedium").renderText("Goodbye"))
    print("See you next time in the friendly skies!")
    print("")

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
            while flight_choice != 5:
                print(Figlet(font = "cybermedium").renderText("Flight Info"))
                print('''
                    1) View all flights
                    2) Search by airline
                    3) Search by origin
                    4) Search by destination 
                    5) Main Menu 
                      ''')
                flight_choice = int(input("               Enter number : "))

                if flight_choice == 1:
                    flight_info_functions.view_all_flights()
                    navigate_back()

                if flight_choice == 2:
                    flight_info_functions.view_by_airline()
                    navigate_back()

                if flight_choice == 3:
                    flight_info_functions.view_by_origin()
                    navigate_back()

                if flight_choice == 4:
                    flight_info_functions.view_by_destination()
                    navigate_back()

                if flight_choice == 5:
                    greeting()
                    main()

        if choice == 2:
            passenger_choice = 0
            while passenger_choice != 4:
                print(Figlet(font = "cybermedium").renderText("Passenger Info"))
                print('''
                    1) View all passengers
                    2) View passengers on flights
                    3) Search by last name
                    4) Main Menu 
                     
                      ''')
                passenger_choice = int(input("               Enter number : "))

                if passenger_choice == 1:
                    passenger_info_functions.view_all_passengers()
                    navigate_back()

                if passenger_choice == 2:
                    passenger_info_functions.view_pax_count()
                    navigate_back()

                if passenger_choice == 3:
                    passenger_info_functions.search_by_last_name()
                    navigate_back()

                if passenger_choice == 4:
                    greeting()
                    main()

        
        if choice == 4:
            exit()

if __name__ == '__main__':
    greeting()
    main()