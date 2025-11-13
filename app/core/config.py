import os
from typing import List


class Settings:
    """Настройки приложения для анализа ЛЭП"""
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Power Line Inspection API"

    # Настройки для загрузки файлов
    UPLOAD_DIR: str = "static/uploads"
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: List[str] = [".jpg", ".jpeg", ".png", ".bmp"]

    # На будущее: настройки для AI модели
    AI_MODEL_PATH: str = "models/power_line_detector.pth"


settings = Settings()