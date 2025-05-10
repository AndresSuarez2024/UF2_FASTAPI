import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",        # Asegúrate de que el host esté correcto
        user="root",             # Usuario
        password="Coco120604@",  # Contraseña
        database="penjat",  # Nombre de la base de datos
        collation="utf8mb4_general_ci"  # Colación recomendada
    )
    return connection
