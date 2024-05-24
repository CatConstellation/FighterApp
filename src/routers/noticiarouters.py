import sys
import os
import shutil
from fastapi import HTTPException, Depends, APIRouter, UploadFile, Form
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import File

# Agregar la ruta del directorio raíz de tu proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from conexionbd import SessionLocal
from src.models.noticiamodel import create_noticia as create_noticia_db, get_noticias as get_noticias_db, get_noticia as get_noticia_db, delete_noticia as delete_noticia_db
from src.models.schemas import NoticiaCreate, NoticiaSchema
from src.models.noticia import Noticia

router = APIRouter()

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

    # Guardar el archivo en el directorio y obtener su ruta
    file_path = os.path.join(upload_folder, archivo.filename)
    with open(file_path, "wb") as file_object:
        shutil.copyfileobj(archivo.file, file_object)

    # Crear el objeto NoticiaCreate
    noticia_data = NoticiaCreate(id_noticia=id_noticia, titulo=titulo, cuerpo=cuerpo, archivo=file_path, fecha=fecha)
    return create_noticia_db(db, noticia_data, archivo)

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

