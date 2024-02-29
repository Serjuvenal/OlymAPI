from sqlalchemy import Column, Integer, String

from database import Base


class RolleModel(Base):
    __tablename__ = "Rolle"

    id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String)


class RolleDesMitarbeitersModel(Base):
    __tablename__ = "RolleDesMitarbeiters"

    id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String)


class MitarbeiterModel(Base):
    __tablename__ = "Mitarbeiter"

    id = Column(Integer, primary_key=True, index=True)
    vorname = Column(String)
    nachname = Column(String)
    email = Column(String, unique=False, index=True)


class TeilnehmerModel(Base):
    __tablename__ = "teilnehmer"

    id = Column(Integer, primary_key=True, index=True)
    vorname = Column(String)
    nachname = Column(String)
    alter = Column(String)
    team_id = Column(String)
