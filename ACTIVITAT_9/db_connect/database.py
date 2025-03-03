import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde el entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Verificar que la URL no esté vacía
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está configurada en el archivo .env")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
