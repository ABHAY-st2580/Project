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
    Customer_name varchar(20) DEFAULT NULL,
    Customer_Address varchar(250),
    Customer_phone_number INT(10),
    Amount_Pending INT
);
CREATE TABLE Sale (
    Sale_id INT AUTO_INCREMENT PRIMARY KEY,
    Date_ TIMESTAMP DEFAULT 
    CURRENT_TIMESTAMP,
    Customer_phone_number INT(10),
    Total_Amount INT,
    Fare_Amount INT,
    Amount_Paid INT,
    Amount_Pending INT,
);
-- CREATE TABLE Sale_Items (
--     Tile_number INT Primary Key,
--     Sale_id INT,
--     Tile_Size VARCHAR(20),
--     Tile_Type VARCHAR(10),
--     Quantity INT,
--     Rate INT,
--     FOREIGN KEY (Sale_id) REFERENCES Sale(Sale_id)
-- );