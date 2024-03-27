from dotenv import find_dotenv, load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, crud
from app.users import auth_backend, active_user, fastapi_users
from app.schemas import UserCreate, UserRead, UserUpdate
from app.database import User, create_db_and_tables, get_async_session
from fastapi.middleware.cors import CORSMiddleware

# import sendmail


load_dotenv(find_dotenv())


app = FastAPI()
app.include_router(fastapi_users.get_auth_router(auth_backend), tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(), tags=["auth"])
app.include_router(fastapi_users.get_verify_router(UserRead), tags=["auth"])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), tags=["users"], prefix="/users")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)


@app.get("/autheticated-route")
async def autheticated_route(user: User = Depends(active_user)):
    return {"message": f"Hallo von {user.username} mit {user.email}"}


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()


#                               SPORTART


@app.post("/sportart-anlegen")
async def sportart_anlegen(schema: schemas.SportartSchema, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.create_sportart(db, schema)
    await db.commit()
    return promise


@app.get("/get-all-sportarten")
async def get_all_sportarten(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_sportarten(db)
    return promise


@app.get("/get-sportart/{sportart_id}")
async def sportart(sportart_id: int, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_sportart_by_id(db, sportart_id)
    return promise


@app.put("/update-sportart/{sportart_id}")
async def update_sportart(
        sportart_id: int, schema: schemas.SportartSchema, db: AsyncSession = Depends(get_async_session)
):
    db_sportart = await crud.get_sportart_by_id(db, sportart_id)
    if db_sportart is None:
        raise HTTPException(status_code=404, detail="Sportstaette nicht gefunden!")
    updated_sportart = await crud.update_sportart(sportart_id, db, schema)
    return updated_sportart


@app.delete("/delete-sportart-id/{sportart_id}")
async def delete_sportart_id(sportart_id: int, db: AsyncSession = Depends(get_async_session)):
    db_sportart = await crud.get_sportart_by_id(db, sportart_id)
    if db_sportart is None:
        raise HTTPException(status_code=404, detail="Sportart nicht gefunden!")
    try:
        await crud.delete_sportart(db, db_sportart)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Sportart erfolgreich entfernt!"}


#                               TEILNEHMER


@app.post("/teilnehmer-registrieren")
async def teilnehmer_registrieren(schema: schemas.TeilnehmerSchema, db: AsyncSession = Depends(get_async_session)):
    try:
        teilnehmer_obj = await crud.create_teilnehmer(db, schema)
        await db.commit()
        return teilnehmer_obj
    except Exception as e:
        await db.rollback()
        raise e


@app.get("/get-teilnehmern")
async def get_teilnehmern(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_all_teilnehmer(db)
    return promise


@app.get("/get-teilnehmer/{vorname}")
async def teilnehmer(vorname: str, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_teilnehmer_by_vorname(db, vorname)
    return promise


#                               SPORTSTAETTEN


@app.get("/get-all-sportstaetten")
async def get_all_sportstaetten(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_sportstaetten(db)
    return promise


@app.post("/sportstaette-anlegen")
async def sportstaette_anlegen(schema: schemas.SportstaetteSchema, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.create_sportstaette(db, schema)
    await db.commit()
    return promise


@app.put("/update-sportstaette/{sportstaette_id}")
async def update_sportstaette(
        sportstaette_id: int, schema: schemas.SportstaetteSchema, db: AsyncSession = Depends(get_async_session)
):
    db_sportstaette = await crud.get_sportstaette_by_id(db, sportstaette_id)
    if db_sportstaette is None:
        raise HTTPException(status_code=404, detail="Sportstaette nicht gefunden!")
    updated_sportstaette = await crud.update_sportstaette(sportstaette_id, db, schema)
    return updated_sportstaette


@app.delete("/delete-sportstaette/{sportstaette_id}")
async def delete_sportstaette(sportstaette_id: int, db: AsyncSession = Depends(get_async_session)):
    db_sportstaette = await crud.get_sportstaette_by_id(db, sportstaette_id)
    if db_sportstaette is None:
        raise HTTPException(status_code=404, detail="Sportaette nicht gefunden!")
    try:
        await crud.delete_sportstaette(db, db_sportstaette)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Sportstaette erfolgreich entfernt!"}


#                       BEWERTUNGSART


@app.post("/bewertungsart-anlegen")
async def bewertungsart_anlegen(schema: schemas.BewertungsartSchema, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.create_bewertungsart(db, schema)
    await db.commit()
    return promise


@app.get("/get-bewertungsart/{bewertungsart_id}")
async def bewertungsart(bewertungsart_id: int, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_bewertungsart_by_id(db, bewertungsart_id)
    return promise


@app.get("/get-all-bewertungsart")
async def get_all_bewertungsart(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_bewertungsart(db)
    return promise


@app.put("/update-bewertungsart/{bewertungsart_id}")
async def update_bewertungsart(bewertungsart_id: int, schema: schemas.BewertungsartSchema, db: AsyncSession = Depends(get_async_session)):
    db_bewertungsart = await crud.get_bewertungsart_by_id(db, bewertungsart_id)
    if db_bewertungsart is None:
        raise HTTPException(status_code=404, detail="Bewertungsart nicht gefunden!")
    updated_bewertungsart = await crud.update_bewertungsart(bewertungsart_id, schema, db)
    return updated_bewertungsart


@app.delete("/delete-bewertungsart/{bewertungsart_id}")
async def delete_bewertungsart(bewertungsart_id: int, db: AsyncSession = Depends(get_async_session)):
    db_bewertungsart = await crud.get_bewertungsart_by_id(db, bewertungsart_id)
    if db_bewertungsart is None:
        raise HTTPException(status_code=404, detail="Team nicht gefunden!")
    try:
        await crud.delete_bewertungsart(db, db_bewertungsart)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Bewertungsart erfolgreich entfernt"}


#                       WETTBEWERB


@app.post("/wettbewerb-anlegen")
async def wettbewerb_anlegen(schema: schemas.WettbewerbSchema, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.create_wettbewerb(db, schema)
    await db.commit()
    return promise


@app.get("/get-wettbewerb/{wettbewerb_id}")
async def bewertungsart(wettbewerb_id: int, db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_wettbewerb_by_id(db, wettbewerb_id)
    return promise


@app.get("/get-all-wettbewerb")
async def get_all_wettbewerb(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_wettbewerb(db)
    return promise


@app.put("/ergibniss-eingeben/{bewertung}")
async def ergibniss_eingeben(
        wettbewerb_id: int, bewertung: int, db: AsyncSession = Depends(get_async_session)
):
    db_wettbewerb = await crud.get_wettbewerb_by_id(db, wettbewerb_id)
    if db_wettbewerb is None:
        raise HTTPException(status_code=404, detail="Wettbewerb nicht gefunden!")
    updated_wettbewerb = await crud.update_bewertung_in_wettbewerb(wettbewerb_id, bewertung, db,)
    return updated_wettbewerb


@app.put("/update-partner-wettbewerb/{partner_wettbewerb_id}")
async def update_wettbewerb_partner_id(
        wettbewerb_id: int, partner_wettbewerb_id: int, db: AsyncSession = Depends(get_async_session)
):
    db_wettbewerb = await crud.get_wettbewerb_by_id(db, wettbewerb_id)
    if db_wettbewerb is None:
        raise HTTPException(status_code=404, detail="Wettbewerb nicht gefunden!")
    updated_wettbewerb = await crud.update_partner_in_wettbewerb(wettbewerb_id, partner_wettbewerb_id, db,)
    return updated_wettbewerb


@app.delete("/delete-wettbewerb/{wettbewerb_id}")
async def delete_wettbewerb(wettbewerb_id: int, db: AsyncSession = Depends(get_async_session)):
    db_wettbewerb = await crud.get_wettbewerb_by_id(db, wettbewerb_id)
    if db_wettbewerb is None:
        raise HTTPException(status_code=404, detail="Wettbewerb nicht gefunden!")
    try:
        await crud.delete_wettbewerb(db, db_wettbewerb)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Bewertungsart erfolgreich entfernt"}


# FORMS

@app.get("/get-top-disziplin/{sportart_id}")
async def get_top_disziplin(sportart_id: int, spiel: str, db: AsyncSession = Depends(get_async_session)):
    if spiel == "qualifizierung":
        promise = await crud.get_top_sportart_qualifizierung(db, sportart_id)
    elif spiel == "finale":
        promise = await crud.get_top_sportart_finale(db, sportart_id)
    return promise


@app.get("/get-all-termine")
async def get_all_termine(db: AsyncSession = Depends(get_async_session)):
    promise = await crud.get_termine(db)
    return promise