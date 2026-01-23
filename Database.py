import mysql.connector
from mysql.connector import Error

conn = None
def get_connection():
    global conn
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abhayst2580",
            database="Marble_Tiles",
            auth_plugin = "mysql_native_password"
        )

        if conn.is_connected():
            return conn

    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None

def close_connection():
    if conn is not None:
        conn.close()