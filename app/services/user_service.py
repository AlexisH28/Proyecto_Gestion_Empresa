from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user_model import User

# Buscar un usuario por su ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Obtener la lista completa de usuarios
def get_all_users(db: Session):
    return db.query(User).all()

# Eliminar un usuario por su ID
def delete_user_by_id(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return True