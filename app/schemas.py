from enum import Enum

from pydantic import BaseModel, EmailStr

from fastapi_users.schemas import BaseUser, BaseUserUpdate, BaseUserCreate

########
# USER
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


class RolleSchema(BaseModel):
    bezeichnung: str


class MitarbeiterSchema(BaseModel):
    vorname: str
    nachname: str
    email: EmailStr
    username: str
    kennwort: str
    is_active: bool


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
    team_id: int


class TeamSchema(BaseModel):
    bezeichnung: str


class Roles(Enum):
    user = "user"
    admin = "admin"


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    password: str
    is_active: bool = False
    role: Roles = "user"

    class Config:
        from_attributes = True
