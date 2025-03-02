import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        # Estableix la connexió amb la base de dades
        connection = mysql.connector.connect(
            host="localhost",  # Asegura't que el host sigui correcte
            user="root",  # El teu usuari
            password="Coco120604@",  # La teva contrasenya
            database="penjat",  # Nom de la base de dades
            collation="utf8mb4_general_ci"  # Collation recomanat per a caràcters especials
        )
        if connection.is_connected():
            print("Connexió exitosa a la base de dades")
            return connection
    except Error as e:
        print(f"Error en la connexió a la base de dades: {e}")
        return None
