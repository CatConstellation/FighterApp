from sqlalchemy.orm import Session
from .noticia import Noticia
from .schemas import NoticiaCreate
from fastapi.responses import FileResponse
from .schemas import NoticiaUpdate
from models import Noticia
from sqlalchemy.orm import Session

def get_crearnoticia():
    return FileResponse("src/views/crearnoticia.html")

def create_noticia(db: Session, noticia: NoticiaCreate):
    db_noticia = Noticia(id_noticia=noticia.id_noticia, titulo=noticia.titulo, cuerpo=noticia.cuerpo, 
                         archivo=noticia.archivo, fecha=noticia.fecha)
    db.add(db_noticia)
    db.commit()
    db.refresh(db_noticia)
    return db_noticia

def get_eliminarnoticia():
    return FileResponse("src/views/eliminarnoticia.html")

def eliminar_noticia(db: Session, noticia_id: int):
    db_noticia = db.query(Noticia).filter(Noticia.id_noticia == noticia_id).first()
    if db_noticia:
        db.delete(db_noticia)
        db.commit()
        return True
    return False

def get_noticias(db: Session):
    return db.query(Noticia).all()

def get_noticia(db: Session, noticia_id: int):
    return db.query(Noticia).filter(Noticia.id_noticia == noticia_id).first()

def update_noticia(db: Session, noticia_id: int, noticia_data: NoticiaUpdate):
    db_noticia = db.query(Noticia).filter(Noticia.id_noticia == noticia_id).first()
    if db_noticia is None:
        return None
    
    for key, value in noticia_data.dict(exclude_unset=True).items():
        setattr(db_noticia, key, value)

    db.commit()
    db.refresh(db_noticia)
    return db_noticia

