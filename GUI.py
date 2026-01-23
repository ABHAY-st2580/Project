from Stock import _12_18_
from Stock import _1_2_
from Stock import _2_2_
from Stock import _2_4_
from Stock import _16_16_
from Stock import _20_20_
from Sale import Sale
from Sale import Sale_Items
from Debt import Debt
from Database import get_connection

import tkinter as tk
from tkinter import ttk, messagebox

frame = None
tree_ = None
Tile_number_entry, hl_entry, l_entry, d_entry, f_entry, Tile_name_entry, entry, records = None, None, None,None,None,None,None, None
_12_18_ = _12_18_()
_1_2_ = _1_2_()
_2_2_ = _2_2_()
_2_4_ = _2_4_()
_16_16_ = _16_16_()
_20_20_ = _20_20_()
update_items = Sale_Items()

root = tk.Tk()
root.title("STOCK_MANAGER_APP")
root.geometry("600x400")

def view():
    global records, tree_
    if(tree_ != None):
        tree_.delete(*tree_.get_children())
    for index, row in enumerate(records):
        if index % 2 == 0:
            tree_.insert("", "end", values=row, tags=('evenrow',))
        else:
            tree_.insert("", "end", values=row, tags=('oddrow',))

def check_data():
    global records
    value = combo.get()
    if (value == '12X18'):
        records = _12_18_.check()
        view()
    elif (value == '1X2'):
        records = _1_2_.check()
        view()
    elif (value == '2X2'):
        records = _2_2_.check()
        view()
    elif (value == '2X4'):
        records = _2_4_.check()
        view()
    elif (value == '16X16'):
        records = _16_16_.check()
        view()
    elif (value == '20X20'):
        records = _20_20_.check()
        view()
def new_record():
    global frame, Tile_name_entry, entry, hl_entry, l_entry, d_entry, f_entry, Tile_number_entry, records
    value = combo.get()
    if (value == '12X18'):
        _12_18_.new_design(design_number=Tile_number_entry.get(), hl_qty=hl_entry.get(),
                                     l_qty=l_entry.get(),
                                     f_qty=f_entry.get(), d_qty=d_entry.get())
        records = _12_18_.check()
        view()
    elif (value == '1X2'):
        _1_2_.new_design(design_number=Tile_number_entry.get(), hl_qty=hl_entry.get(),
                                     l_qty=l_entry.get(),
                                     f_qty=f_entry.get(), d_qty=d_entry.get())
        records = _1_2_.check()
        view()
    elif (value == '2X2'):
        _2_2_.new_design(design_name=Tile_name_entry.get(), qty=entry.get())
        records = _2_2_.check()
        view()
    elif (value == '2X4'):
        _2_4_.new_design(design_name=Tile_name_entry.get(), qty=entry.get())
        records = _2_4_.check()
        view()
    elif (value == '16X16'):
        _16_16_.new_design(design_name=Tile_name_entry.get(), design_number = 0, qty=entry.get())
        records = _16_16_.check()
        view()
    elif (value == '20X20'):
        _20_20_.new_design(design_name=Tile_name_entry.get(), design_number = 0, qty=entry.get())
        records = _20_20_.check()
        view()


def update():
    global frame, Tile_name_entry, entry, hl_entry,l_entry,d_entry,f_entry,Tile_number_entry, records
    value = combo.get()
    if (value == '12X18'):
        update_items.update_in_stock(Tile_number= Tile_number_entry.get(), Tile_size= 1218, hl_qty = hl_entry.get(), l_qty = l_entry.get(),
                                     f_qty = f_entry.get(), d_qty = d_entry.get())
        records = _12_18_.check()
        view()
    elif (value == '1X2'):
        update_items.update_in_stock(Tile_number= Tile_number_entry.get(), Tile_size= 12, hl_qty = hl_entry.get(), l_qty = l_entry.get(),
                                     f_qty = f_entry.get(), d_qty = d_entry.get())
        records = _1_2_.check()
        view()
    elif(value == '2X2'):
        update_items.update_in_stock(Tile_name = Tile_name_entry.get(), Tile_size=22, qty = entry.get())
        records = _2_2_.check()
        view()
    elif (value == '2X4'):
        update_items.update_in_stock(Tile_name=Tile_name_entry.get(), Tile_size=24, qty=entry.get())
        records = _2_4_.check()
        view()
    elif (value == '16X16'):
        update_items.update_in_stock(Tile_name=Tile_name_entry.get(), Tile_size=1616, qty=entry.get())
        records = _16_16_.check()
        view()
    elif (value == '20X20'):
        update_items.update_in_stock(Tile_name=Tile_name_entry.get(), Tile_size=2020, qty=entry.get())
        records = _20_20_.check()
        view()

def Select_tile_type():
    value = combo.get()
    global frame, tree_
    if (frame is not None) and (tree_ is not None):
        frame.destroy()
        tree_.destroy()

    if(value == '12X18'):
        _1218()
    elif(value == '1X2'):
        _12()
    elif (value == '2X2'):
        _22()
    elif (value == '2X4'):
        _24()
    elif (value == '16X16'):
        _1616()
    elif (value == '20X20'):
        _2020()
def data(cols):
    global tree_
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', background = '#D3D3D3', foreground = 'black', rowheight = 25, fieldbackground = '#D3D3D3')
    style.map('Treeview', background = [('selected', '#347083')])
    tree = tk.Frame(root)
    tree.pack(pady = 10, fill = 'both', expand = 1)
    tree_scroll = tk.Scrollbar(tree)
    tree_scroll.pack(side = 'right', fill = 'y')

    tree_ = ttk.Treeview(tree, columns=cols, show="headings", yscrollcommand=tree_scroll.set, selectmode = 'extended')
    for c in cols:
        tree_.heading(c, text=c)
        tree_.column(c, width=150, anchor="center")

    tree_.pack(fill="both", padx=10, pady=2, expand = 1)
    tree_scroll.config(command = tree_.yview)

    tree_.tag_configure('oddrow', background='white')
    tree_.tag_configure('evenrow', background='lightblue')

def _1218():
    global frame, Tile_number_entry, hl_entry,l_entry,d_entry,f_entry
    frame = tk.LabelFrame(root, text='12x18')
    frame.pack(fill='x', padx=10, pady = 2)
    number_label = tk.Label(frame, text='TILE NUMBER')
    number_label.grid(row=1, column=0, padx=10, pady=10)
    Tile_number_entry = tk.Entry(frame)
    Tile_number_entry.grid(row=1, column=1, padx=10, pady=10)

    hl_label = tk.Label(frame, text='HL')
    hl_label.grid(row=1, column=2, padx=10, pady=10)
    hl_entry = tk.Entry(frame)
    hl_entry.grid(row=1, column=3, padx=10, pady=10)

    l_label = tk.Label(frame, text='L')
    l_label.grid(row=1, column=4, padx=10, pady=10)
    l_entry = tk.Entry(frame)
    l_entry.grid(row=1, column=5, padx=10, pady=10)

    d_label = tk.Label(frame, text='D')
    d_label.grid(row=1, column=6, padx=10, pady=10)
    d_entry = tk.Entry(frame)
    d_entry.grid(row=1, column=7, padx=10, pady=10)

    f_label = tk.Label(frame, text='F')
    f_label.grid(row=1, column=8, padx=10, pady=10)
    f_entry = tk.Entry(frame)
    f_entry.grid(row=1, column=9, padx=10, pady=10)

    update_ = tk.Button(frame, text="UPDATE BOXES", command = update)
    update_.grid(row=2, columns=1, padx=30, pady=10)

    add_record = tk.Button(frame, text = 'ADD NEW DESIGN', command = new_record)
    add_record.grid(row = 2, columns = 4, padx = 30, pady = 10)
    cols = ['Tile_Number','HL', 'L', 'D', 'F']
    data(cols)
    check_data()

def _12():
    global frame, Tile_number_entry, hl_entry,l_entry,d_entry,f_entry
    frame = tk.LabelFrame(root, text='1X2')
    frame.pack(fill='x', padx=20, pady = 2)
    number_label = tk.Label(frame, text='TILE NUMBER')
    number_label.grid(row=1, column=0, padx=10, pady=10)
    Tile_number_entry = tk.Entry(frame)
    Tile_number_entry.grid(row=1, column=1, padx=10, pady=10)

    hl_label = tk.Label(frame, text='HL')
    hl_label.grid(row=1, column=2, padx=10, pady=10)
    hl_entry = tk.Entry(frame)
    hl_entry.grid(row=1, column=3, padx=10, pady=10)

    l_label = tk.Label(frame, text='L')
    l_label.grid(row=1, column=4, padx=10, pady=10)
    l_entry = tk.Entry(frame)
    l_entry.grid(row=1, column=5, padx=10, pady=10)

    d_label = tk.Label(frame, text='D')
    d_label.grid(row=1, column=6, padx=10, pady=10)
    d_entry = tk.Entry(frame)
    d_entry.grid(row=1, column=7, padx=10, pady=10)

    f_label = tk.Label(frame, text='F')
    f_label.grid(row=1, column=8, padx=10, pady=10)
    f_entry = tk.Entry(frame)
    f_entry.grid(row=1, column=9, padx=10, pady=10)

    button = tk.Button(frame, text="UPDATE", command=update)
    button.grid(row=2, columns=1, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record)
    add_record.grid(row=2, columns=4, padx=30, pady=10)
    cols = ['TILE_NUMBER', 'HL', 'L', 'D', 'F']
    data(cols)
    check_data()

def _22():
    global frame, Tile_name_entry, entry
    frame = tk.LabelFrame(root, text='2X2')
    frame.pack(fill='x', padx=20, pady = 2)
    number_label = tk.Label(frame, text='TILE NAME')
    number_label.grid(row=1, column=0, padx=10, pady=10)
    Tile_name_entry = tk.Entry(frame)
    Tile_name_entry.grid(row=1, column=1, padx=10, pady=10)

    label = tk.Label(frame, text='BOXES(QUANTITY)')
    label.grid(row=1, column=2, padx=10, pady=10)
    entry = tk.Entry(frame)
    entry.grid(row=1, column=3, padx=10, pady=10)

    button = tk.Button(frame, text="UPDATE", command=update)
    button.grid(row=2, columns=1, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record)
    add_record.grid(row=2, columns=4, padx=30, pady=10)
    cols = ['TILE_NAME', 'BOXES(QTY)']
    data(cols)
    check_data()

def _24():
    global frame, Tile_name_entry, entry
    frame = tk.LabelFrame(root, text='2X4')
    frame.pack(fill='x', padx=20, pady = 2)
    number_label = tk.Label(frame, text='TILE NAME')
    number_label.grid(row=1, column=0, padx=10, pady=10)
    Tile_name_entry = tk.Entry(frame)
    Tile_name_entry.grid(row=1, column=1, padx=10, pady=10)

    label = tk.Label(frame, text='BOXES(QUANTITY)')
    label.grid(row=1, column=2, padx=10, pady=10)
    entry = tk.Entry(frame)
    entry.grid(row=1, column=3, padx=10, pady=10)

    button = tk.Button(frame, text="UPDATE", command=update)
    button.grid(row=2, columns=1, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record)
    add_record.grid(row=2, columns=4, padx=30, pady=10)
    cols = ['TILE_NAME', 'BOXES(QTY)']
    data(cols)
    check_data()

def _1616():
    global frame, Tile_name_entry, entry
    frame = tk.LabelFrame(root, text='16X16')
    frame.pack(fill='x', padx=20, pady = 2)
    number_label = tk.Label(frame, text='TILE NAME')
    number_label.grid(row=1, column=0, padx=10, pady=10)
    Tile_name_entry = tk.Entry(frame)
    Tile_name_entry.grid(row=1, column=1, padx=10, pady=10)

    label = tk.Label(frame, text='BOXES(QUANTITY)')
    label.grid(row=1, column=2, padx=10, pady=10)
    entry = tk.Entry(frame)
    entry.grid(row=1, column=3, padx=10, pady=10)

    button = tk.Button(frame, text="UPDATE", command=update)
    button.grid(row=2, columns=1, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record)
    add_record.grid(row=2, columns=4, padx=30, pady=10)
    cols = ['TILE_NAME', 'BOXES(QTY)']
    data(cols)
    check_data()

def _2020():
    global frame, Tile_name_entry, entry
    frame = tk.LabelFrame(root, text='20x20')
    frame.pack(fill='x', padx=20, pady = 2)
    number_label = tk.Label(frame, text='TILE NAME')
    number_label.grid(row=1, column=0, padx=10, pady=10)
    Tile_name_entry = tk.Entry(frame)
    Tile_name_entry.grid(row=1, column=1, padx=10, pady=10)

    label = tk.Label(frame, text='BOXES(QUANTITY)')
    label.grid(row=1, column=2, padx=10, pady=10)
    entry = tk.Entry(frame)
    entry.grid(row=1, column=3, padx=10, pady=10)

    button = tk.Button(frame, text="UPDATE", command=update)
    button.grid(row=2, columns=1, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record)
    add_record.grid(row=2, columns=4, padx=30, pady=10)
    cols = ['TILE_NAME', 'BOXES(QTY)']
    data(cols)
    check_data()


options = ["12X18", "1X2", "2X4", "2X2", "16X16", "20X20"]
dropdown_frame = tk.Frame(root)
dropdown_frame.pack(fill = 'x')
Tile_type = tk.Label(dropdown_frame, text='SELECT TILE_TYPE')
Tile_type.grid(row = 0, column= 0, padx = 10, pady = 10)
combo = ttk.Combobox(dropdown_frame, values=options)
combo.grid(row = 0, column= 1, padx = 10, pady = 10)
button = tk.Button(dropdown_frame, text= "Check_Data", command = Select_tile_type)
button.grid(row = 1, columns = 1, padx = 30, pady = 3)
root.mainloop()