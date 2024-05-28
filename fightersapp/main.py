from fastapi import FastAPI, File, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from src.routers.noticiarouters import router as noticia_router
from conexionbd import Base, engine
import uuid
import os
from fastapi.templating import Jinja2Templates

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Montar directorio estático
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2Templates
templates = Jinja2Templates(directory="src/views")

# Incluir el router de noticias
app.include_router(noticia_router, prefix="/api/v1")

# Endpoint para servir el archivo noticiaver.html
@app.get("/")
async def get_index(request: Request):
    # Aquí deberías obtener las noticias de la base de datos
    noticias = []  # Reemplaza esto con tu lógica para obtener noticias
    return templates.TemplateResponse("noticiaver.html", {"request": request, "noticias": noticias})

# Endpoint para servir el archivo crearnoticia.html
@app.get("/crearnoticia.html")
async def get_create_news():
    return FileResponse("src/views/crearnoticia.html")

# Endpoint para servir el archivo modificarnoticia.html
@app.get("/modificarnoticia.html")
async def get_modify_news():
    return FileResponse("src/views/modificarnoticia.html")

# Endpoint para servir el archivo noticiadetalle.html
@app.get("/noticiadetalle.html")
async def get_news_detail():
    return FileResponse("src/views/noticiadetalle.html")

# Endpoint para manejar la subida de archivos
@app.post("/api/v1/noticias/")
async def create_noticia(titulo: str, cuerpo: str, fecha: str, archivo: UploadFile = File(...)):
    # Guarda el archivo
    upload_folder = "static/images"
    os.makedirs(upload_folder, exist_ok=True)
    filename = f"{uuid.uuid4()}_{archivo.filename}"
    file_location = os.path.join(upload_folder, filename)
    
    with open(file_location, "wb") as file:
        file.write(archivo.file.read())

    return {"titulo": titulo, "cuerpo": cuerpo, "fecha": fecha, "archivo": f"/static/images/{filename}"}

# Endpoint para mostrar los detalles de una noticia
@app.get("/noticia/{noticia_id}")
async def get_noticia_detalle(request: Request, noticia_id: int):
    # Aquí deberías obtener la noticia de la base de datos usando noticia_id
    noticia = {}  # Reemplaza esto con tu lógica para obtener una noticia específica
    return templates.TemplateResponse("noticiadetalle.html", {"request": request, "noticia": noticia})
