from sqlalchemy import ForeignKey, Column, Integer, String, Date, DateTime

from database import Base


class RolleModel(Base):
    __tablename__ = "Rolle"

    rolle_id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String)


class RolleDesMitarbeitersModel(Base):
    __tablename__ = "RolleDesMitarbeiters"

    rolledesmitarbeiters_id = Column(Integer, primary_key=True, index=True)
    rolle_id = Column(Integer, ForeignKey('Rolle.rolle_id'), index=True)
    mitarbeiter_id = Column(Integer, ForeignKey('Mitarbeiter.mitarbeiter_id'), index=True)


class MitarbeiterModel(Base):
    __tablename__ = "Mitarbeiter"

    mitarbeiter_id = Column(Integer, primary_key=True, index=True)
    vorname = Column(String)
    nachname = Column(String)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    kennwort = Column(String)


class WettbewerbMitarbeiterModel(Base):
    __tablename__ = "WettbewerbMitarbeiter"

    wettbewerbmitarbeiter_id = Column(Integer, primary_key=True, index=True)
    wettbewerb_id = Column(Integer, ForeignKey('Wettbewerb.wettbewerb_id'), index=True)
    mitarbeiter_id = Column(Integer, ForeignKey('Mitarbeiter.mitarbeiter_id'), index=True)


class WettbewerbModel(Base):
    __tablename__ = "Wettbewerb"

    wettbewerb_id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String)
    datum = Column(Date)
    start = Column(DateTime)
    dauer = Column(Integer)
    sportart_id = Column(Integer, ForeignKey('Sportart.sportart_id'), index=True)
    sportstaette_id = Column(Integer, ForeignKey('Sportstaette.sportstaette_id'), index=True)


class SportartModel(Base):
    __tablename__ = "Sportart"

    sportart_id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String)


class SportstaetteModel(Base):
    __tablename__ = "Sportstaette"

    sportstaette_id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String)


class BewertungModel(Base):
    __tablename__ = "Bewertung"

    bewertung_id = Column(Integer, primary_key=True, index=True)
    bewertungsart_id = Column(Integer, ForeignKey('Bewertungsart.bewertungsart_id'), index=True)
    wettbewerb_id = Column(Integer, ForeignKey('Wettbewerb.wettbewerb_id'), index=True)


class BewertungsartModel(Base):
    __tablename__ = "Bewertungsart"

    bewertungsart_id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String)


class WettbewerbTeilnehmer(Base):
    __tablename__ = "WettbewerbTeilnehmer"

    wettbewerbteilnehmer_id = Column(Integer, primary_key=True, index=True)
    teilnehmer_id = Column(Integer, ForeignKey('Teilnehmer.teilnehmer_id'), index=True)
    wettbewerb_id = Column(Integer, ForeignKey('Wettbewerb.wettbewerb_id'), index=True)


class TeilnehmerModel(Base):
    __tablename__ = "Teilnehmer"

    teilnehmer_id = Column(Integer, primary_key=True, index=True)
    vorname = Column(String)
    nachname = Column(String)
    alter = Column(String)
    team_id = Column(Integer, ForeignKey('Team.team_id'), index=True)


class TeamModel(Base):
    __tablename__ = "Team"

    team_id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String)
