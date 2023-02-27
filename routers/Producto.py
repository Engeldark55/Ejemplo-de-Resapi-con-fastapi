#lib de router
from fastapi import APIRouter, Depends
#schemas
from schemas.producto import Schema_producto, Schema_view_client
#conexion y modelo
from db.conn import get_db
from db import models
#lib session
from sqlalchemy.orm import Session
#para el formato model_response
from typing import List

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

@router.get("/choose_product_all", response_model=List[Schema_view_client])
async def choose_product_all(db:Session = Depends(get_db)):
    product_all = db.query(models.Producto).all()
    return product_all

@router.get("/choose_product/{id}", response_model=Schema_view_client)
async def choose_one_product(id:int,db:Session = Depends(get_db)):
    product_one = db.query(models.Producto).filter(models.Producto.id == id).first()
    if not product_one:
        return {'msj': 'usuario no encontrado..'}
    return product_one

