from database import get_db_connection

# Funció per obtenir la informació de la pantalla principal
def get_informacio_principal():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM informacio_principal")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Funció per obtenir les lletres disponibles
def get_lletres_disponibles():
    lletres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ñ"]
    return lletres

# Funció per registrar un intent
def registrar_intent(id_usuario, id_paraula, lletra, encertat, errors):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO registre_joc (id_usuario, id_paraula, lletra, encertat, errors)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_usuario, id_paraula, lletra, encertat, errors))
    conn.commit()
    conn.close()

# Funció per obtenir les estadístiques d'un jugador
def get_estadistiques_jugador(id_usuario):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuaris WHERE id_usuario = %s", (id_usuario,))
    row = cursor.fetchone()
    conn.close()
    return row
