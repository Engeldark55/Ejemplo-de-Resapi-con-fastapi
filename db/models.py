from db.conn import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, BLOB,Float
from datetime import datetime
class Producto(Base):
    __tablename__ = "Producto"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    codigo = Column(String, unique=True)
    nombre = Column(String) 
    img = Column(BLOB)
    precio = Column(Float)
    estado = Column(Boolean)
    fecha_crecion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    