from sqlalchemy.orm import Session
from .noticia import Noticia
from .schemas import NoticiaDelete
from fastapi.responses import FileResponse

def get_eliminarnoticia():
    return FileResponse("src/views/eliminarnoticia.html")

def eliminar_noticia(db: Session, noticia_id: int) -> bool:
    """Deletes a noticia from the database by its ID.

    Args:
        db: SQLAlchemy session object.
        noticia_id: ID of the noticia to be deleted.

    Returns:
        True if the noticia was deleted successfully, False otherwise.
    """

    try:
        db_noticia = db.query(Noticia).filter(Noticia.id_noticia == noticia_id).first()
        if db_noticia:
            db.delete(db_noticia)
            db.commit()
            return True
        return False
    except Exception as e:
        print(f"Error deleting noticia: {e}")
        return False  # Indicate deletion failure

def get_noticias(db: Session):
    return db.query(Noticia).all()

def get_noticia(db: Session, noticia_id: int):
    return db.query(Noticia).filter(Noticia.id_noticia == noticia_id).first()
