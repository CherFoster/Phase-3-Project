# Airbook

***

## Description

Airbook is an application program that is ran from the command-line that allows you to view flight, passenger, and reservation information, as well as creating and deleting reservations for passengers.

***

## Getting Started

Fork and clone this repository and navigate into its directory to get started. Make sure you have Python and SQLAlchemy installed before running the application. Install SQLAlchemy by running <code>pip install sqlalchemy</code>. Run <code>pipenv install</code> to install any dependencies, and enter the virtual environment by running <code>pipenv shell</code>. Navigate into the lib/db directory and run <code>python seed.py</code> in the terminal to generate fake data to the database. Once the data has been created, change directories back into the lib folder and run <code>python cli.py</code> to run the Airbook application.

### File Structure
Models.py, seed.py, and the flights database are located in the lib/db directory. 

<code>Models.py</code> contains the database structure where the tables and columns were created.

<code>Seed.py</code> contains the code where the data instances are created and inserted into the database.

Also located in lib/db is a folder where helper functions were created. These functions were imported into <code>cli.py</code> in the lib directory. The 3 files in the helpers folder contains code that provides functionality for the 3 tables. 

- <code>flight_info_functions.py</code>:
    - This file allows you to view every flight and its generated information including the airline, flight number, origin, destination, and departure and arrival time. Similarly to an airline's booking website or a search engine, you can also search flights by airline, origin, or destination.

- <code>passenger_info_functions.py</code>:
    - This file contains functions for all passenger information including names and phone numbers. You can view all the passengers that are on associated with a specific flight, and can look up passenger information by searching for the passenger's last name.

- <code>reservation_functions.py</code>: 
    - This file allows you to perform CRUD actions on the Reservation database. You can view all reservations, search for a reservation by inputing a confirmation number, as well as create new reservations and delete existing reservations. The Reservations class is associated with both the Flight and Passenger classes so that when a new reservation is created or deleted, it will also add the inputed reservation info to the flight and passenger databases.

### Visuals

<a href="https://imgur.com/mNyjptI"><img src="https://i.imgur.com/mNyjptI.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/A2Tunt0"><img src="https://i.imgur.com/A2Tunt0.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/9uvvBnB"><img src="https://i.imgur.com/9uvvBnB.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/P83VoOs"><img src="https://i.imgur.com/P83VoOs.png" title="source: imgur.com" /></a>




