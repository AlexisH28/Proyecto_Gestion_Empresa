# Funciones para JWT

from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError

# Variables para configuración del token JWT
SECRET_KEY = "2812"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto para cifrar contraseñas usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashea una contraseña usando bcrypt
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verifica que una contraseña en texto plano coincida con el hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Crea un token JWT válido por un tiempo determinado
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)