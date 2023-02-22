from pydantic import BaseModel #lib paara crear class en modelo de un obj
from typing import Optional #tipado opc 
from datetime import datetime

#modelo Prod.
class Producto(BaseModel):
    codigo:str
    nombre:str
    img:str
    precio:float
    estado:bool
    fecha_crecion:str#este valor se define en db no aqui tomarlo en cuenta
