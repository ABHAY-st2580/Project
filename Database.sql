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
 Design_name varchar(100) Primary Key,
	Tile_number INT,
    Qty INT
);
Create Table _20_20_(
 Design_name varchar(100) Primary Key,
	Tile_number INT,
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
    Cust_name varchar(20),
    Date_ TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Total_Amount INT,
    Fare_Amount INT,
    Amount_Pending INT,
    Address Text,
    Phone_number int(10)
);
CREATE TABLE sale_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_id INT,
    tile_type VARCHAR(20),
    HL_L_D_F VARCHAR(20) default NULL,
    tile_name_number VARCHAR(100),
    quantity INT,
    FOREIGN KEY (Sale_id) REFERENCES Sale(Sale_id)
);