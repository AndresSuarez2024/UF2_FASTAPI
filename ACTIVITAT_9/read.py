import conn

def read_users():

    conn = conn.connect_db
    cursor = conn.cursor()

    sql_read_users = "SELECT * FROM users"

    cursor.execute(sql_read_users)

    users = cursor.fetchall()


    return users