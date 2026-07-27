# app/server/routers/api_routers.py
from fastapi import APIRouter
from app.server.routers.auth import router as auth_router 

router = APIRouter(prefix="/api", tags=["API"])
router.include_router(auth_router)


# 3. Your other API endpoints (Forecast, etc.) EXAMPLE
@router.post("/forecast")
def get_forecast():
    return {"status": "ok", "message": "Likviditetsdata för KassaKoll"}