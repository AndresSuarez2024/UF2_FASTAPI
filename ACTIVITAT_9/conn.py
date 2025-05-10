import psycopg2

def connect_db():
    conn = psycopg2.connect(
        database = "",
        password = "",
        user = "",
        host = "", 
    )

    return conn