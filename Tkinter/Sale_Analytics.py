from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
from Database import get_connection
import tkinter as tk

def show_sales_analytics(tab_analytics):
    for widget in tab_analytics.winfo_children():
        widget.destroy()
    conn = get_connection()
    query_sales = """
        SELECT DATE_FORMAT(Date_, '%Y-%m') AS month,
               SUM(Total_Amount) AS revenue
        FROM Sale
        GROUP BY month
        ORDER BY month;
    """
    df_sales = pd.read_sql(query_sales, conn)
    query_tiles = """
        SELECT tile_name_number,
               SUM(quantity) AS total_quantity
        FROM sale_items
        GROUP BY tile_name_number
        ORDER BY total_quantity DESC
        LIMIT 5;
    """
    df_tiles = pd.read_sql(query_tiles, conn)
    conn.close()
    fig = plt.figure(figsize=(7,6))
    ax1 = fig.add_subplot(211)
    ax1.plot(df_sales['month'], df_sales['revenue'])
    ax1.set_title("Monthly Revenue Trend")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Revenue")
    ax2 = fig.add_subplot(212)
    ax2.bar(df_tiles['tile_name_number'], df_tiles['total_quantity'])
    ax2.set_title("Top 5 Selling Tiles")
    ax2.set_xlabel("Tile")
    ax2.set_ylabel("Quantity Sold")
    ax2.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=tab_analytics)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    total_revenue = df_sales['revenue'].sum()
    total_quantity = df_tiles['total_quantity'].sum()
    summary = f"""
    Total Revenue: ₹{total_revenue}
    Top 5 Tiles Total Quantity: {total_quantity}
    Best Selling Tile: {df_tiles.iloc[0]['tile_name_number']}
    """

    tk.Label(
        tab_analytics,
        text=summary,
        font=("Arial", 11, "bold"),
        bg="#f0f4f8",
        fg="#1f4e79",
        justify="left"
    ).pack(pady=10)
