from typing import Any, Sequence

from sqlalchemy import Row
from sqlalchemy.exc import InvalidRequestError, IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app import database
from app import schemas


async def get_sportarten(db: AsyncSession):
    result = await db.execute(database.SportartModel.__table__.select())
    db_sportart = result.fetchall()
    print(type(db_sportart))
    [print(_) for _ in db_sportart]
    return db_sportart


async def create_sportart(db: AsyncSession, sportart: schemas.SportartSchema):
    try:
        async with db.begin():
            db_sportart = database.SportartModel(**sportart.dict())
            db.add(db_sportart)
            await db.flush()
            await db.refresh(db_sportart)
        return db_sportart
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Unable to create sportart: {e}")


def create_wettbewerb(db: Session, wettbewerb: schemas.WettbewerbSchema):
    db_wettbewerb = database.WettbewerbModel(
        bezeichnung=wettbewerb.bezeichnung,
        datum=wettbewerb.datum,
        start=wettbewerb.start,
        dauer=wettbewerb.dauer,
    )
    db.add(db_wettbewerb)
    db.commit()
    db.refresh(db_wettbewerb)
    return db_wettbewerb


def create_sportstaette(db: Session, sportstaette: schemas.SportstaetteSchema):
    db_sportstaette = database.SportstaetteModel(
        bezeichnung=sportstaette.bezeichnung,
    )
    db.add(db_sportstaette)
    db.commit()
    db.refresh(db_sportstaette)
    return db_sportstaette


def create_bewertungsart(db: Session, bewertungsart: schemas.BewertungsartSchema):
    db_bewertungsart = database.BewertungsartModel(
        bezeichnung=bewertungsart.bezeichnung,
    )
    db.add(db_bewertungsart)
    db.commit()
    db.refresh(db_bewertungsart)
    return db_bewertungsart


def create_teilnehmer(db: Session, teilnehmer: schemas.TeilnehmerSchema):
    db_teilnehmer = database.TeilnehmerModel(
        vorname=teilnehmer.vorname,
        nachname=teilnehmer.nachname,
        alter=teilnehmer.alter,
        team_id=teilnehmer.team_id,
    )
    db.add(db_teilnehmer)
    db.commit()
    db.refresh(db_teilnehmer)
    return db_teilnehmer


def create_team(db: Session, team: schemas.TeamSchema):
    db_team = database.TeamModel(
        bezeichnung=team.bezeichnung,
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


# REGION GET FROM DB


def get_wettbewerbe(db: Session):
    return db.query(database.WettbewerbModel).all()


def get_sportstaetten(db: Session):
    return db.query(database.SportstaetteModel).all()


def get_bewertungsarten(db: Session):
    return db.query(database.BewertungsartModel).all()


def get_teilnehmern(db: Session):
    return (db.query(database.TeilnehmerModel).join()
            .all())


def get_teams(db: Session):
    return db.query(database.TeamModel).all()


def get_teilnehmer_by_vorname(db: Session, vorname: str, nachname: str):
    return (
        db.query(database.TeilnehmerModel).filter(
            database.TeilnehmerModel.vorname == vorname,
            database.TeilnehmerModel.nachname == nachname
        ).all()
    )
