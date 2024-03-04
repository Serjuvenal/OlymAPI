from dotenv import find_dotenv, load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import auth
import crud
import models
import schemas
# import sendmail
from database import engine, get_db

load_dotenv(find_dotenv())

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


############
# ENDPUNKTE USER
############


@app.post("/register-user")
def register_user(mitarbeiter: schemas.MitarbeiterSchema, db: Session = Depends(get_db)):
    db_mitarbeiter = crud.create_mitarbeiter(db=db, mitarbeiter=mitarbeiter)
    token = auth.create_access_token(db_mitarbeiter)
    return db_mitarbeiter, token


@app.get("/mitarbeiter-verifizierung/{token}", response_class=HTMLResponse)
def login_user(token: str, db: Session = Depends(get_db)):
    payload = auth.verify_token(token)
    username = payload.get("sub")
    db_user = crud.get_users_by_username(db, username)
    db_user.is_active = True
    db.commit()
    return f"""
    <html>
        <head>
            <title>Ihres Konto: {username}, ist jetzt aktiv.</title>
        </head>
        <body>
            <h2><a href="http://olymp.internal">
                Zurück zur Startseite.
            </a></h2>
        </body>
    </html>
    """


@app.post("/login-mitarbeiter")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    db_user = crud.get_users_by_username(db=db, username=form_data.username)
    if not db_user:
        raise HTTPException(
            status_code=401, detail="Anmeldeinformationen nicht korrekt"
        )
    if auth.verify_password(form_data.password, db_user.hashed_password):
        token = auth.create_access_token(db_user)
        return {"access_token": token, "token_Type": "bearer"}
    raise HTTPException(status_code=401, detail="Anmeldeinformationen nicht korrekt")


@app.get("/users", dependencies=[Depends(auth.check_active)])
def get_all_users(db: Session = Depends(get_db)):
    users = crud.get_users(db=db)
    return users


############
# ENDPUNKTE ROLLE
############


@app.post("/rolle-einlegen", dependencies=[Depends(auth.check_active)])
def rolle_einlegen(rolle: schemas.RolleSchema, db: Session = Depends(get_db)):
    db_rolle = crud.create_rolle(db=db, rolle=rolle)
    return db_rolle


@app.get("/rollen", dependencies=[Depends(auth.check_active)])
def get_all_rollen(db: Session = Depends(get_db)):
    rollen = crud.get_rollen(db=db)
    return rollen


############
# ENDPUNKTE MITARBEITER
############


@app.post("/mitarbeiter-einlegen", dependencies=[Depends(auth.check_active)])
def mitarbeiter_einlegen(mitarbeiter: schemas.MitarbeiterSchema, db: Session = Depends(get_db)):
    db_mitarbeiter = crud.create_mitarbeiter(db=db, mitarbeiter=mitarbeiter)
    token = auth.create_access_token(db_mitarbeiter)
#    sendmail.send_mail(to=db_mitarbeiter.email, token=token, username=db_mitarbeiter.username)
    return db_mitarbeiter, token


@app.get("/mitarbeitern", dependencies=[Depends(auth.check_active)])
def get_all_mitarbeiter(db: Session = Depends(get_db)):
    mitarbeitern = crud.get_mitarbeiter(db=db)
    return mitarbeitern


############
# ENDPUNKTE WETBEWERB
############


@app.post("/wettbewerb-einlegen", dependencies=[Depends(auth.check_active)])
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


@app.post("/sportart-einlegen", dependencies=[Depends(auth.check_active)])
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


@app.post("/sportstaette-einlegen", dependencies=[Depends(auth.check_active)])
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


@app.post("/bewertungsart-einlegen", dependencies=[Depends(auth.check_active)])
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


@app.post("/teilnehmer-registrierung", dependencies=[Depends(auth.check_active)])
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


@app.post("/team-einlegen", dependencies=[Depends(auth.check_active)])
def team_einlegen(team: schemas.TeamSchema, db: Session = Depends(get_db)):
    db_team = crud.create_team(db=db, team=team)
    return db_team


@app.get("/teams")
def get_all_teams(db: Session = Depends(get_db)):
    db_teams = crud.get_teams(db=db)
    return db_teams
