from db.conn import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, BLOB,Float
from datetime import datetime
class Producto(Base):
    __tablename__ = "Producto"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    codigo = Column(String, unique=True)
    nombre = Column(String) 
    img = Column(String)
    precio = Column(Float)
    estado = Column(Boolean)
    fecha_crecion = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Cliente(Base):
    __tablename__ = "Cliente"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    codigo = Column(String, unique=True)
    nombre = Column(String) 
    fecha_n = Column(String) 
    user_name = Column(String, unique=True) 
    correo = Column(String, unique=True) 
    password = Column(String) 
    numero_cell = Column(Integer)
    domisilio = Column(String) 
    fecha_creacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)