from Database import get_connection
import pandas as pd

def get_data():
    conn = get_connection()

    query = ''