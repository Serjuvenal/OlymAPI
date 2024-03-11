from sqlalchemy import ForeignKey, Column, Integer, String, Date, DateTime, Boolean, Enum

from database import Base
from schemas import Roles


class RolleModel(Base):
    __tablename__ = "Rolle"

    rolle_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String)


class RolleDesMitarbeitersModel(Base):
    __tablename__ = "RolleDesMitarbeiters"

    rolledesmitarbeiters_id = Column(Integer, primary_key=True, index=True, unique=True)
    rolle_id = Column(Integer, ForeignKey('Rolle.rolle_id'), index=True)
    mitarbeiter_id = Column(Integer, ForeignKey('Mitarbeiter.mitarbeiter_id'), index=True)


class MitarbeiterModel(Base):
    __tablename__ = "Mitarbeiter"

    mitarbeiter_id = Column(Integer, primary_key=True, index=True, unique=True)
    vorname = Column(String)
    nachname = Column(String)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True)
    kennwort = Column(String)
    is_active = Column(Boolean, default=False)


class WettbewerbMitarbeiterModel(Base):
    __tablename__ = "WettbewerbMitarbeiter"

    wettbewerbmitarbeiter_id = Column(Integer, primary_key=True, index=True, unique=True)
    wettbewerb_id = Column(Integer, ForeignKey('Wettbewerb.wettbewerb_id'), index=True)
    mitarbeiter_id = Column(Integer, ForeignKey('Mitarbeiter.mitarbeiter_id'), index=True)


class WettbewerbModel(Base):
    __tablename__ = "Wettbewerb"

    wettbewerb_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String)
    datum = Column(Date)
    start = Column(DateTime)
    dauer = Column(Integer)
    sportart_id = Column(Integer, ForeignKey('Sportart.sportart_id'), index=True)
    sportstaette_id = Column(Integer, ForeignKey('Sportstaette.sportstaette_id'), index=True)


class SportartModel(Base):
    __tablename__ = "Sportart"

    sportart_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String)


class SportstaetteModel(Base):
    __tablename__ = "Sportstaette"

    sportstaette_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String)


class BewertungModel(Base):
    __tablename__ = "Bewertung"

    bewertung_id = Column(Integer, primary_key=True, index=True, unique=True)
    bewertungsart_id = Column(Integer, ForeignKey('Bewertungsart.bewertungsart_id'), index=True)
    wettbewerb_id = Column(Integer, ForeignKey('Wettbewerb.wettbewerb_id'), index=True)


class BewertungsartModel(Base):
    __tablename__ = "Bewertungsart"

    bewertungsart_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String)


class WettbewerbTeilnehmer(Base):
    __tablename__ = "WettbewerbTeilnehmer"

    wettbewerbteilnehmer_id = Column(Integer, primary_key=True, index=True, unique=True)
    teilnehmer_id = Column(Integer, ForeignKey('Teilnehmer.teilnehmer_id'), index=True)
    wettbewerb_id = Column(Integer, ForeignKey('Wettbewerb.wettbewerb_id'), index=True)


class TeilnehmerModel(Base):
    __tablename__ = "Teilnehmer"

    teilnehmer_id = Column(Integer, primary_key=True, index=True, unique=True)
    vorname = Column(String)
    nachname = Column(String)
    alter = Column(String)
    team_id = Column(Integer, ForeignKey('Team.team_id'), index=True)


class TeamModel(Base):
    __tablename__ = "Team"

    team_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String)


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String, unique=False, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    role = Column(Enum(Roles), default="user")
