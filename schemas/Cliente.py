from pydantic import BaseModel #lib paara crear class en modelo de un obj
from typing import Optional #tipado opc 
from datetime import datetime

#model cli.
class Schema_cliente(BaseModel):
    codigo:str
    nombre:str
    fecha_n:str
    user_name:str
    correo:str
    password:str
    numero_cell:int
    domiciolio:str
    fecha_creacion:datetime=datetime.now()#no se crea aqui es en la db 