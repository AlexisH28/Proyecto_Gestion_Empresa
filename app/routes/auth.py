# Rutas de Login y Registro

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.auth_service import register_user, login_user
from app.db.database import get_db

# Se define el router para el grupo de rutas de autenticación
router = APIRouter(prefix="/auth", tags=["auth"])

# Endpoint para registrar un usuario nuevo
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

# Endpoint para iniciar sesión y obtener un token
@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    return login_user(credentials, db)