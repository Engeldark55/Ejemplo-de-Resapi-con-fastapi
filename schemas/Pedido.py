from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#model pedido
class Pedido(BaseModel):
    codigo:str
    id_cliente:Optional[int]
    id_producto:Optional[int]
    total:float
    metodo_pago:str
    cod_targeta:Optional[str]
    fecha_pedido:datetime=datetime.now()
    fecha_entregra:datetime
    estado:bool 