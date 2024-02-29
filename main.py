from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


############
# ENDPUNKTE ROLLE
############


@app.post("/rolle_einlegen")
def rolle_einlegen(rolle: schemas.RolleSchema, db: Session = Depends(get_db)):
    db_rolle = crud.create_rolle(db=db, rolle=rolle)
    return db_rolle


@app.get("/rollen")
def get_all_rollen(db: Session = Depends(get_db)):
    rollen = crud.get_rollen(db=db)
    return rollen


############
# ENDPUNKTE MITARBEITER
############


@app.post("/mitarbeiter_einlegen")
def mitarbeiter_einlegen(mitarbeiter: schemas.MitarbeiterSchema, db: Session = Depends(get_db)):
    db_mitarbeiter = crud.create_mitarbeiter(db=db, mitarbeiter=mitarbeiter)
    return db_mitarbeiter


@app.get("/mitarbeitern")
def get_all_mitarbeiter(db: Session = Depends(get_db)):
    mitarbeitern = crud.get_mitarbeiter(db=db)
    return mitarbeitern


############
# ENDPUNKTE WETBEWERB
############


@app.post("/wettbewerb_einlegen")
def wettbewerb_einlegen(wettbewerb: schemas.WettbewerbSchema, db: Session = Depends(get_db)):
    db_wettbewerb = crud.create_wettbewerb(db=db, wettbewerb=wettbewerb)
    return db_wettbewerb


@app.get("/wettbewerbe")
def get_all_wettbewerbe(db: Session = Depends(get_db)):
    db_wettbewerbe = crud.get_wettbewerbe(db=db)
    return db_wettbewerbe


############
# ENDPUNKTE SPORTART
############


@app.post("/sportart_einlegen")
def sportart_einlegen(sportart: schemas.SportartSchema, db: Session = Depends(get_db)):
    db_sportart = crud.create_sportart(db=db, sportart=sportart)
    return db_sportart


@app.get("/sportarten")
def get_all_sportarten(db: Session = Depends(get_db)):
    db_sportarten = crud.get_sportarten(db=db)
    return db_sportarten


############
# ENDPUNKTE SPORTSTAETTEN
############


@app.post("/sportstaette_einlegen")
def sportstaette_einlegen(sportstaette: schemas.SportstaetteSchema, db: Session = Depends(get_db)):
    db_sportstaette = crud.create_sportstaette(db=db, sportstaette=sportstaette)
    return db_sportstaette


@app.get("/sportstaetten")
def get_all_sportstaetten(db: Session = Depends(get_db)):
    db_sportstaetten = crud.get_sportstaetten(db=db)
    return db_sportstaetten


############
# ENDPUNKTE BEWERTUNGSART
############


@app.post("/bewertungsart_einlegen")
def bewertungsart_einlegen(bewertungsart: schemas.BewertungsartSchema, db: Session = Depends(get_db)):
    db_bewertungsart = crud.create_bewertungsart(db=db, bewertungsart=bewertungsart)
    return db_bewertungsart


@app.get("/bewertungsarten")
def get_all_bewertungsarten(db: Session = Depends(get_db)):
    db_bewertungsarten = crud.get_bewertungsarten(db=db)
    return db_bewertungsarten


############
# ENDPUNKTE TEILNEHMER
############


@app.post("/teilnehmer_registrierung")
def register_teilnehmer(teilnehmer: schemas.TeilnehmerSchema, db: Session = Depends(get_db)):
    db_teilnehmer = crud.create_teilnehmer(db=db, teilnehmer=teilnehmer)
    return db_teilnehmer


@app.get("/teilnehmern")
def get_all_teilnehmer(db: Session = Depends(get_db)):
    db_teilnehmern = crud.get_teilnehmern(db=db)
    return db_teilnehmern


@app.get("/teilnehmer")
def get_teilnehmer(vorname: str, nachname: str, db: Session = Depends(get_db)):
    db_teilnehmer = crud.get_teilnehmer_by_vorname(db=db, vorname=vorname, nachname=nachname)
    return db_teilnehmer


############
# ENDPUNKTE TEAM
############


@app.post("/team_einlegen")
def team_einlegen(team: schemas.TeamSchema, db: Session = Depends(get_db)):
    db_team = crud.create_team(db=db, team=team)
    return db_team


@app.get("/teams")
def get_all_teams(db: Session = Depends(get_db)):
    db_teams = crud.get_teams(db=db)
    return db_teams

