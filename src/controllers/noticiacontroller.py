from fastapi import APIRouter
from views.noticiaviews import show_noticias, show_create_noticia_form

router = APIRouter()

@router.get("/noticias")
async def get_noticias():
    noticias = show_noticias()
    return noticias

@router.get("/noticias/crear")
async def create_noticia_form():
    return show_create_noticia_form()

