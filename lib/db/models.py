from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer(), primary_key=True)
    flight_number = Column(Integer())
    origin = Column(String())
    destination = Column(String())
    departure_time = Column(Integer())
    arrival_time = Column(Integer())

    def __repr__(self):
        return f"ID: {self.id}" + \
            f"Flight Number: {self.flight_number}" + \
            f"Origin: {self.origin}" + \
            f"Destination: {self.destination}" + \
            f"Departure Time: {self.departure_time}" + \
            f"Arrival Time: {self.arrival_time}"
    

    
class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    phone_number = Column(Integer())
    flight_id = Column(Integer(), ForeignKey('flight.id'))

    def __repr__(self):
        return f"Id: {self.id}" + \
            f"Name: {self.name}" + \
            f"Phone Number: {self.phone_number}" + \
            f"Flight ID: {self.flight_id}"
    
    

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer(), primary_key=True)
    confirmation = Column(String())
    reservation_status = Column(String())
    date = Column(DateTime())
    passenger_id = Column(Integer(), ForeignKey('passenger.id'))

    def __repr__(self):
        return f"ID: {self.id}" + \
            f"Confirmation Number: {self.confirmation}" + \
            f"Reservation Status: {self.reservation_status}" + \
            f"Date: {self.date}" + \
            f"Passenger ID: {self.passenger_id}"
