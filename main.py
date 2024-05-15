import sys
import os
from fastapi import FastAPI
from src.routers.noticiarouters import router as noticia_router
from conexionbd import Base, engine
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

# Añadir el directorio raíz del proyecto a sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Incluir el router de noticias
app.include_router(noticia_router, prefix="/api/v1")

# Endpoint para servir el archivo index.html
@app.get("/")
async def get_index():
  return FileResponse("src/views/crearnoticia.html")

# Endpoint para eliminar noticias
@app.get("/eliminar-noticia/{noticia_id}")
async def eliminar_noticia_page(noticia_id: int):
  # Opcional: Pasar noticia_id al template para pre-llenar datos
  return FileResponse("src/views/eliminarnoticia.html")
