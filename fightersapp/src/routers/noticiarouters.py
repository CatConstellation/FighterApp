from fastapi import HTTPException, Depends, APIRouter, UploadFile, Form
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import File

import sys
import os
import shutil
import uuid

# Agregar la ruta del directorio raíz de tu proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from conexionbd import SessionLocal
from src.models.noticiamodel import (
    create_noticia as create_noticia_db,
    get_noticias as get_noticias_db,
    get_noticia as get_noticia_db,
    delete_noticia as delete_noticia_db,
    update_noticia as update_noticia_db  # Asegúrate de importar la función de actualización
)
from src.models.schemas import NoticiaCreate, NoticiaSchema, NoticiaUpdate
from src.models.noticia import Noticia

router = APIRouter()

UPLOAD_DIRECTORY = "static/images/"

# Asegúrate de que el directorio de subida existe
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_next_noticia_id(db: Session) -> int:
    """Obtiene el próximo ID disponible para una nueva noticia."""
    last_noticia = db.query(Noticia).order_by(Noticia.id_noticia.desc()).first()
    if last_noticia:
        return last_noticia.id_noticia + 1
    else:
        return 1

@router.post("/noticias/", response_model=NoticiaSchema)
def create_noticia(
    titulo: str = Form(...),
    cuerpo: str = Form(...),
    fecha: str = Form(...),
    archivo: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Obtener el próximo ID disponible
    id_noticia = get_next_noticia_id(db)

    # Crear el directorio de imágenes si no existe
    upload_folder = "static/images"
    os.makedirs(upload_folder, exist_ok=True)

    # Generar un nombre único para el archivo
    filename = f"{uuid.uuid4()}_{archivo.filename}"
    file_path = os.path.join(upload_folder, filename)
    
    # Guardar el archivo en el directorio y obtener su ruta
    with open(file_path, "wb") as file_object:
        shutil.copyfileobj(archivo.file, file_object)

    # Crear el objeto NoticiaCreate
    noticia_data = NoticiaCreate(id_noticia=id_noticia, titulo=titulo, cuerpo=cuerpo, archivo=file_path, fecha=fecha)

    # Llamar a la función create_noticia_db con todos los argumentos necesarios
    return create_noticia_db(db, noticia_data, archivo.file)

@router.get("/noticias/", response_model=list[NoticiaSchema])
def read_noticias(db: Session = Depends(get_db)):
    return get_noticias_db(db)

@router.get("/noticias/{noticia_id}", response_model=NoticiaSchema)
def read_publicacion(noticia_id: int, db: Session = Depends(get_db)):
    db_noticia = get_noticia_db(db, noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return db_noticia

@router.delete("/noticias/{noticia_id}", response_model=dict)
def delete_noticia(noticia_id: int, db: Session = Depends(get_db)):
    db_noticia = get_noticia_db(db, noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    delete_noticia_db(db, noticia_id)
    return {"detail": "Noticia eliminada"}

@router.get("/noticias/buscar/", response_model=list[NoticiaSchema])
def search_noticias(query: str, db: Session = Depends(get_db)):
    noticias = db.query(Noticia).filter(Noticia.titulo.ilike(f"%{query}%")).all()
    return noticias

@router.put("/noticias/{noticia_id}", response_model=NoticiaSchema)
def update_noticia(noticia_id: int, noticia_data: NoticiaUpdate, db: Session = Depends(get_db)):
    db_noticia = get_noticia_db(db, noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Noticia no encontrada")
    updated_noticia = update_noticia_db(db, noticia_id, noticia_data)
    if updated_noticia:
        return updated_noticia
    raise HTTPException(status_code=404, detail="Noticia no encontrada")


