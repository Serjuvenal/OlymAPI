from pydantic import BaseModel, EmailStr


class TeilnehmerSchema(BaseModel):
    vorname: str
    nachname: str
    land: str
    email: EmailStr

    class Config:
        from_attributes = True
#        orm_mode = True
