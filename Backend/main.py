import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv

from database.conexion import obtener_conexion
from routers.usuarios import router as usuarios_router
from routers.destinos import router as destinos_router
from routers.reservas import router as reservas_router
from routers.paquetes import router as paquetes_router
from routers.auth import router as auth_router
from routers.alojamientos import router as alojamientos_router

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Permitir HTTP local para OAuth de Google en desarrollo
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

load_dotenv()
print("API KEY:", os.getenv("GOOGLE_MAPS_API_KEY"))

app = FastAPI(
    title="TravelingFeeling API",
    version="1.0"
)

# Middleware para manejar sesiones de manera nativa compatible con FastAPI
app.add_middleware(SessionMiddleware, secret_key="123")

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

# Inclusión de los routers de la API
app.include_router(auth_router)
app.include_router(usuarios_router)
app.include_router(reservas_router)
app.include_router(destinos_router)
app.include_router(paquetes_router)
app.include_router(alojamientos_router)

# Ruta absoluta para asegurar que siempre encuentre credentials.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLE_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, "credentials.json")

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
GOOGLE_REDIRECT_URI = "http://127.0.0.1:5000/google/callback"

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

@app.get("/google/login")
def google_login(request: Request):
    flow = Flow.from_client_secrets_file(
        GOOGLE_CLIENT_SECRETS_FILE,
        scopes=SCOPES
    )
    flow.redirect_uri = GOOGLE_REDIRECT_URI
    
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        prompt='consent'
    )
    
    # Guardamos tanto el estado como el code_verifier generado por PKCE
    request.session['state'] = state
    request.session['code_verifier'] = flow.code_verifier
    
    return RedirectResponse(url=authorization_url)

@app.get("/google/callback")
def google_callback(request: Request, error: str = None):
    if error:
        return HTMLResponse(content=f"<h1>Error de autorización de Google</h1><p><strong>Error:</strong> {error}</p>")

    state = request.session.get('state')
    code_verifier = request.session.get('code_verifier')
    
    if not state:
        return HTMLResponse(content="<h1>Error</h1><p>No se encontró el estado de OAuth en la sesión.</p><a href='/google/login'>Intentar nuevamente</a>")

    flow = Flow.from_client_secrets_file(
        GOOGLE_CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        state=state
    )
    flow.redirect_uri = GOOGLE_REDIRECT_URI
    
    # Asignamos el code_verifier que guardamos en la sesión durante el login
    flow.code_verifier = code_verifier
    
    flow.fetch_token(authorization_response=str(request.url))
    credentials = flow.credentials
    
    request.session['google_credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    
    return HTMLResponse(content="<h1>¡Google Calendar conectado!</h1><p>La autorización funcionó correctamente.</p>")

@app.get("/google/calendars")
def google_calendars(request: Request):
    credentials_data = request.session.get('google_credentials')
    if not credentials_data:
        return RedirectResponse(url='/google/login')
    
    credentials = Credentials(
        token=credentials_data['token'],
        refresh_token=credentials_data['refresh_token'],
        token_uri=credentials_data['token_uri'],
        client_id=credentials_data['client_id'],
        client_secret=credentials_data['client_secret'],
        scopes=credentials_data['scopes']
    )
    
    service = build('calendar', 'v3', credentials=credentials)
    calendars = service.calendarList().list().execute()
    return calendars

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)