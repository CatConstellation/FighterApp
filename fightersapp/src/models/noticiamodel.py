import sys
import os

# Agregar la ruta del directorio raíz de tu proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from sqlalchemy.orm import Session
from fastapi import UploadFile
from src.models.noticia import Noticia
from src.models.schemas import NoticiaCreate
from src.models.schemas import NoticiaUpdate
from fastapi.responses import FileResponse
import shutil

def save_file(file: UploadFile, destination: str):
    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return destination

def get_crearnoticia():
    return FileResponse("src/views/crearnoticia.html")

def create_noticia(db: Session, noticia: NoticiaCreate, file: UploadFile):
    file_path = save_file(file, f"static/images/{file.filename}")
    db_noticia = Noticia(id_noticia=noticia.id_noticia, titulo=noticia.titulo, cuerpo=noticia.cuerpo, 
                         archivo=file_path, fecha=noticia.fecha)
    db.add(db_noticia)
    db.commit()
    db.refresh(db_noticia)
    return db_noticia

def get_noticias(db: Session):
    return db.query(Noticia).all()

def get_noticia(db: Session, noticia_id: int):
    return db.query(Noticia).filter(Noticia.id_noticia == noticia_id).first()

def delete_noticia(db: Session, noticia_id: int):
    db.query(Noticia).filter(Noticia.id_noticia == noticia_id).delete()
    db.commit()

def update_noticia(db: Session, noticia_id: int, noticia_data: NoticiaUpdate):
    db_noticia = db.query(Noticia).filter(Noticia.id_noticia == noticia_id).first()
    if db_noticia is None:
        return None
    
    for key, value in noticia_data.dict(exclude_unset=True).items():
        setattr(db_noticia, key, value)

    db.commit()
    db.refresh(db_noticia)
    return db_noticia