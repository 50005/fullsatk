from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# Временное хранилище (позже заменим на базу данных)
processing_history = []


@router.get("/")
async def get_processing_history(limit: int = 10, offset: int = 0):
    """
    Получить историю обработки изображений пользователя

    - **limit**: Количество записей (по умолчанию 10)
    - **offset**: Смещение для пагинации
    """
    # ЗАГЛУШКА: здесь будет фильтрация по пользователю и пагинация
    user_history = processing_history[offset:offset + limit]

    return {
        "history": user_history,
        "total": len(processing_history),
        "limit": limit,
        "offset": offset,
        "message": "История обработки (заглушка)"
    }


@router.get("/{processing_id}")
async def get_processing_details(processing_id: str):
    """
    Получить детали конкретной обработки

    - **processing_id**: ID обработки
    """
    # ЗАГЛУШКА: поиск в базе данных
    processing_entry = next(
        (item for item in processing_history if item["id"] == processing_id),
        None
    )

    if not processing_entry:
        raise HTTPException(status_code=404, detail="Обработка не найдена")

    return {
        "processing_entry": processing_entry,
        "message": "Детали обработки (заглушка)"
    }


@router.delete("/{processing_id}")
async def delete_processing_entry(processing_id: str):
    """
    Удалить запись из истории обработки

    - **processing_id**: ID обработки для удаления
    """
    # ЗАГЛУШКА: удаление из базы данных
    global processing_history
    processing_history = [item for item in processing_history if item["id"] != processing_id]

    return {
        "message": f"Запись {processing_id} удалена из истории",
        "status": "⚠️ Заглушка - удаление из временного хранилища"
    }