# MAIN PRODUCTION
# Registro de todos los routers

from fastapi import FastAPI
from app.routes import auth, users  # Importamos los routers de auth y users

# Creamos la instancia de la app
app = FastAPI(title="🗂️ Gestor de Reservas de Salas 🗂️")

# Registramos los routers en la app
app.include_router(auth.router) # Módulo Autenticación
app.include_router(users.router) # Módulo Usuarios

# Mensaje de prueba en la raíz
@app.get("/")
def root():
    return {"message": "📃 Bienvenido a la API de Gestión de Reservas de Salas de Coworking 📃"}