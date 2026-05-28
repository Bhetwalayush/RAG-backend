from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    date = Column(String)
    time = Column(String)