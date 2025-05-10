import mysql.connector
from mysql.connector import Error

DB = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Coco120604@',
    'database': 'db_fastapi',
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci',
}

def db_connection():
    try:
        connection = mysql.connector.connect(**DB)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectarse a la base de datos: {e}")
        raise

def close_db_connection(connection):
    if connection.is_connected():
        connection.close()