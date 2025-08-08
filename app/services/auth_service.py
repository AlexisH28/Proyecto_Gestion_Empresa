# Lógica del registro/login

from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.utils.security import hash_password, verify_password, create_access_token

# Función para registrar un usuario nuevo
def register_user(user_data: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado.")

    user = User(
        nombre=user_data.nombre,
        email=user_data.email,
        contrasena_hash=hash_password(user_data.contrasena)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Función para loguear un usuario y retornar un token de acceso JWT
def login_user(credentials: UserLogin, db: Session):
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not verify_password(credentials.contrasena, user.contrasena_hash):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}