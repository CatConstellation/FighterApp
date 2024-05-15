from sqlalchemy.orm import Session
from .noticia import Noticia
from .schemas import NoticiaCreate
from fastapi.responses import FileResponse

def get_crearnoticia():
    return FileResponse("src/views/crearnoticia.html")

def create_noticia(db: Session, noticia: NoticiaCreate):
    db_noticia = Noticia(id_noticia=noticia.id_noticia, titulo=noticia.titulo, cuerpo=noticia.cuerpo, 
                         archivo=noticia.archivo, fecha=noticia.fecha)
    db.add(db_noticia)
    db.commit()
    db.refresh(db_noticia)
    return db_noticia

def get_noticias(db: Session):
    return db.query(Noticia).all()

def get_noticia(db: Session, noticia_id: int):
    return db.query(Noticia).filter(Noticia.id_noticia == noticia_id).first()

