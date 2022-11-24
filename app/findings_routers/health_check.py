from fastapi import APIRouter
router = APIRouter()

@router.get("/api/health/", tags=["health"],description="This will running status of the service.")
async def get_health():
    return "running"