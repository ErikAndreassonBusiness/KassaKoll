# Responsibility: Define API endpoints without touching app directly

# Example:
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["Forecast"])

@router.post("/auth/redirect")
def get_forecast():
    return {"status": "ok", "message": "Likviditetsdata för KassaKoll"}