from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer(), primary_key=True)
    airline = Column(String())
    flight_number = Column(Integer())
    origin = Column(String())
    destination = Column(String())
    departure_time = Column(Integer())
    arrival_time = Column(Integer())
    passengers = relationship('Passenger', backref=backref('flight'))
    reservations = relationship('Reservation', backref=backref('flight'))

    def __repr__(self):
        return (
            f"ID: {self.id}" + \
            f"Airline: {self.airline}" + \
            f"Flight Number: {self.flight_number}" + \
            f"Origin: {self.origin}" + \
            f"Destination: {self.destination}" + \
            f"Departure Time: {self.departure_time}" + \
            f"Arrival Time: {self.arrival_time}"
        )

    
class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    phone_number = Column(Integer())
    flight_id = Column(Integer(), ForeignKey('flights.id'))

    def __repr__(self):
        return (
            f"ID: {self.id}" + \
            f"Name: {self.first_name} {self.last_name}" + \
            f"Phone Number: {self.phone_number}"
        )


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer(), primary_key=True)
    confirmation = Column(String())
    date = Column(DateTime())
    flight_id = Column(Integer(), ForeignKey('flights.id'))

    def __repr__(self):
        return (
            f"ID: {self.id}" + \
            f"Confirmation Number: {self.confirmation}" + \
            f"Date: {self.date}"
        )