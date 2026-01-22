from Stock import _12_18_
from Stock import _1_2_
from Stock import _2_2_
from Stock import _2_4_
from Stock import _16_16_
from Stock import _20_20_
import Sale
import Debt
from Database import get_connection

import tkinter as tk
from tkinter import ttk, messagebox


_12_18_ = _12_18_()
_1_2_ = _1_2_()
_2_2_ = _2_2_()
_2_4_ = _2_4_()
_16_16_ = _16_16_()
_20_20_ = _20_20_()


root = tk.Tk()
root.title("STOCK_MANAGER_APP")
root.geometry("600x400")

def Select_tile_type():
    value = combo.get()
    if(value == '12X18'):
        _1218()
def data(cols):
    tree = ttk.Treeview(root, columns=cols, show="headings")

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=150, anchor="center")

    tree.pack(fill="both", expand=True, padx=10, pady=2)


def _1218():
    frame_1218 = tk.LabelFrame(root, text='12x18')
    frame_1218.pack(fill='x', padx=20, expand = True)
    number_label = tk.Label(frame_1218, text='TILE NUMBER')
    number_label.grid(row=1, column=0, padx=10, pady=10)
    Tile_number_entry = tk.Entry(frame_1218)
    Tile_number_entry.grid(row=1, column=1, padx=10, pady=10)

    hl_label = tk.Label(frame_1218, text='HL')
    hl_label.grid(row=1, column=2, padx=10, pady=10)
    hl_entry = tk.Entry(frame_1218)
    hl_entry.grid(row=1, column=3, padx=10, pady=10)

    l_label = tk.Label(frame_1218, text='L')
    l_label.grid(row=1, column=4, padx=10, pady=10)
    l_entry = tk.Entry(frame_1218)
    l_entry.grid(row=1, column=5, padx=10, pady=10)

    d_label = tk.Label(frame_1218, text='D')
    d_label.grid(row=1, column=6, padx=10, pady=10)
    d_entry = tk.Entry(frame_1218)
    d_entry.grid(row=1, column=7, padx=10, pady=10)

    f_label = tk.Label(frame_1218, text='F')
    f_label.grid(row=1, column=8, padx=10, pady=10)
    f_entry = tk.Entry(frame_1218)
    f_entry.grid(row=1, column=9, padx=10, pady=10)
    cols = ['Tile_Number','HL', 'L', 'D', 'F']
    data(cols)

def _12():
    pass

def _22():
    pass

def _24():
    pass

def _1616():
    pass

def _2020():
    pass


options = ["12X18", "1X2", "2X4", "2X2", "16X16", "20X20"]
dropdown_frame = tk.Frame(root)
dropdown_frame.pack(fill = 'x')
Tile_type = tk.Label(dropdown_frame, text='SELECT TILE_TYPE')
Tile_type.grid(row = 0, column= 0, padx = 10, pady = 10)
combo = ttk.Combobox(dropdown_frame, values=options)
combo.grid(row = 0, column= 1, padx = 10, pady = 10)
button = tk.Button(dropdown_frame, text= "Check_Data", command = Select_tile_type)
button.grid(row = 1, columns = 1, padx = 30, pady = 10)
root.mainloop()