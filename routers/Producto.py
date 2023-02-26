#lib de router
from fastapi import APIRouter, Depends
from schemas.producto import Schema_producto
#conexion y modelo
from db.conn import get_db
from db import models
#lib session
from sqlalchemy.orm import Session

#crear router
router = APIRouter(
    prefix="/Producto",#nombre de identificacion de api o url
    tags=["Productos"]#nombre para el docs url
)

@router.get("/")
async def Producto():
    return "index"

@router.post("/create_Product")
async def create_product(producto:Schema_producto, db:Session = Depends(get_db)):
    #convertir el schema a un diccionario
    dic_prod = producto.dict()
    #igualando los valores de modelo y schemas
    modelo_producto = models.Producto(
        codigo = dic_prod['codigo'],
        nombre= dic_prod['nombre'],
        img= dic_prod['img'],
        precio= dic_prod['precio'],
        estado= dic_prod['estado']
    )
    #guardar ala db
    db.add(modelo_producto)
    db.commit()
    #una vez guardados refrecaremos la db
    db.refresh(modelo_producto)
    return 'Producto guardado con exito'
    