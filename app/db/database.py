# Conexión y sesión

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# URL de conexión a la base de datos MySQL
DATABASE_URL = "mysql+pymysql://gestor_user:campus2025@localhost:3306/gestor_reservas"

# Se crea el engine y la sesión para conectarse a la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función que genera la sesión de conexión y la cierra al finalizar

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Cargar variables del archivo .env
load_dotenv()

# Obtener la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

print("mysql+pymysql://gestor_user:campus2025@localhost:3306/gestor_reservas", DATABASE_URL)
print("2812", SECRET_KEY)

