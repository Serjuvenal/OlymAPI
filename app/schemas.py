from pydantic import BaseModel, EmailStr

from fastapi_users.schemas import BaseUser, BaseUserUpdate, BaseUserCreate

########
# USER AUTHENTIFIZIERUNG
########


class UserRead(BaseUser):
    username: str
    pass


class UserCreate(BaseUserCreate):
    username: str
    pass


class UserUpdate(BaseUserUpdate):
    username: str
    pass


########
# REST ENTITAETEN
########


class WettbewerbSchema(BaseModel):
    bezeichnung: str
    datum: str
    start: str
    dauer: int


class SportartSchema(BaseModel):
    bezeichnung: str


class SportstaetteSchema(BaseModel):
    bezeichnung: str


class BewertungsartSchema(BaseModel):
    bezeichnung: str


class TeilnehmerSchema(BaseModel):
    vorname: str
    nachname: str
    alter: str
    startnummer: str
    team_id: int


class TeamSchema(BaseModel):
    bezeichnung: str
