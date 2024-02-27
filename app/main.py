from sqlalchemy.orm import Session

from fastapi import Depends, FastAPI

from . import models, schemas
from app import crud
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

olympiapp = FastAPI()


@olympiapp.post("/teilnehmer_registrierung")
def register_teilnehmer(teilnehmer: schemas.TeilnehmerSchema, db: Session = Depends(get_db)):
    db_teilnehmer = crud.create_teilnehmer(db=db, teilnehmer=teilnehmer)
    return db_teilnehmer


@olympiapp.get("/teilnehmern")
def get_all_teilnehmer(db: Session = Depends(get_db)):
    teilnehmern = crud.get_teilnehmern(db=db)
    return teilnehmern


@olympiapp.get("/teilnehmer")
def get_teilnehmer(vorname: str, nachname:str, db: Session = Depends(get_db)):
    db_teilnehmer = crud.get_teilnehmer_by_vorname(db=db, vorname=vorname, nachname=nachname)
    return db_teilnehmer
