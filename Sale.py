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

    if(pending != 0):
      query = 'insert into Customer_debt(Customer_Address, Customer_phone_num, Amount_pending) values (%s, %s, %s)'
      self.__cursor.execute(query, (address, phone_number, pending))

class Sale_Items:
  def __init__(self):
    self.__conn = get_connection()
    self.__cursor = self.__conn.cursor()
  
  def update_in_stock(self, other, Tile_number, Tile_name, Tile_size, Tile_Type, qty):
    if(Tile_size == 1218):
      if(Tile_Type == 1):
        query = "update _12_18_ set HL_qty = %s where Tile_number = %s"
        self.__cursor.execute(query, (qty, Tile_number))
      elif(Tile_Type == 2):
        query = "update _12_18_ set L_qty = %s where Tile_number = %s"
        self.__cursor.execute(query, (qty, Tile_number))
      elif(Tile_Type == 3):
        query = "update _12_18_ set D_qty = %s where Tile_number = %s"
        self.__cursor.execute(query, (qty, Tile_number))
      else:
        query = "update _12_18_ set F_qty = %s where Tile_number = %s"
        self.__cursor.execute(query, (qty, Tile_number))
    
    elif(Tile_size == 12):
      if(Tile_Type == 1):
        query = "update _1_2_ set HL_qty = %s where Tile_number = %s"
        self.__cursor.execute(query, (qty, Tile_number))
      elif(Tile_Type == 2):
        query = "update _1_2_ set L_qty = %s where Tile_number = %s"
        self.__cursor.execute(query, (qty, Tile_number))
      elif(Tile_Type == 3):
        query = "update _1_2_ set D_qty = %s where Tile_number = %s"
        self.__cursor.execute(query, (qty, Tile_number))
      else:
        query = "update _1_2_ set F_qty = %s where Tile_number = %s"
        self.__cursor.execute(query, (qty, Tile_number))

    elif(Tile_size == 24):
      query = "update _2_4 set Qty = %s where Tile_name = %s"
      self.__cursor.execute(query, (qty, Tile_name))
