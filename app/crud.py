from typing import Any, Sequence
from sqlalchemy import Row, desc, select, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app import database
from app import schemas


# noinspection PyTypeChecker
async def datalist_to_dict(data: Sequence[Row]):
    data_dict = {}
    for zeile in data:
        key, value = zeile
        data_dict[key] = value
    return data_dict


# SPORTART


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
            raise ValueError(f"Error al crear Sportart: {e}")


async def get_sportarten(db: AsyncSession):
    result = await db.execute(database.SportartModel.__table__.select())
    liste = result.fetchall()
    sportarten = await datalist_to_dict(liste)
    return sportarten


async def get_sportart_by_id(db, sportart_id):
    result = await db.execute(database.SportartModel.__table__.select().filter(
        database.SportartModel.sportart_id == sportart_id,
    ))
    liste = result.fetchall()
    data_dict = []
    for zeile in liste:
        # [print(zeile)]
        keys = ["sportart_id", "bezeichnung"]
        data_dict.append(dict(zip(keys, zeile)))
    return data_dict


async def update_sportart(sportart_id: int, db: AsyncSession, schema: schemas.SportartSchema):
    try:
        db_sportart = await db.get(database.SportartModel, sportart_id)
        if db_sportart is None:
            raise ValueError("Sportart no existe.")
        db_sportart.bezeichnung = schema.bezeichnung
        await db.commit()
        return db_sportart
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al actualizar Sportart: {e}")


async def delete_sportart(db: AsyncSession, sportart: database.SportartModel):
    try:
        await db.delete(sportart)
        await db.commit()
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al eliminar Sportart: {e}")


# SPORTSTAETTE


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
            raise ValueError(f"Error al crear Sportstaette: {e}")


async def get_sportstaetten(db: AsyncSession):
    result = await db.execute(database.SportstaetteModel.__table__.select())
    liste = result.fetchall()
    sportstaetten = await datalist_to_dict(liste)
    return sportstaetten


async def get_sportstaette_by_id(db: AsyncSession, sportstaette_id: int):
    result = await db.execute(database.SportstaetteModel.__table__.select().filter(
        database.SportstaetteModel.sportstaette_id == sportstaette_id,
    ))
    liste = result.fetchall()
    data_dict = []
    for zeile in liste:
        keys = ["sportstaette_id", "bezeichnung"]
        data_dict.append(dict(zip(keys, zeile)))
    return data_dict


async def update_sportstaette(sportstaette_id: int, db: AsyncSession, schema: schemas.SportstaetteSchema):
    try:
        db_sportstaette = await db.get(database.SportstaetteModel, sportstaette_id)
        if db_sportstaette is None:
            raise ValueError("Sportstaette no existe.")
        db_sportstaette.bezeichnung = schema.bezeichnung
        await db.commit()
        return db_sportstaette
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al actualizar Sportstaette: {e}")


async def delete_sportstaette(db: AsyncSession, sportstaette: database.SportstaetteModel):
    try:
        await db.delete(sportstaette)
        await db.commit()
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al eliminar Sportstaette: {e}")


# TEILNEHMER


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
        keys = ["teilnehmer_id", "vorname", "nachname", "email", "team_id"]
        data_dict.append(dict(zip(keys, zeile)))
    return data_dict


async def get_all_teilnehmer(db: AsyncSession):
    result = await db.execute(database.TeilnehmerModel.__table__.select())
    liste = result.fetchall()
    data_dict = []
    for zeile in liste:
        keys = ["teilnehmer_id","vorname","nachname", "email", "team_id"]
        data_dict.append(dict(zip(keys,zeile)))
    return data_dict


# TEAM


#async def create_team(db: AsyncSession, team: schemas.TeamSchema):
#    try:
#        async with db.begin():
#            db_team = database.TeamModel(**team.dict())
#            db.add(db_team)
#            await db.flush()
#            await db.refresh(db_team)
#        return db_team
#    except IntegrityError as e:
#        async with db.rollback():
#            raise ValueError(f"Error al crear team: {e}")


#async def get_team_by_id(db: AsyncSession, team_id: int):
#    try:
#        db_team = await db.get(database.TeamModel, team_id)
#        return db_team
#    except IntegrityError as e:
#        async with db.rollback():
#            raise ValueError(f"No se pudo encontrar Team: {e}")


#async def get_teams(db: AsyncSession):
#    result = await db.execute(database.TeamModel.__table__.select())
#    liste = result.fetchall()
#    teams = await datalist_to_dict(liste)
#    return teams


#async def update_team(team_id: int, team: schemas.TeamSchema, db: AsyncSession):
#    try:
#        db_team = await db.get(database.TeamModel, team_id)
#        if db_team is None:
#            raise ValueError("Team no existe.")
#        db_team.bezeichnung = team.bezeichnung
#        await db.commit()
#        return db_team
#    except IntegrityError as e:
#        async with db.rollback():
#            raise ValueError(f"Error al actualizar el equipo: {e}")


#async def delete_team(db: AsyncSession, team: database.TeamModel):
#    try:
#        await db.delete(team)
#        await db.commit()
#    except IntegrityError as e:
#        async with db.rollback():
#            raise ValueError(f"Error al eliminar el equipo: {e}")


# BEWERTUNGSART


async def create_bewertungsart(db: AsyncSession, bewertungsart: schemas.BewertungsartSchema):
    try:
        async with db.begin():
            db_bewertungsart = database.BewertungsartModel(**bewertungsart.dict())
            db.add(db_bewertungsart)
            await db.flush()
            await db.refresh(db_bewertungsart)
        return db_bewertungsart
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al crear Bewertungsart: {e}")


async def get_bewertungsart_by_id(db: AsyncSession, bewertungsart_id: int):
    try:
        db_bewertungsart = await db.get(database.BewertungsartModel, bewertungsart_id)
        return db_bewertungsart
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"No se pudo encontrar Bewertungsart: {e}")


async def get_bewertungsart(db: AsyncSession):
    result = await db.execute(database.BewertungsartModel.__table__.select())
    liste = result.fetchall()
    promise = await datalist_to_dict(liste)
    return promise


async def update_bewertungsart(bewertungsart_id: int, bewertungsart: schemas.BewertungsartSchema, db: AsyncSession):
    try:
        db_bewertungsart = await db.get(database.BewertungsartModel, bewertungsart_id)
        if db_bewertungsart is None:
            raise ValueError("El equipo no existe.")
        db_bewertungsart.bezeichnung = bewertungsart.bezeichnung
        await db.commit()
        return db_bewertungsart
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al actualizar el equipo: {e}")


async def delete_bewertungsart(db: AsyncSession, bewertungsart: database.BewertungsartModel):
    try:
        await db.delete(bewertungsart)
        await db.commit()
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al eliminar Bewertungsart: {e}")


# WETTKAMPF


async def create_wettbewerb(db: AsyncSession, wettbewerb: schemas.WettbewerbSchema):
    try:
        async with db.begin():
            db_wettbewerb = database.WettbewerbModel(**wettbewerb.dict())
            db.add(db_wettbewerb)
            await db.flush()
            await db.refresh(db_wettbewerb)
        return db_wettbewerb
    except IntegrityError as e:
        await db.rollback()
        raise ValueError(f"Error al crear Wettbewerb: {e}")


async def get_wettbewerb_by_id(db: AsyncSession, wettbewerb_id: int):
    try:
        db_wettbewerb = await db.get(database.WettbewerbModel, wettbewerb_id)
        return db_wettbewerb
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"No se pudo encontrar Wettbewerb: {e}")


async def get_wettbewerb(db: AsyncSession):
    result = await db.execute(database.WettbewerbModel.__table__.select())
    liste = result.fetchall()
    data_dict = []
    for zeile in liste:
        keys = ["wettbewerb_id", "termin", "bewertung", "sportart_id",
                "sportstaette_id", "teilnehmer_id", "bewertungsart_id", "partner_wettbewerb_id"]
        data_dict.append(dict(zip(keys, zeile)))
    return data_dict


async def update_wettbewerb(wettbewerb_id: int, wettbewerb_bewertung: int , wettbewerb: schemas.BewertungsartSchema, db: AsyncSession):
    try:
        db_wettbewerb = await db.get(database.WettbewerbModel, wettbewerb_id)
        if db_wettbewerb is None:
            raise ValueError("Wettbewerb no existe.")
        db_wettbewerb.bewertung = wettbewerb_bewertung
        await db.commit()
        return db_wettbewerb
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al actualizar Wettbewerb: {e}")


async def delete_wettbewerb(db: AsyncSession, wettbewerb: database.WettbewerbModel):
    try:
        await db.delete(wettbewerb)
        await db.commit()
    except IntegrityError as e:
        async with db.rollback():
            raise ValueError(f"Error al eliminar Wettbewerb: {e}")


async def get_top_sportart(db: AsyncSession, sportart_id: int):
    result = await db.execute(
        select(
            [database.TeilnehmerModel.teilnehmer_id, database.TeilnehmerModel.vorname,
             database.TeilnehmerModel.nachname, database.WettbewerbModel.bewertung]
        ) #spalten
        .select_from(database.TeilnehmerModel)  # Especifica la tabla de la que seleccionar
        #.join(database.WettbewerbModel,
        #      database.WettbewerbModel.teilnehmer_id == database.TeilnehmerModel.teilnehmer_id)
        .where(and_(
            database.WettbewerbModel.sportart_id == sportart_id,
            database.WettbewerbModel.teilnehmer_id == database.TeilnehmerModel.teilnehmer_id
        ))
        .order_by(desc(database.WettbewerbModel.bewertung))
    )
    top_sportart = result.fetchall()
    data_dict = []
    for zeile in top_sportart:
        [print(zeile)]
        keys = ["Startnummer", "Vorname", "Nachname", "Punkte"]
        data_dict.append(dict(zip(keys, zeile)))
    return data_dict
