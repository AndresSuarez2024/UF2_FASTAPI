from pydantic import BaseModel

# Esquema para el Usuario
class Usuario(BaseModel):
    nombre: str

# Esquema para la Palabra
class Palabra(BaseModel):
    id_palabra: int  # Suponiendo que la tabla de palabras tenga un ID
    palabra: str

# Esquema para el Intento
class Intento(BaseModel):
    id_usuario: int
    id_palabra: int
    letra: str
    encertado: bool
    errores: int

# Esquema para la Información Principal
class Informacion(BaseModel):
    text: str  # Si el campo en la base de datos es solo un texto, esto está bien
