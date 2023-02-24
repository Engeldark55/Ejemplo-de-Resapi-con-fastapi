from fastapi import FastAPI #lib fastapi
import uvicorn #server

#importando apis
from routers import Home
 
from db import models #importamos para crear la tablas
from db.conn import  engine #importamos db para  engine
models.Base.metadata.create_all(bind=engine) #crear tablas

app = FastAPI() #iniciando app
#inclullendo el router de las de mas api
app.include_router(Home.router)

#ejecucion del server
if __name__ == "__main__":
    uvicorn.run("main:app", port = 8000, reload = True)