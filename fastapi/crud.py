from sqlalchemy.orm import Session

import models
import schemas


def create_teilnehmer(db: Session, teilnehmer: schemas.TeilnehmerSchema):
    db_teilnehmer = models.TeilnehmerModel(
        vorname=teilnehmer.vorname,
        nachname=teilnehmer.nachname,
        email=teilnehmer.email,
        land=teilnehmer.land,
    )
    db.add(db_teilnehmer)
    db.commit()
    db.refresh(db_teilnehmer)
    return db_teilnehmer


def get_teilnehmern(db: Session):
    return db.query(models.TeilnehmerModel).all()


def get_teilnehmer_by_vorname(db: Session, vorname: str, nachname: str):
    return (
        db.query(models.TeilnehmerModel).filter(models.TeilnehmerModel.vorname == vorname, models.TeilnehmerModel.nachname == nachname).all()
    )