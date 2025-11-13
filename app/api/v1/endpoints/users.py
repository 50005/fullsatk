from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def get_all_users():
    """ЗАГЛУШКА: Получить всех пользователей"""
    return {
        "message": "GET /api/v1/users - Получить всех пользователей",
        "status": "⚠️ Заглушка - не реализовано",
        "action": "В будущем вернет список пользователей из БД"
    }

@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    """ЗАГЛУШКА: Получить пользователя по ID"""
    return {
        "message": f"GET /api/v1/users/{user_id} - Получить пользователя",
        "status": "⚠️ Заглушка - не реализовано",
        "user_id": user_id,
        "action": f"В будущем вернет пользователя с ID {user_id}"
    }

@router.post("/")
async def create_user():
    """ЗАГЛУШКА: Создать пользователя"""
    return {
        "message": "POST /api/v1/users - Создать пользователя",
        "status": "⚠️ Заглушка - не реализовано",
        "action": "В будущем создаст нового пользователя в БД"
    }