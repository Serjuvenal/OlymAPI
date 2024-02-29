from pydantic import BaseModel, EmailStr


class RolleSchema(BaseModel):
    bezeichnung: str


class MitarbeiterSchema(BaseModel):
    vorname: str
    nachname: str
    email: EmailStr
    username: str
    kennwort: str


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



