from pydantic import BaseModel

from fastapi_users.schemas import BaseUser, BaseUserUpdate, BaseUserCreate
from datetime import datetime


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
    termin: datetime
    bewertung: int
    sportart_id: int
    sportstaette_id: int
    teilnehmer_id: int
    bewertungsart_id: int
    partner_wettbewerb_id: int


class SportartSchema(BaseModel):
    bezeichnung: str


class SportstaetteSchema(BaseModel):
    bezeichnung: str


class BewertungsartSchema(BaseModel):
    bezeichnung: str


class TeilnehmerSchema(BaseModel):
    vorname: str
    nachname: str
    email: str
#    team_id: int


#class TeamSchema(BaseModel):
#    bezeichnung: str
