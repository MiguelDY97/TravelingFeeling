from fastapi import FastAPI
from database.conexion import obtener_conexion
from routers.usuarios import router as usuarios_router
from routers.destinos import router as destinos_router

app = FastAPI(
    title="TravelingFeeling API",
    version="1.0"
)
app.include_router(usuarios_router)
app.include_router(destinos_router)

@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a TravelingFeeling"
    }

@app.get("/conexion")
def probar_conexion():

    conexion = obtener_conexion()

    conexion.close()

    return {
        "estado": "Conexión exitosa con MySQL"
    }