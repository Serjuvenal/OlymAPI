from sqlalchemy.orm import Session

from . import models, schemas


def create_teilnehmer(db: Session, teilnehmer: schemas.TeilnehmerSchema):
    db_user = models.TeilnehmerModel(
        email=teilnehmer.email,
        vorname=teilnehmer.vorname,
        nachname=teilnehmer.nachname,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_teilnehmern(db: Session):
    return db.query(models.TeilnehmerModel).all()


def get_teilnehmer_by_vorname(db: Session, vorname: str, nachname: str):
    return (
        db.query(models.TeilnehmerModel).filter(models.TeilnehmerModel.vorname == vorname, models.TeilnehmerModel.nachname == nachname).all()
    )