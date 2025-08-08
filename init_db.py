# Inicialización Base de Datos

from app.models.user_model import Base
from app.db.database import engine

# Crea todas las tablas definidas en los modelos
print("⚙️ Creando tablas en la base de datos... ⚙️")
Base.metadata.create_all(bind=engine)
print("🗓️ Tablas creadas exitosamente 🗓️")