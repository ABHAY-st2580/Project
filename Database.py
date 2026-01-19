import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abhayst2580",
            database="Marble_Tiles"
        )

        if conn.is_connected():
            return conn

    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None