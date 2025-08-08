# MAIN PRODUCTION

from fastapi import FastAPI
from app.routes import auth  # Importamos el router de autenticación

# Creamos la instancia de la app
app = FastAPI(title="Gestor de Reservas de Salas")

# Registramos las rutas de autenticación
app.include_router(auth.router)

# Mensaje de prueba en la raíz
@app.get("/")
def root():
    return {"message": "📃 Bienvenido a la API de Gestión de Reservas de Salas de Coworking 📃"}