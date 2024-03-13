from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey, Column, Integer, String, Date, DateTime
from fastapi_users.db import SQLAlchemyBaseUserTable

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

Base = declarative_base()

###########
# MODELLE
###########


class User(SQLAlchemyBaseUserTable, Base):
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10), unique=True)


class WettbewerbMitarbeiterModel(Base):
    __tablename__ = "WettbewerbMitarbeiter"

    wettbewerbmitarbeiter_id = Column(Integer, primary_key=True, index=True, unique=True)
    wettbewerb_id = Column(Integer, ForeignKey('Wettbewerb.wettbewerb_id'), index=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), index=True)


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
    startnummer = Column(Integer, unique=True)
    team_id = Column(Integer, ForeignKey('Team.team_id'), index=True)


class TeamModel(Base):
    __tablename__ = "Team"

    team_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String)


###########
# MODELLE
###########


async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_and_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session():
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session=session, user_table=User)
