from dotenv import find_dotenv, load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, crud
from app.users import auth_backend, active_user, fastapi_users
from app.schemas import UserCreate, UserRead, UserUpdate
from app.database import User, create_db_and_tables, get_async_session

# import sendmail


load_dotenv(find_dotenv())


app = FastAPI()
app.include_router(fastapi_users.get_auth_router(auth_backend), tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(), tags=["auth"])
app.include_router(fastapi_users.get_verify_router(UserRead), tags=["auth"])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), tags=["users"], prefix="/users")


@app.get("/autheticated-route")
async def autheticated_route(user: User = Depends(active_user)):
    return {"message": f"Hallo von {user.username} mit {user.email}"}


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()


############
# ENDPUNKTE SPORTART
############


@app.post("/sportart-einlegen")
async def sportart_einlegen(sportart: schemas.SportartSchema, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.create_sportart(db, sportart)
    await db.commit()
    return promise


@app.get("/sportarten")
async def get_all_sportarten(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_sportarten(db)
    return promise


@app.post("/teilnehmer-registrieren")
async def teilnehmer_registrieren(teilnehmer: schemas.TeilnehmerSchema, db: AsyncSession = Depends(get_async_session)):
    try:
        # Crear el nuevo Teilnehmer
        teilnehmer_obj = await crud.create_teilnehmer(db, teilnehmer)
        # Commitear los cambios en la sesión de la base de datos
        await db.commit()
        return teilnehmer_obj
    except Exception as e:
        # Si ocurre algún error, hacer rollback de la transacción
        await db.rollback()
        raise e


@app.get("/teilnehmern")
async def get_all_teilnehmern(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_all_teilnehmer(db)
    return promise


@app.get("/teilnehmer-abfrage")
async def teilnehmer(vorname: str, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_teilnehmer_by_vorname(db, vorname)
    return promise


# SPORTSTAETTEN


@app.get("/sportstaetten")
async def get_sportstaetten(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_sportstaetten(db)
    return promise


@app.post("/sportstaette-anlegen")
async def sportstaette_anlegen(sportstaette: schemas.SportstaetteSchema, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.create_sportstaette(db, sportstaette)
    await db.commit()
    return promise


# TEAMS


@app.get("/teams")
async def get_teams(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_teams(db)
    return promise


@app.post("/team-anlegen")
async def team_anlegen(team: schemas.TeamSchema, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.create_team(db, team)
    await db.commit()
    return promise


@app.put("/teams/{team_id}")
async def update_team(team_id: int, team: schemas.TeamSchema, db: AsyncSession = Depends(get_async_session)):
    db_team = await crud.get_team_by_id(db, team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    updated_team = await crud.update_team(team_id, team, db)
    return updated_team


@app.delete("/teams/{team_id}")
async def delete_team(team_id: int, db: AsyncSession = Depends(get_async_session)):
    db_team = await crud.get_team_by_id(db, team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    try:
        await crud.delete_team(db, db_team)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Team deleted successfully"}