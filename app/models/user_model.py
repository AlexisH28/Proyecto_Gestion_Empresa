# Modelo de usuario SQLAlchemy

from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from sqlalchemy.ext.declarative import declarative_base
import enum

# Se define la base para los modelos
Base = declarative_base()

# Enum para restringir los roles a 'user' o 'admin'
class UserRole(enum.Enum):
    user = "user"
    admin = "admin"

# Modelo de la tabla "users" en la base de datos
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    contrasena_hash = Column(String(255), nullable=False)
    rol = Column(SqlEnum(UserRole), default=UserRole.user, nullable=False)