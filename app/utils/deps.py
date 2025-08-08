from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user_model import User, UserRole
from app.utils.security import SECRET_KEY, ALGORITHM

# Define el esquema de autenticación: espera un token Bearer en el header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Función para obtener el usuario autenticado desde el token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        # Decodificamos el JWT usando la clave secreta y algoritmo
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")  # 'sub' es donde guardamos el email en el token
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    except JWTError:
        # Si falla la decodificación del token, devolvemos error 401
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

    # Buscamos el usuario en la base de datos
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")

    return user  

# Función para obtener el usuario actual y verificar si es admin
def get_current_admin(current_user: User = Depends(get_current_user)):
    if current_user.rol != UserRole.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permisos de administrador")
    return current_user