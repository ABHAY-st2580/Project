# 🧱 TileTracker – Tile Stock Management System

A **desktop-based stock and sales management system** designed for tile shops to efficiently manage inventory, customer transactions, and product demand.  
The system also integrates **data mining algorithms** to generate useful business insights from sales data.

---

## 🚀 Features

- 📦 **Inventory Management**
  - Track available tile stock
  - Manage tile categories and quantities

- 🧾 **Sales Entry System**
  - Record customer purchases
  - Store transaction history

- 👤 **Customer Management**
  - Maintain customer details
  - Track customer purchase records

- 🤖 **Machine Learning Insights**
  - Market Basket Analysis using **Apriori & FP-Growth**
  - Discover frequently purchased tile combinations

- 📊 **Data Visualization**
  - Sales trend graphs
  - Demand analysis using **Matplotlib**

- 🖥 **Graphical User Interface**
  - Interactive dashboard built using **Tkinter / CustomTkinter**

---

## 🛠 Tech Stack

| Technology | Usage |
|-----------|------|
| **Python** | Core programming |
| **Tkinter / CustomTkinter** | GUI development |
| **MySQL** | Database management |
| **Pandas** | Data processing |
| **Matplotlib** | Data visualization |
| **Apriori Algorithm** | Frequent itemset mining |
| **FP-Growth Algorithm** | Market basket analysis |

---

## 🏗 Project Structure

```
TileTracker/
│
├── main.py
├── database/
│   ├── schema.sql
│
├── gui/
│   ├── dashboard.py
│   ├── sales_entry.py
│
├── ml/
│   ├── apriori_analysis.py
│   ├── fp_growth_analysis.py
│
├── visualization/
│   ├── sales_graphs.py
│
└── README.md
```

---

## 📊 Machine Learning Insights

The system applies **Market Basket Analysis** on tile sales data to:

- Identify **frequently bought tile combinations**
- Detect **sales patterns**
- Assist in **inventory planning**
- Provide **data-driven business insights**

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/tilesense-stock-management.git
```

### 2️⃣ Navigate to project directory

```bash
cd tilesense-stock-management
```

### 3️⃣ Install required libraries

```bash
pip install pandas matplotlib mlxtend mysql-connector-python
```

### 4️⃣ Setup MySQL database

Import the provided SQL schema file into your MySQL database.

### 5️⃣ Run the application

```bash
python main.py
```

---

## 📷 Application Screenshots

<!-- <img width="1919" height="1129" alt="image" src="https://github.com/user-attachments/assets/f7c21349-802b-4d20-824a-26b631d37792" /> -->
<img width="959" height="500" alt="image" src="https://github.com/user-attachments/assets/0cbed8aa-0726-496b-b850-32a913a9028c" />



---

## 📈 Future Improvements

- Tile **demand prediction using ML models**
- **Web-based version** using Django
- Automated **stock alerts**
- Advanced **analytics dashboard**

---

## 👨‍💻 Author

**Abhay Singh Tomar**  
B.Tech Computer Science  
National Institute of Technology Kurukshetra

---

⭐ If you found this project useful, consider **starring the repository**.
