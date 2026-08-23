from fastapi import APIRouter
from models.login import LoginRequest
import services.auth_service as auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Autenticacion"]
)

@router.post("/login")
def login(login_data: LoginRequest):

    return auth_service.login_usuario(login_data)