from sqlalchemy import Column, Integer, String

from fastapi.app.database import Base


class TeilnehmerModel(Base):
    __tablename__ = "teilnehmer"

    id = Column(Integer, primary_key=True, index=True)
    vorname = Column(String)
    nachname = Column(String)
    land = Column(String)
    email = Column(String, unique=False, index=True)
