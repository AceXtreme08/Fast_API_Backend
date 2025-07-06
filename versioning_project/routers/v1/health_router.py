from fastapi import APIRouter

router = APIRouter()

@router.get("/health", summary="Health Check API")
def health_check():
    return {"status": "running"}

