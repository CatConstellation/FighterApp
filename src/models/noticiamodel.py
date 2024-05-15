from sqlalchemy.orm import Session
from .noticia import Noticia
from .schemas import NoticiaCreate
from fastapi.responses import FileResponse

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
