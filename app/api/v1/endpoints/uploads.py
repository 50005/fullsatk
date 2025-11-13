from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid
from app.core.config import settings

router = APIRouter()


@router.post("/power-line")
async def upload_power_line_image(file: UploadFile = File(...)):
    """
    Загрузить изображение линии электропередач для анализа

    - **file**: Изображение в формате JPG, PNG или BMP (макс. 10MB)
    """
    # Проверяем расширение файла
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Неподдерживаемый формат файла. Разрешены: {settings.ALLOWED_EXTENSIONS}"
        )

    # Генерируем уникальное имя файла
    file_id = str(uuid.uuid4())
    filename = f"{file_id}{file_extension}"
    file_path = os.path.join(settings.UPLOAD_DIR, filename)

    # Сохраняем файл
    try:
        contents = await file.read()
        if len(contents) > settings.MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail="Файл слишком большой")

        with open(file_path, "wb") as f:
            f.write(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при сохранении файла: {str(e)}")

    # ЗАГЛУШКА: здесь будет вызов AI модели для анализа
    analysis_result = {
        "detected_objects": [
            {"type": "power_line", "confidence": 0.95, "bbox": [100, 50, 300, 200]},
            {"type": "transformer", "confidence": 0.87, "bbox": [400, 150, 500, 300]},
            {"type": "pole", "confidence": 0.92, "bbox": [200, 350, 250, 450]}
        ],
        "overall_condition": "good",  # good, warning, critical
        "issues_found": ["Незначительное провисание провода"],
        "recommendations": ["Плановый осмотр через 3 месяца"]
    }

    return {
        "message": "Изображение успешно загружено и обработано",
        "file_id": file_id,
        "filename": filename,
        "file_url": f"/static/uploads/{filename}",
        "analysis_result": analysis_result,
        "status": "⚠️ Заглушка - AI модель не подключена"
    }


@router.get("/{file_id}")
async def get_upload_info(file_id: str):
    """
    Получить информацию о загруженном файле
    """
    # ЗАГЛУШКА: здесь будет поиск в базе данных
    return {
        "file_id": file_id,
        "status": "processed",
        "uploaded_at": "2024-01-01T12:00:00Z",
        "analysis_result": {"detected_objects": []},
        "message": "Информация о файле (заглушка)"
    }