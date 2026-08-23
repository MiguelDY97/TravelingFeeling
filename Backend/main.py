from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.conexion import obtener_conexion
from routers.usuarios import router as usuarios_router
from routers.destinos import router as destinos_router
from routers.reservas import router as reservas_router
from routers.paquetes import router as paquetes_router
from routers.auth import router as auth_router

app = FastAPI(
    title="TravelingFeeling API",
    version="1.0"
)

origenes_permitidos = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "null" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origenes_permitidos,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(usuarios_router)
app.include_router(reservas_router)
app.include_router(destinos_router)
app.include_router(paquetes_router)

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