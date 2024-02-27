from pydantic import BaseModel, EmailStr


class TeilnehmerSchema(BaseModel):
    email: EmailStr
    vorname: str
    nachname: str

    class Config:
        from_attributes = True
#        orm_mode = True
