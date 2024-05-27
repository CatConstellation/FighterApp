from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from conexionbd import SessionLocal
from src.models.noticiamodel import create_noticia as create_noticia_db
from src.models.noticiamodel import get_noticias as get_noticias_db, get_noticia as get_noticia_db
from src.models.noticiamodel import eliminar_noticia as eliminar_noticia_db
from src.models.schemas import NoticiaCreate, NoticiaSchema
from src.models.schemas import NoticiaUpdate


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

@router.delete("/noticias/{noticia_id}")
def delete_noticia(noticia_id: int, db: Session = Depends(get_db)):
    success = eliminar_noticia_db(db, noticia_id)
    if not success:
        raise HTTPException(status_code=404, detail="Noticia no encontrada")
    return {"message": "Noticia eliminada correctamente"}

@router.get("/noticias/", response_model=list[NoticiaSchema])
def read_noticias(db: Session = Depends(get_db)):
    return get_noticias_db(db)

@router.get("/noticias/{noticia_id}", response_model=NoticiaSchema)
def read_publicacion(noticia_id: int, db: Session = Depends(get_db)):
    db_noticia = get_noticia_db(db, noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return db_noticia

@router.put("/noticias/{noticia_id}", response_model=NoticiaSchema)
def update_noticia(noticia_id: int, noticia_data: NoticiaUpdate, db: Session = Depends(get_db)):
    updated_noticia = update_noticia(db, noticia_id, noticia_data)
    if updated_noticia:
        return updated_noticia
    raise HTTPException(status_code=404, detail="Noticia no encontrada")
