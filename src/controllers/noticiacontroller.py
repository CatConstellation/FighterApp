import sys
import os

# Agregar la ruta del directorio raíz de tu proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import APIRouter
from src.models.noticiamodel import get_crearnoticia

router = APIRouter()

@router.get("/")
async def get_index():
    return get_crearnoticia() 
