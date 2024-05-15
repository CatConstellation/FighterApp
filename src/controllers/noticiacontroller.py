from fastapi import APIRouter
from src.models import get_crearnoticia

router = APIRouter()

@router.get("/")
async def get_index():
    return get_crearnoticia()
