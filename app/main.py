from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.api import api_router
from app.core.config import settings
import os

# Создаем папку для загрузок если ее нет
os.makedirs("static/uploads", exist_ok=True)

app = FastAPI(
    title="Power Line Inspection API",
    description="API для анализа линий электропередач по фотографиям",
    version="1.0.0"
)

# Подключаем статические файлы (для доступа к загруженным изображениям)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем API роуты
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {
        "message": "🔌 Power Line Inspection API работает!",
        "description": "Система анализа ЛЭП по фотографиям"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Power Line Inspection API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)