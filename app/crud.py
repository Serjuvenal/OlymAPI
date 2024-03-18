from typing import Any, Sequence
from sqlalchemy import Row
from sqlalchemy.exc import InvalidRequestError, IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app import database
from app import schemas


# noinspection PyTypeChecker
async def datalist_to_dict(data: list):
    data_dict = {}
    for zeile in data:
        key, value = zeile
        data_dict[key] = value
    return data_dict


async def get_sportarten(db: AsyncSession):
    result = await db.execute(database.SportartModel.__table__.select())
    liste = result.fetchall()
    sportarten = await datalist_to_dict(liste)
    return sportarten


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


async def get_sportstaetten(db: AsyncSession):
    result = await db.execute(database.SportstaetteModel.__table__.select())
    liste = result.fetchall()
    sportstaetten = await datalist_to_dict(liste)
    return sportstaetten


async def create_sportstaette(db: AsyncSession, sportstaette: schemas.SportstaetteSchema):
    try:
        async with db.begin():
            db_sportstaette = database.SportstaetteModel(**sportstaette.dict())
            db.add(db_sportstaette)
            await db.flush()
            await db.refresh(db_sportstaette)
        return db_sportstaette
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Unable to create sportart: {e}")


async def create_teilnehmer(db: AsyncSession, teilnehmer: schemas.TeilnehmerSchema):
    try:
        async with db.begin():
            db_teilnehmer = database.TeilnehmerModel(**teilnehmer.dict())
            db.add(db_teilnehmer)
            await db.flush()
            await db.refresh(db_teilnehmer)
        return db_teilnehmer
    except IntegrityError as e:
        await db.rollback()
        raise ValueError(f"Unable to create teilnehmer: {e}")


async def get_teilnehmer_by_vorname(db: AsyncSession, vorname: str):
    result = await db.execute(database.TeilnehmerModel.__table__.select().filter(
        database.TeilnehmerModel.vorname == vorname,
            ))
    liste = result.fetchall()
    data_dict = []
    for zeile in liste:
        # [print(zeile)]
        keys = ["teilnehmer_id", "vorname", "nachname", "alter", "startnummer", "team_id"]
        data_dict.append(dict(zip(keys, zeile)))
    return data_dict


async def get_all_teilnehmer(db: AsyncSession):
    result = await db.execute(database.TeilnehmerModel.__table__.select())
    liste = result.fetchall()
    data_dict = []
    for zeile in liste:
        # [print(zeile)]
        keys = ["teilnehmer_id","vorname","nachname","alter", "startnummer", "team_id"]
        data_dict.append(dict(zip(keys,zeile)))
    return data_dict


async def get_team_by_id(db: AsyncSession, team_id: int):
    try:
        db_team = await db.get(database.TeamModel, team_id)
        return db_team
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Unable to find team: {e}")


async def get_teams(db: AsyncSession):
    result = await db.execute(database.TeamModel.__table__.select())
    liste = result.fetchall()
    teams = await datalist_to_dict(liste)
    return teams


async def create_team(db: AsyncSession, team: schemas.TeamSchema):
    try:
        async with db.begin():
            db_team = database.TeamModel(**team.dict())
            db.add(db_team)
            await db.flush()
            await db.refresh(db_team)
        return db_team
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Unable to create team: {e}")


async def update_team(team_id: int, team: schemas.TeamSchema, db: AsyncSession):
    try:
        db_team = await db.get(database.TeamModel, team_id)
        if db_team is None:
            raise ValueError("El equipo no existe.")
        db_team.bezeichnung = team.bezeichnung

        await db.commit()
        [print(db_team.bezeichnung)]
        return db_team
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al actualizar el equipo: {e}")


async def delete_team(db: AsyncSession, team: database.TeamModel):
    try:
        await db.delete(team)
        await db.commit()
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al eliminar el equipo: {e}")