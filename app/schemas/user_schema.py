# Esquemas de entrada y salida 

from pydantic import BaseModel, EmailStr, constr
from enum import Enum

# Enum que replica los roles definidos en el modelo
class UserRole(str, Enum):
    user = "user"
    admin = "admin"

# Esquema para registrar un usuario
class UserCreate(BaseModel):
    nombre: str
    email: EmailStr
    contrasena: constr(min_length=6) #type: ingnore

# Esquema para loguear un usuario
class UserLogin(BaseModel):
    email: EmailStr
    contrasena: str

# Esquema de respuesta para retornar datos del usuario
class UserResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    rol: UserRole

    class Config:
        from_attributes = True  # Permite la conversión desde ORM (SQLAlchemy)