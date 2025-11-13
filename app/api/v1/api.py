from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, uploads, history

api_router = APIRouter()

# Подключаем эндпоинты
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(uploads.router, prefix="/uploads", tags=["file-uploads"])
api_router.include_router(history.router, prefix="/history", tags=["processing-history"])