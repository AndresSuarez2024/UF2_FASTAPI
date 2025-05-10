from fastapi import FastAPI, HTTPException
from models import create_usuario, get_usuarios, get_usuario, update_usuario, delete_usuario
from models import get_palabras, get_palabra, registrar_intento, get_registro_juego
from models import get_informacion_principal
from schemas import Informacion, Usuario, Palabra, Intento

app = FastAPI()

# Endpoints para la tabla Usuarios
@app.post("/api/usuarios")
async def crear_usuario_endpoint(usuario: Usuario):
    # Creamos el usuario en la base de datos
    create_usuario(usuario.nombre)
    return {"message": "Usuario creado correctamente"}

@app.get("/api/usuarios")
async def obtener_usuarios():
    # Obtenemos todos los usuarios de la base de datos
    usuarios = get_usuarios()
    return {"usuarios": usuarios}

@app.get("/api/usuarios/{id_usuario}")
async def obtener_usuario(id_usuario: int):
    usuario = get_usuario(id_usuario)
    if usuario:
        return {"usuario": usuario}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.put("/api/usuarios/{id_usuario}")
async def actualizar_usuario(id_usuario: int, usuario: Usuario):
    # Actualizamos el nombre del usuario en la base de datos
    update_usuario(id_usuario, usuario.nombre)
    return {"message": "Usuario actualizado correctamente"}

@app.delete("/api/usuarios/{id_usuario}")
async def eliminar_usuario(id_usuario: int):
    # Eliminamos el usuario de la base de datos
    delete_usuario(id_usuario)
    return {"message": "Usuario eliminado correctamente"}

# Endpoints para la tabla Palabras
@app.get("/api/palabras")
async def obtener_palabras():
    # Obtenemos todas las palabras de la base de datos
    palabras = get_palabras()
    return {"palabras": palabras}

@app.get("/api/palabras/{id_palabra}")
async def obtener_palabra(id_palabra: int):
    palabra = get_palabra(id_palabra)
    if palabra:
        return {"palabra": palabra}
    else:
        raise HTTPException(status_code=404, detail="Palabra no encontrada")

# Endpoints para la tabla Registro de Juego
@app.post("/api/registro_juego")
async def registrar_intento_endpoint(intent: Intento):
    # Registramos un intento en la base de datos
    registrar_intento(intent.id_usuario, intent.id_palabra, intent.letra, intent.encertado, intent.errores)
    return {"message": "Intento registrado correctamente"}

@app.get("/api/registro_juego/{id_usuario}")
async def obtener_registro_juego(id_usuario: int):
    # Obtenemos los registros del usuario
    registros = get_registro_juego(id_usuario)
    return {"registros": registros}

# Endpoints para la Información Principal
@app.get("/api/informacion_principal")
async def obtener_informacion_principal():
    # Obtenemos la información principal de la base de datos
    info = get_informacion_principal()
    return {"informacion": info}
