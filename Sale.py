# from Stock
from Database import get_connection
class Sale:
  def __init__(self):
    self.__conn = get_connection()
    self.__cursor = self.__conn.cursor()

  def All_sale(self):
    query = 'select * from Sale'
    self.__cursor.execute(query)
    return self.__cursor.fetchall()

  def new_sale(self, amount, paid, pending, phone_number, address):
    query = 'insert into Sale(Customer_phone_num, Total_Amount, Amount_Paid, Amount_Pending) values (%s, %s, %s, %s)'
    self.__cursor.execute(query, (phone_number, amount, paid, pending))
    self.__conn.commit()

    if(pending != 0):
      query = 'insert into Customer_debt(Customer_Address, Customer_phone_num, Amount_pending) values (%s, %s, %s)'
      self.__cursor.execute(query, (address, phone_number, pending))
      self.__conn.commit()

class Sale_Items:
  def __init__(self):
    self.__conn = get_connection()
    self.__cursor = self.__conn.cursor()
  
  def update_in_stock(self, Tile_number = 0, Tile_name = "", Tile_size = 0, qty = 0, hl_qty = 0, l_qty = 0, d_qty = 0, f_qty = 0):
    if(Tile_size == 1218):
        query = "update _12_18_ set HL_qty = HL_qty - %s where Tile_number = %s and HL_qty >= %s"
        self.__cursor.execute(query, (hl_qty, Tile_number, hl_qty))
        self.__conn.commit()
        query = "update _12_18_ set L_qty = L_qty - %s where Tile_number = %s and L_qty >= %s"
        self.__cursor.execute(query, (l_qty, Tile_number, l_qty))
        self.__conn.commit()
        query = "update _12_18_ set D_qty = D_qty - %s where Tile_number = %s and D_qty >= %s"
        self.__cursor.execute(query, (d_qty, Tile_number, d_qty))
        self.__conn.commit()
        query = "update _12_18_ set F_qty = F_qty - %s where Tile_number = %s and F_qty >= %s"
        self.__cursor.execute(query, (f_qty, Tile_number, f_qty))
        self.__conn.commit()
    
    elif(Tile_size == 12):
      query = "update _1_2_ set HL_qty = HL_qty - %s where Tile_number = %s and HL_qty >= %s"
      self.__cursor.execute(query, (hl_qty, Tile_number, hl_qty))
      self.__conn.commit()
      query = "update _1_2_ set L_qty = L_qty - %s where Tile_number = %s and L_qty >= %s"
      self.__cursor.execute(query, (l_qty, Tile_number, l_qty))
      self.__conn.commit()
      query = "update _1_2_ set D_qty = D_qty - %s where Tile_number = %s and D_qty >= %s"
      self.__cursor.execute(query, (d_qty, Tile_number, d_qty))
      self.__conn.commit()
      query = "update _1_2_ set F_qty = F_qty - %s where Tile_number = %s and F_qty >= %s"
      self.__cursor.execute(query, (f_qty, Tile_number, f_qty))
      self.__conn.commit()

    elif(Tile_size == 24):
      query = "update _2_4_ set Qty = Qty - %s where Tile_name = %s and Qty >= %s"
      self.__cursor.execute(query, (qty, Tile_name, qty))
      self.__conn.commit()

    elif (Tile_size == 22):
      query = "update _2_2_ set Qty = Qty - %s where Tile_name = %s and Qty >= %s"
      self.__cursor.execute(query, (qty, Tile_name, qty))
      self.__conn.commit()

    elif(Tile_size == 1616):
      query = "update _16_16_ set Qty = Qty - %s where Design_name = %s and Qty >= %s"
      self.__cursor.execute(query, (qty, Tile_name, qty))
      self.__conn.commit()

    elif (Tile_size == 2020):
      query = "update _20_20_ set Qty = Qty - %s where Design_name = %s and Qty >= %s"
      self.__cursor.execute(query, (qty, Tile_name, qty))
      self.__conn.commit()
