from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user_schema import UserResponse
from app.services import user_service
from app.utils.deps import get_current_user, get_current_admin

# Creamos el router para usuarios
router = APIRouter(prefix="/users", tags=["users"])

# Endpoint para obtener la información del usuario autenticado
@router.get("/me", response_model=UserResponse)
def get_me(current_user=Depends(get_current_user)):
    return current_user

# Endpoint para obtener todos los usuarios (solo admin)
@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return user_service.get_all_users(db)

# Endpoint para eliminar un usuario por ID (solo admin)
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    user_service.delete_user_by_id(db, user_id)
    return None