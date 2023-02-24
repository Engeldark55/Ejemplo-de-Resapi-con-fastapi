from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import setting #importar var de entorno

#variable la cual pasar a entorno 
SQLALCHEMY_DATABASE_URL = setting.URL_SQLITE
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

#fun. para la session local  y esta servira  para hacer el CRUD de la db
def get_db():
    db = session_local()    
    try:
        yield db
    finally:
        db.close()