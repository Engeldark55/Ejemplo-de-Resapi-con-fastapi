from pydantic import BaseModel #lib paara crear class en modelo de un obj
from typing import Optional #tipado opc 
from datetime import datetime

#modelo Prod.
class Schema_producto(BaseModel):
    codigo:str
    nombre:str
    img:str
    precio:float
    estado:bool
    fecha_crecion:datetime=datetime.now()

#lo que se mostrara en fornt-end
class Schema_view_client(BaseModel):
    codigo:str
    nombre:str
    img:str
    precio:float
    class Config:
        orm_mode = True
   