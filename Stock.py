from Database import get_connection

import pandas as pd

class _12_18_:

    def __init__(self):
        self.__conn = get_connection()
        self.__cursor = self.__conn.cursor()

    def check(self):
        query = 'select * from _12_18_'
        return pd.read_sql(query, self.__conn)

    def new_design(self, design_number, hl_qty, l_qty, d_qty, f_qty):
        query = 'insert into _12_18_ (Tile_number, HL_qty, L_qty, D_qty, F_qty) values (%s, %s, %s, %s, %s)'
        self.__cursor.execute(query, (design_number, hl_qty, l_qty, d_qty, f_qty))
        self.__conn.commit()

    def remove_design(self, design_number):
        query = 'drop from _12_18_ where Tile_number = %s'
        self.__cursor.execute(query, (design_number,))


class _2_4_:

    def __init__(self):
        self.__conn = get_connection()
        self.__cursor = self.__conn.cursor()

    def check(self):
        query = 'select * from _2_4_'
        return pd.read_sql(query, self.__conn)

    def new_design(self, design_name, qty):
        query = 'insert into _2_4_ (Tile_name, Qty) values (%s, %s)'
        self.__cursor.execute(query, (design_name, qty))
        self.__conn.commit()

    def remove_design(self, design_name):
        query = 'drop from _2_4_ where Tile_name = %s'
        self.__cursor.execute(query, (design_name,))


class _2_2_:

    def __init__(self):
        self.__conn = get_connection()
        self.__cursor = self.__conn.cursor()

    def check(self):
        query = 'select * from _2_2_'
        return pd.read_sql(query, self.__conn)

    def new_design(self, design_name, qty):
        query = 'insert into _2_2_ (Tile_name, Qty) values (%s, %s)'
        self.__cursor.execute(query, (design_name, qty))
        self.__conn.commit()

    def remove_design(self, design_name):
        query = 'drop from _2_2_ where Tile_name = %s'
        self.__cursor.execute(query, (design_name,))


class _1_2_:

    def __init__(self):
        self.__conn = get_connection()
        self.__cursor = self.__conn.cursor()

    def check(self):
        query = 'select * from _1_2_'
        return pd.read_sql(query, self.__conn)

    def new_design(self, design_number, hl_qty, l_qty, d_qty, f_qty):
        query = 'insert into _1_2_ (Tile_number, HL_qty, L_qty, D_qty, F_qty) values (%s, %s, %s, %s, %s)'
        self.__cursor.execute(query, (design_number, hl_qty, l_qty, d_qty, f_qty))
        self.__conn.commit()

    def remove_design(self, design_number):
        query = 'drop from _1_2_ where Tile_number = %s'
        self.__cursor.execute(query, (design_number,))


class _16_16_:

    def __init__(self):
        self.__conn = get_connection()
        self.__cursor = self.__conn.cursor()

    def check(self):
        query = 'select * from _16_16_'
        return pd.read_sql(query, self.__conn)

    def new_design(self, design_name, design_number, qty):
        query = 'insert into _16_16_(Design_name, Tile_number, Qty) values (%s, %s, %s)'
        self.__cursor.execute(query, (design_name, design_number, qty))
        self.__conn.commit()

    def remove_design(self, design_number):
        query = 'drop from _16_16_ where Tile_number = %s'
        self.__cursor.execute(query, (design_number,))


class _20_20_:

    def __init__(self):
        self.__conn = get_connection()
        self.__cursor = self.__conn.cursor()

    def check(self):
        query = 'select * from _20_20_'
        return pd.read_sql(query, self.__conn)

    def new_design(self, design_name, design_number, qty):
        query = 'insert into _20_20_(Design_name, Tile_number, Qty) values (%s, %s, %s)'
        self.__cursor.execute(query, (design_name, design_number, qty))
        self.__conn.commit()

    def remove_design(self, design_number):
        query = 'drop from _20_20_ where Tile_number = %s'
        self.__cursor.execute(query, (design_number,))
