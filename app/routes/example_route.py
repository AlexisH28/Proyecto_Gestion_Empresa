from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "¡Hola desde la ruta de ejemplo!"}
@router.get("/goodbye")
def goodbye():
    return {"message": "¡Adiós desde la ruta de ejemplo!"}