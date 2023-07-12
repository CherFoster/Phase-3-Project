#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pyfiglet import Figlet

engine = create_engine("sqlite:///db/flights.db")
session = Session(engine, future=True)

def main():
    choice = 0
    while choice != 4:
        print("Flight Info")
        print("Welcome...")
        print('''
                What information would you like to look up?
                    1) Flights
                    2) Passenger Information
                    3) Reservations
                    4) Exit 
              ''')
        choice = int(input("                Enter : ")) 

if __name__ == 'main':
    main()