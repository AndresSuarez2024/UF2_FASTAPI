from database import get_db_connection

# CRUD para la tabla Usuarios
def create_usuario(nombre: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuaris (nom, punts_actuals, partides_totals, partides_guanyades, partida_mes_punts)
        VALUES (%s, %s, %s, %s, %s)
    """, (nombre, 0, 0, 0, 0))  # 'nom' en vez de 'nombre' para coincidir con la base de datos
    conn.commit()
    conn.close()

def get_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuaris")  # La tabla se llama 'usuaris'
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_usuario(id_usuario: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuaris WHERE id_usuario = %s", (id_usuario,))  # 'usuaris' en vez de 'usuarios'
    row = cursor.fetchone()
    conn.close()
    return row

def update_usuario(id_usuario: int, nombre: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuaris SET nom = %s WHERE id_usuario = %s", (nombre, id_usuario))  # 'nom' en vez de 'nombre'
    conn.commit()
    conn.close()

def delete_usuario(id_usuario: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuaris WHERE id_usuario = %s", (id_usuario,))  # 'usuaris' en vez de 'usuarios'
    conn.commit()
    conn.close()

# CRUD para la tabla Palabras
def get_palabras():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM paraules")  # La tabla se llama 'paraules'
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_palabra(id_palabra: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM paraules WHERE id_palabra = %s", (id_palabra,))  # 'paraules' en vez de 'palabras'
    row = cursor.fetchone()
    conn.close()
    return row

# CRUD para la tabla Registro de Juego
def registrar_intento(id_usuario: int, id_palabra: int, letra: str, encertado: bool, errores: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO registre_joc (id_usuario, id_paraula, lletra, encertat, errors)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_usuario, id_palabra, letra, encertado, errores))  # 'registre_joc' y 'id_paraula' en vez de 'registro_juego' e 'id_palabra'
    conn.commit()
    conn.close()

def get_registro_juego(id_usuario: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registre_joc WHERE id_usuario = %s", (id_usuario,))  # 'registre_joc' en vez de 'registro_juego'
    rows = cursor.fetchall()
    conn.close()
    return rows

# CRUD para la tabla Información Principal
def get_informacion_principal():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM informacio_principal")  # 'informacio_principal' es el nombre correcto
    rows = cursor.fetchall()
    conn.close()
    return rows
