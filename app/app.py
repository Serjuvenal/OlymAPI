from dotenv import find_dotenv, load_dotenv
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session
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
    db_sportart = await crud.create_sportart(db, sportart)
    await db.commit()
    return db_sportart


@app.get("/sportarten")
async def get_all_sportarten(db: AsyncSession = Depends(get_async_session)):
    db_sportarten = await crud.get_sportarten(db)
    return db_sportarten
