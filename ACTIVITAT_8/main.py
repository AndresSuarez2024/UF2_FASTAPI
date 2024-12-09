from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import db_connection  # Importar la función de conexión

# Crear la aplicación FastAPI
app = FastAPI()

# Modelo de datos con BaseModel
class Item(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    tax: Optional[float] = None
    stock: bool
    categoria: str

# Rutas y endpoints

@app.get("/")
def read_root():
    """Endpoint raíz"""
    return {"API en funcionamiento!"}

@app.get("/items/")
def get_items():
    """Endpoint GET para obtener todos los ítems de la tabla"""
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items;")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Endpoint GET para obtener un ítem específico"""
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE id = %s;", (item_id,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()
    if item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

@app.post("/items/")
def create_item(item: Item):
    """Endpoint POST para crear un ítem"""
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO items (nombre, descripcion, precio, tax, stock, categoria)
        VALUES (%s, %s, %s, %s, %s, %s);
        """,
        (item.nombre, item.descripcion, item.precio, item.tax, item.stock, item.categoria),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Item creado!"}

@app.get("/status")
def check_status():
    """Endpoint adicional para probar el estado del servidor"""
    return {"status": "El servidor está en funcionamiento"}