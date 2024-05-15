from fastapi import APIRouter
from src.models import get_eliminarnoticia

router = APIRouter()

@router.delete("/{noticia_id}", status_code=204)
async def delete_noticia(noticia_id: int, db: Session = Depends(get_db)):
    """
    Deletes a noticia from the database by its ID.

    Args:
        noticia_id: ID of the noticia to be deleted.
        db: SQLAlchemy session object (injected through dependency).

    Raises:
        HTTPException: 404 Not Found if noticia with the given ID is not found.
    """
    success = eliminar_noticia(db, noticia_id)
    if not success:
        raise HTTPException(status_code=404, detail="Noticia no encontrada")
    return None  # No content returned on successful deletion
