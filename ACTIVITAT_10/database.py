from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/penjat_db"

# Crear motor de base de datos asíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear sesión asíncrona
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos SQLAlchemy
Base = declarative_base()

# Dependencia para obtener sesión de BD
async def get_db():
    async with SessionLocal() as session:
        yield session
