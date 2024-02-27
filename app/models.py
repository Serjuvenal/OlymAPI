from sqlalchemy import Column, Integer, String

from app.database import Base


class TeilnehmerModel(Base):
    __tablename__ = "teilnehmer"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=False, index=True)
    vorname = Column(String)
    nachname = Column(String)
