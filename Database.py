import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abhayst2580",
            database="Marble_Tiles",
            auth_plugin="mysql_native_password"
        )

        if conn.is_connected():
            return conn
        else:
            return None

    except Error as e:
        print("MySQL connection error:", e)
        return None

