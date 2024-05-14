from sqlalchemy import Column, Integer, String, Date
from conexionbd import Base

class Noticia(Base):
    __tablename__ = 'noticias'

    id_noticia = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    cuerpo = Column(String)
    archivo = Column(String)  # Ruta de la imagen - "static/images/noticia1.jpg".
    fecha = Column(Date)
