from Database import get_connection
import pandas as pd
import numpy as np
class Debt:
    def __init__(self):
        self.__conn = get_connection()
        self.__cursor = self.__conn.cursor()

    def check(self):
        query = 'select * from Customer_debt'
        return pd.read_sql(query, self.__conn)

    def update_paid(self, cust_id):
        query = 'drop from Customer_debt where Cust_id = %s'
        self.__cursor.execute(query, (cust_id, ))

