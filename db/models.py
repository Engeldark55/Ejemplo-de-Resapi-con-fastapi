from db.conn import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, BLOB,Float
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    codigo = Column(String, unique=True)
    nombre = Column(String) 
    img = Column(String)
    precio = Column(Float)
    estado = Column(Boolean)
    fecha_crecion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    pedido = relationship("Pedido", backref="producto", cascade="delete,merge")
class Cliente(Base):
    __tablename__ = "cliente"
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
    pedido = relationship("Pedido", backref="cliente", cascade="delete,merge")

class Pedido(Base):
    __tablename__ = "pedido"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    folio = Column(String, unique=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id", ondelete="CASCADE"))
    id_producto = Column(Integer, ForeignKey("producto.id", ondelete="CASCADE"))
    total_pagar = Column(Integer)
    estado = Column(String)
    fecha_creacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)