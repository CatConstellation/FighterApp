from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from conexionbd import SessionLocal
from src.models.noticiamodel import create_noticia as create_noticia_db, get_noticias as get_noticias_db, get_noticia as get_noticia_db
from src.models.schemas import NoticiaCreate, NoticiaSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/noticias/", response_model=NoticiaSchema)
def create_noticia(noticia: NoticiaCreate, db: Session = Depends(get_db)):
    return create_noticia_db(db, noticia)

@router.get("/noticias/", response_model=list[NoticiaSchema])
def read_noticias(db: Session = Depends(get_db)):
    return get_noticias_db(db)

@router.get("/noticias/{noticia_id}", response_model=NoticiaSchema)
def read_publicacion(noticia_id: int, db: Session = Depends(get_db)):
    db_noticia = get_noticia_db(db, noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return db_noticia
