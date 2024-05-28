import sys
import os

# Agregar la ruta del directorio raíz de tu proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from sqlalchemy import Column, Integer, String, Date
from conexionbd import Base

class Noticia(Base):
    __tablename__ = 'noticias'

    id_noticia = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    cuerpo = Column(String)
    archivo = Column(String)  # Ruta del archivo
    fecha = Column(Date)