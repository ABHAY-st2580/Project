Create Table _12_18_(
	Tile_number INT Primary Key,
    HL_qty INT,
    L_qty INT,
    D_qty INT,
    F_qty INT
);

Create Table _2_4_(
    Tile_name varchar(100) Primary Key,
    Qty INT
);

Create Table _16_16_(
    Design_name varchar(100) Unique,
	Tile_number INT Primary Key,
    Qty INT
);

Create Table _20_20_(
    Design_name varchar(100) Unique,
	Tile_number INT Primary Key,
    Qty INT
);

Create Table _1_2_(
	Tile_number INT Primary Key,
    HL_qty INT,
    L_qty INT,
    D_qty INT,
    F_qty INT
);

Create Table _2_2_(
	Tile_name varchar(100) Primary Key,
    Qty INT
);


Create Table Customer_debt(
	Cust_id INT auto_increment Primary Key,
    Customer_name varchar(20),
    Customer_phone_number INT(10),
    Customer_Address varchar(250),
    Amount_Pending INT
);
CREATE TABLE Sale (
    Sale_id INT AUTO_INCREMENT PRIMARY KEY,
    Cust_id INT,
    Date_ TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Total_Amount INT,
    Fare_Amount INT,
    Amount_Paid INT,
    Amount_Pending INT,
    FOREIGN KEY (Cust_id) REFERENCES Customer_debt(Cust_id)
);
CREATE TABLE Sale_Items (
    Item_id INT AUTO_INCREMENT PRIMARY KEY,
    Sale_id INT,
    Tile_Size VARCHAR(20),
    Tile_Type VARCHAR(10),
    Quantity INT,
    Rate INT,
    FOREIGN KEY (Sale_id) REFERENCES Sale(Sale_id)
);