from db.conn import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean

class Producto(Base):
    __tablename__ = "Producto"
    pass