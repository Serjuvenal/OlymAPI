from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, DateTime
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi import Depends
import os


mysqlurlocal = os.getenv("mysqlurlocal")

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db" #async
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase"
# SQLALCHEMY_DATABASE_URL = "mysql+aiomysql:///./olympapi" #async
Base = declarative_base()


engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(SQLAlchemyBaseUserTable, Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10), unique=True)


class WettbewerbMitarbeiterModel(Base):
    __tablename__ = "WettbewerbMitarbeiter"

    wettbewerbmitarbeiter_id = Column(Integer, primary_key=True, index=True, unique=True)
    wettbewerb_id = Column(Integer, ForeignKey('Wettbewerb.wettbewerb_id'), index=True)
    user_id = Column(Integer, ForeignKey('user.id'), index=True)


class SportartModel(Base):
    __tablename__ = "Sportart"

    sportart_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String(45), unique=True)


class WettbewerbModel(Base):
    __tablename__ = "Wettbewerb"

    wettbewerb_id = Column(Integer, primary_key=True, index=True, unique=True)
    termin = Column(DateTime)
    bewertung = Column(Integer)
    sportart_id = Column(Integer, ForeignKey('Sportart.sportart_id'), index=True)
    sportstaette_id = Column(Integer, ForeignKey('Sportstaette.sportstaette_id'), index=True)
    teilnehmer_id = Column(Integer, ForeignKey('Teilnehmer.teilnehmer_id'), index=True)
    bewertungsart_id = Column(Integer, ForeignKey('Bewertungsart.bewertungsart_id'), index=True)
    partner_wettbewerb_id = Column(Integer, ForeignKey('Wettbewerb.wettbewerb_id'))


class SportstaetteModel(Base):
    __tablename__ = "Sportstaette"

    sportstaette_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String, unique=True)


class BewertungsartModel(Base):
    __tablename__ = "Bewertungsart"

    bewertungsart_id = Column(Integer, primary_key=True, index=True, unique=True)
    bezeichnung = Column(String, unique=True)


class TeilnehmerModel(Base):
    __tablename__ = "Teilnehmer"

    teilnehmer_id = Column(Integer, primary_key=True, index=True, unique=True)
    vorname = Column(String)
    nachname = Column(String)
    email = Column(String)
#    team_id = Column(Integer, ForeignKey('Team.team_id'), index=True)


#class TeamModel(Base):
#    __tablename__ = "Team"
#
#    team_id = Column(Integer, primary_key=True, index=True, unique=True)
#    bezeichnung = Column(String, unique=True)


###########
# MODELLE
###########


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
