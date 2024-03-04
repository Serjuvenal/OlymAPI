import datetime

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext

from fastapi import Depends, HTTPException, status

JWT_SECRET = "OlymAPI"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(user):
    try:
        claims = {
            "sub": user.username,
            "email": user.email,
            "role": user.role.value,
            "active": user.is_active,
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=30),
        }
        return jwt.encode(claims=claims, key=JWT_SECRET, algorithm=ALGORITHM)
    except Exception as ex:
        print(str(ex))
        raise ex


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_token(token):
    try:
        payload = jwt.decode(token, key=JWT_SECRET)
        return payload
    except:
        raise Exception("Der Token ist fehlerhaft!")


def check_active(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    active = payload.get("active")
    if not active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Fehler, Konto ist nicht aktiv",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        return payload


def check_admin(payload: dict = Depends(check_active)):
    role = payload.get("role")
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Zugriff nur für autorisierte Benutzer.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        return payload
