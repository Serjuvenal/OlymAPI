from sqlalchemy.orm import Session

import auth
import models
import schemas

# REGION USERS


def create_user(db: Session, user: schemas.UserSchema):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.UserModel(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        role=user.role.value,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(models.UserModel).all()


def get_users_by_username(db: Session, username: str):
    return (
        db.query(models.UserModel).filter(models.UserModel.username == username).first()
    )


# REGION CREATE IN DB


def create_rolle(db: Session, rolle: schemas.RolleSchema):
    db_rolle = models.RolleModel(
        bezeichnung=rolle.bezeichnung,
    )
    db.add(db_rolle)
    db.commit()
    db.refresh(db_rolle)
    return db_rolle


def create_mitarbeiter(db: Session, mitarbeiter: schemas.MitarbeiterSchema):
    db_mitarbeiter = models.MitarbeiterModel(
        vorname=mitarbeiter.vorname,
        nachname=mitarbeiter.nachname,
        email=mitarbeiter.email,
        username=mitarbeiter.username,
        kennwort=mitarbeiter.kennwort,
    )
    db.add(db_mitarbeiter)
    db.commit()
    db.refresh(db_mitarbeiter)
    return db_mitarbeiter


def create_wettbewerb(db: Session, wettbewerb: schemas.WettbewerbSchema):
    db_wettbewerb = models.WettbewerbModel(
        bezeichnung=wettbewerb.bezeichnung,
        datum=wettbewerb.datum,
        start=wettbewerb.start,
        dauer=wettbewerb.dauer,
    )
    db.add(db_wettbewerb)
    db.commit()
    db.refresh(db_wettbewerb)
    return db_wettbewerb


def create_sportart(db: Session, sportart: schemas.SportartSchema):
    db_sportart = models.SportartModel(
        bezeichnung=sportart.bezeichnung,
    )
    db.add(db_sportart)
    db.commit()
    db.refresh(db_sportart)
    return db_sportart


def create_sportstaette(db: Session, sportstaette: schemas.SportstaetteSchema):
    db_sportstaette = models.SportstaetteModel(
        bezeichnung=sportstaette.bezeichnung,
    )
    db.add(db_sportstaette)
    db.commit()
    db.refresh(db_sportstaette)
    return db_sportstaette


def create_bewertungsart(db: Session, bewertungsart: schemas.BewertungsartSchema):
    db_bewertungsart = models.BewertungsartModel(
        bezeichnung=bewertungsart.bezeichnung,
    )
    db.add(db_bewertungsart)
    db.commit()
    db.refresh(db_bewertungsart)
    return db_bewertungsart


def create_teilnehmer(db: Session, teilnehmer: schemas.TeilnehmerSchema):
    db_teilnehmer = models.TeilnehmerModel(
        vorname=teilnehmer.vorname,
        nachname=teilnehmer.nachname,
        alter=teilnehmer.alter,
        team_id=teilnehmer.team_id,
    )
    db.add(db_teilnehmer)
    db.commit()
    db.refresh(db_teilnehmer)
    return db_teilnehmer


def create_team(db: Session, team: schemas.TeamSchema):
    db_team = models.TeamModel(
        bezeichnung=team.bezeichnung,
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


# REGION GET FROM DB


def get_rollen(db: Session):
    return db.query(models.RolleModel).all()


def get_mitarbeiter(db: Session):
    return db.query(models.MitarbeiterModel).all()


def get_wettbewerbe(db: Session):
    return db.query(models.WettbewerbModel).all()


def get_sportarten(db: Session):
    return db.query(models.SportartModel).all()


def get_sportstaetten(db: Session):
    return db.query(models.SportstaetteModel).all()


def get_bewertungsarten(db: Session):
    return db.query(models.BewertungsartModel).all()


def get_teilnehmern(db: Session):
    return db.query(models.TeilnehmerModel).all()


def get_teams(db: Session):
    return db.query(models.TeamModel).all()


def get_teilnehmer_by_vorname(db: Session, vorname: str, nachname: str):
    return (
        db.query(models.TeilnehmerModel).filter(
            models.TeilnehmerModel.vorname == vorname,
            models.TeilnehmerModel.nachname == nachname
        ).all()
    )