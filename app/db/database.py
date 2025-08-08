# Conexión y sesión

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos MySQL (modificar con tus credenciales)
DATABASE_URL = "mysql+pymysql://usuario:password@localhost:3306/gestor_reservas"

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
