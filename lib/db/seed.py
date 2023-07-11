from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///band_lockers.db")
session = Session(engine, future=True)

# _Create instances of classes here..._

session.close()
session.commit()