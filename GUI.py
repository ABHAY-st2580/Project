from Stock import _12_18_
from Stock import _1_2_
from Stock import _2_2_
from Stock import _2_4_
from Stock import _16_16_
from Stock import _20_20_
from Sale import Sale_Items, Sale
from Debt import Debt
import tkinter as tk
from tkinter import ttk, messagebox

frame = None
tree_ = None
tree = None
p2 = None
Tile_number_entry, hl_entry, l_entry, d_entry, f_entry, Tile_name_entry, entry, records = None, None, None,None,None,None,None, None
update_items = Sale_Items()
tile_entries = {}

root = tk.Tk()
root.title("STOCK_MANAGER_APP")
root.geometry("1000x600")


def remove_selected_one():
    global tree_, Tile_name_entry, Tile_number_entry
    value = combo.get()
    if not tree_.selection():
        messagebox.showwarning("Warning", "Please select a row first")
        return
    if (value == '12X18'):
        x = Tile_number_entry.get()
        _12_18 = _12_18_()
        _12_18.remove_design(x)
    elif (value == '1X2'):
        x = Tile_number_entry.get()
        _1_2 = _1_2_()
        _1_2.remove_design(x)
    elif (value == '2X2'):
        x = Tile_name_entry.get()
        _2_2 = _2_2_()
        _2_2.remove_design(x)
    elif (value == '2X4'):
        x = Tile_name_entry.get()
        _2_4 = _2_4_()
        _2_4.remove_design(x)
    elif (value == '16X16'):
        x = Tile_name_entry.get()
        _16_16 = _16_16_()
        _16_16.remove_design(x)
    elif (value == '20X20'):
        x = Tile_name_entry.get()
        _20_20 = _20_20_()
        _20_20.remove_design(x)

    tree_.delete(tree_.selection()[0])
    clear_boxes()
def clear_boxes():
    global Tile_number_entry, hl_entry, l_entry, d_entry, f_entry, Tile_name_entry, entry, tree_
    value = combo.get()
    if (value == '12X18' or value == '1X2'):
        Tile_number_entry.delete(0, 'end')
        hl_entry.delete(0, 'end')
        l_entry.delete(0, 'end')
        d_entry.delete(0, 'end')
        f_entry.delete(0, 'end')
    elif (value == '2X4' or value == '2X2' or value == '16X16' or value == '20X20'):
        Tile_name_entry.delete(0, 'end')
        entry.delete(0, 'end')
def select_record(e):
        global Tile_number_entry, hl_entry, l_entry, d_entry, f_entry, Tile_name_entry, entry, tree_
        value = combo.get()
        if(value == '12X18' or value == '1X2'):
            Tile_number_entry.delete(0, 'end')
            hl_entry.delete(0, 'end')
            l_entry.delete(0, 'end')
            d_entry.delete(0, 'end')
            f_entry.delete(0, 'end')
            selected = tree_.focus()
            values = tree_.item(selected, 'values')

            Tile_number_entry.insert(0, values[0])
            hl_entry.insert(0, values[1])
            l_entry.insert(0, values[2])
            d_entry.insert(0, values[3])
            f_entry.insert(0, values[4])
        elif(value == '2X4' or value == '2X2' or value == '16X16' or value == '20X20'):
            Tile_name_entry.delete(0, 'end')
            entry.delete(0, 'end')

            selected = tree_.focus()
            values = tree_.item(selected, 'values')

            Tile_name_entry.insert(0, values[0])
            entry.insert(0, values[1])

def view(record1):
    global tree_
    tree_.delete(*tree_.get_children())
    for index, row in enumerate(record1):
        if index % 2 == 0:
            tree_.insert("", "end", values=row, tags=('evenrow',))
        else:
            tree_.insert("", "end", values=row, tags=('oddrow',))

def check_data():
    value = combo.get()
    if (value == '12X18'):
        _12_18 = _12_18_()
        record1 = _12_18.check()
        view(record1)
    elif (value == '1X2'):
        _1_2 = _1_2_()
        record1 = _1_2.check()
        view(record1)
    elif (value == '2X2'):
        _2_2 = _2_2_()
        record1 = _2_2.check()
        view(record1)
    elif (value == '2X4'):
        _2_4 = _2_4_()
        record1 = _2_4.check()
        view(record1)
    elif (value == '16X16'):
        _16_16 = _16_16_()
        record1 = _16_16.check()
        view(record1)
    elif (value == '20X20'):
        _20_20 = _20_20_()
        record1 = _20_20.check()
        view(record1)
def new_record():
    global Tile_name_entry, entry, hl_entry, l_entry, d_entry, f_entry, Tile_number_entry, records, p2
    value = combo.get()
    if (value == '12X18'):
        _12_18 = _12_18_()
        _12_18.new_design(design_number=Tile_number_entry.get(), hl_qty=hl_entry.get(),
                                     l_qty=l_entry.get(),
                                     f_qty=f_entry.get(), d_qty=d_entry.get())
        records = _12_18.check()
        view(records)
    elif (value == '1X2'):
        _1_2 = _1_2_()
        _1_2.new_design(design_number=Tile_number_entry.get(), hl_qty=hl_entry.get(),
                                     l_qty=l_entry.get(),
                                     f_qty=f_entry.get(), d_qty=d_entry.get())
        records = _1_2.check()
        view(records)
    elif (value == '2X2'):
        _2_2 = _2_2_()
        _2_2.new_design(design_name=Tile_name_entry.get(), qty=entry.get())
        records = _2_2.check()
        view(records)
    elif (value == '2X4'):
        _2_4 = _2_4_()
        _2_4.new_design(design_name=Tile_name_entry.get(), qty=entry.get())
        records = _2_4.check()
        view(records)
    elif (value == '16X16'):
        _16_16 = _16_16_()
        _16_16.new_design(design_name=Tile_name_entry.get(), design_number = p2.get(), qty=entry.get())
        records = _16_16.check()
        view(records)
    elif (value == '20X20'):
        _20_20 = _20_20_()
        _20_20.new_design(design_name=Tile_name_entry.get(), design_number = p2.get(), qty=entry.get())
        records = _20_20.check()
        view(records)


def update():
    global frame, Tile_name_entry, entry, hl_entry,l_entry,d_entry,f_entry,Tile_number_entry, records, tree_
    value = combo.get()
    if Tile_number_entry is None:
        messagebox.showwarning("Warning", "Please Fill Tile_Number")
        return
    if Tile_name_entry is None:
        messagebox.showwarning("Warning", "Please Fill Tile_Name")
        return
    if (value == '12X18'):
        _12_18 = _12_18_()
        update_items.update_in_stock(Tile_number= Tile_number_entry.get(), Tile_size= 1218, hl_qty = hl_entry.get(), l_qty = l_entry.get(),
                                     f_qty = f_entry.get(), d_qty = d_entry.get())
        records = _12_18.check()
        print(records)
    elif (value == '1X2'):
        _1_2 = _1_2_()
        update_items.update_in_stock(Tile_number= Tile_number_entry.get(), Tile_size= 12, hl_qty = hl_entry.get(), l_qty = l_entry.get(),
                                     f_qty = f_entry.get(), d_qty = d_entry.get())
        records = _1_2.check()
    elif(value == '2X2'):
        _2_2 = _2_2_()
        update_items.update_in_stock(Tile_name = Tile_name_entry.get(), Tile_size=22, qty = entry.get())
        records = _2_2.check()
    elif (value == '2X4'):
        _2_4 = _2_4_()
        update_items.update_in_stock(Tile_name=Tile_name_entry.get(), Tile_size=24, qty=entry.get())
        records = _2_4.check()
    elif (value == '16X16'):
        _16_16 = _16_16_()
        update_items.update_in_stock(Tile_name=Tile_name_entry.get(), Tile_size=1616, qty=entry.get())
        records = _16_16.check()
    elif (value == '20X20'):
        _20_20 = _20_20_()
        update_items.update_in_stock(Tile_name=Tile_name_entry.get(), Tile_size=2020, qty=entry.get())
        records = _20_20.check()
    view(records)
def add_sale_record():
    global customer_entries, tile_entries
    sale = Sale()
    customer_name = customer_entries["Customer Name"].get()
    total_amount = customer_entries["Total Amount"].get()
    fare_amount = customer_entries["Fare Amount"].get()
    amount_pending = customer_entries["Amount Pending"].get()
    address = customer_entries["Address"].get()
    phone = customer_entries["Phone Number"].get()

    sale.new_sale(total_amount, customer_name, fare_amount, amount_pending, phone, address)

    record = sale.All_sale()
    view(record)
def Check_Sale():
    global frame, tree_
    if (frame is not None):
        frame.destroy()
    if (tree_ is not None):
        tree_.destroy()
    if (tree is not None):
        tree.destroy()

    frame = tk.LabelFrame(root, text='SALE')
    frame.pack(fill='x', padx=10, pady=2)
    update_ = tk.Button(frame, text="SALE(UPDATE)", command=update, font=("Arial", 8, "bold"))
    update_.grid(row=0, column=0, padx=30, pady=10)
    clear_box = tk.Button(frame, text='CLEAR_DEBT', command=clear_boxes, font=("Arial", 8, "bold"))
    clear_box.grid(row=0, column=2, padx=30, pady=10)
    remove_selected = tk.Button(frame, text='REMOVE_SELECTED_ONE', command=remove_selected_one, font=("Arial", 8, "bold"))
    remove_selected.grid(row=0, column=3, padx=30, pady=10)
    cols = ['Sale_id', 'Customer_Name', 'Date', 'Total_Amount', 'Fare_Amount', 'Amount_Pending', 'Address', 'Phone_Number']
    data(cols)
    sale = Sale()
    record = sale.All_sale()
    view(record)

def Check_Debt():
    global frame, tree_
    if (frame is not None):
        frame.destroy()
    if (tree_ is not None):
        tree_.destroy()
    if (tree is not None):
        tree.destroy()

    frame = tk.LabelFrame(root, text='DEBT')
    frame.pack(fill='x', padx=10, pady=2)
    update_ = tk.Button(frame, text="DEBT(UPDATE)", command=update, font=("Arial", 8, "bold"))
    update_.grid(row=0, column=0, padx=30, pady=10)
    clear_box = tk.Button(frame, text='CLEAR_DEBT', command=clear_boxes, font=("Arial", 8, "bold"))
    clear_box.grid(row=0, column=2, padx=30, pady=10)
    remove_selected = tk.Button(frame, text='REMOVE_SELECTED_ONE', command=remove_selected_one, font=("Arial", 8, "bold"))
    remove_selected.grid(row=0, column=3, padx=30, pady=10)
    cols = ['Customer_Name', 'Amount_Pending', 'Address', 'Phone_Number']
    data(cols)
    debt = Debt()
    record = debt.check()
    view(record)
def Select_tile_type():
    value = combo.get()
    global frame, tree_
    if (frame is not None):
        frame.destroy()
    if (tree_ is not None):
        tree_.destroy()
    if (tree is not None):
        tree.destroy()


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
    else:
        messagebox.showwarning("Warning", "Please Fill Correct Tile_Type")
        return
def data(cols):
    global tree_, tree
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', background = '#D3D3D3', foreground = 'black', rowheight = 25, fieldbackground = '#D3D3D3')
    style.map('Treeview', background = [('selected', '#347083')])
    tree = tk.Frame(root)
    tree.pack(pady = 10, fill = 'x')
    tree_scroll = tk.Scrollbar(tree)
    tree_scroll.pack(side = 'right', fill = 'y')

    tree_ = ttk.Treeview(tree, columns=cols, show="headings", yscrollcommand=tree_scroll.set, selectmode = 'extended')
    for c in cols:
        tree_.heading(c, text=c)
        tree_.column(c, width=150, anchor="center")

    tree_.pack(fill="both", padx=10, pady=2)
    tree_scroll.config(command = tree_.yview)

    tree_.tag_configure('oddrow', background='white')
    tree_.tag_configure('evenrow', background='lightblue')

    tree_.bind('<ButtonRelease-1>', select_record)

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

    update_ = tk.Button(frame, text="TILE_SOLD(UPDATE)", command = update, font=("Arial", 8, "bold"), bg = 'lightblue')
    update_.grid(row=2, column=0, padx=30, pady=10)

    add_record = tk.Button(frame, text = 'ADD NEW DESIGN', command = new_record, font=("Arial", 8, "bold"), bg = 'lightblue')
    add_record.grid(row = 2, column = 1, padx = 30, pady = 10)

    clear_box = tk.Button(frame, text='CLEAR_BOXES', command=clear_boxes, font=("Arial", 8, "bold"), bg = 'lightblue')
    clear_box.grid(row=2, column=2, padx=30, pady=10)

    remove_selected = tk.Button(frame, text='REMOVE_SELECTED_ONE', command=remove_selected_one, font=("Arial", 8, "bold"), bg = 'lightblue')
    remove_selected.grid(row=2, column=3, padx=30, pady=10)
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

    button = tk.Button(frame, text="TILE_SOLD(UPDATE)", command=update, font=("Arial", 8, "bold"), bg = 'lightblue')
    button.grid(row=2, column=0, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record, font=("Arial", 8, "bold"), bg = 'lightblue')
    add_record.grid(row=2, column=1, padx=30, pady=10)

    clear_box = tk.Button(frame, text='CLEAR_BOXES', command=clear_boxes, font=("Arial", 8, "bold"), bg = 'lightblue')
    clear_box.grid(row=2, column=2, padx=30, pady=10)

    remove_selected = tk.Button(frame, text='REMOVE_SELECTED_ONE', command=remove_selected_one, font=("Arial", 8, "bold"), bg = 'lightblue')
    remove_selected.grid(row=2, column=3, padx=30, pady=10)
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

    button = tk.Button(frame, text="TILE_SOLD(UPDATE)", command=update, font=("Arial", 8, "bold"), bg = 'lightblue')
    button.grid(row=2, column=0, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record, font=("Arial", 8, "bold"), bg = 'lightblue')
    add_record.grid(row=2, column=1, padx=30, pady=10)

    clear_box = tk.Button(frame, text='CLEAR_BOXES', command=clear_boxes, font=("Arial", 8, "bold"), bg = 'lightblue')
    clear_box.grid(row=2, column=2, padx=30, pady=10)

    remove_selected = tk.Button(frame, text='REMOVE_SELECTED_ONE', command=remove_selected_one, font=("Arial", 8, "bold"), bg = 'lightblue')
    remove_selected.grid(row=2, column=3, padx=30, pady=10)
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

    button = tk.Button(frame, text="TILE_SOLD(UPDATE)", command=update, font=("Arial", 8, "bold"), bg = 'lightblue')
    button.grid(row=2, column=0, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record, font=("Arial", 8, "bold"), bg = 'lightblue')
    add_record.grid(row=2, column=1, padx=30, pady=10)

    clear_box = tk.Button(frame, text='CLEAR_BOXES', command=clear_boxes, font=("Arial", 8, "bold"), bg = 'lightblue')
    clear_box.grid(row=2, column=2, padx=30, pady=10)

    remove_selected = tk.Button(frame, text='REMOVE_SELECTED_ONE', command=remove_selected_one, font=("Arial", 8, "bold"), bg = 'lightblue')
    remove_selected.grid(row=2, column=3, padx=30, pady=10)
    cols = ['TILE_NAME', 'BOXES(QTY)']
    data(cols)
    check_data()

def _1616():
    global frame, Tile_name_entry, entry, p2
    frame = tk.LabelFrame(root, text='16X16')
    frame.pack(fill='x', padx=20, pady = 2)
    number_label = tk.Label(frame, text='TILE NAME')
    number_label.grid(row=1, column=0, padx=10, pady=10)
    Tile_name_entry = tk.Entry(frame)
    Tile_name_entry.grid(row=1, column=1, padx=10, pady=10)

    l2 = tk.Label(frame, text='TILE NUMBER')
    l2.grid(row=1, column=2, padx=10, pady=10)
    p2 = tk.Entry(frame)
    p2.grid(row=1, column=3, padx=10, pady=10)

    label = tk.Label(frame, text='BOXES(QUANTITY)')
    label.grid(row=1, column=4, padx=10, pady=10)
    entry = tk.Entry(frame)
    entry.grid(row=1, column=5, padx=10, pady=10)

    button = tk.Button(frame, text="TILE_SOLD(UPDATE)", command=update, font=("Arial", 8, "bold"), bg = 'lightblue')
    button.grid(row=2, column=0, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record, font=("Arial", 8, "bold"), bg = 'lightblue')
    add_record.grid(row=2, column=1, padx=30, pady=10)

    clear_box = tk.Button(frame, text='CLEAR_BOXES', command=clear_boxes, font=("Arial", 8, "bold"), bg = 'lightblue')
    clear_box.grid(row=2, column=2, padx=30, pady=10)

    remove_selected = tk.Button(frame, text='REMOVE_SELECTED_ONE', command=remove_selected_one, font=("Arial", 8, "bold"), bg = 'lightblue')
    remove_selected.grid(row=2, column=3, padx=30, pady=10)
    cols = ['TILE_NAME','TILE_NUMBER', 'BOXES(QTY)']
    data(cols)
    check_data()

def _2020():
    global frame, Tile_name_entry, entry, p2
    frame = tk.LabelFrame(root, text='16X16')
    frame.pack(fill='x', padx=20, pady=2)
    number_label = tk.Label(frame, text='TILE NAME')
    number_label.grid(row=1, column=0, padx=10, pady=10)
    Tile_name_entry = tk.Entry(frame)
    Tile_name_entry.grid(row=1, column=1, padx=10, pady=10)

    l2 = tk.Label(frame, text='TILE NUMBER')
    l2.grid(row=1, column=2, padx=10, pady=10)
    p2 = tk.Entry(frame)
    p2.grid(row=1, column=3, padx=10, pady=10)

    label = tk.Label(frame, text='BOXES(QUANTITY)')
    label.grid(row=1, column=4, padx=10, pady=10)
    entry = tk.Entry(frame)
    entry.grid(row=1, column=5, padx=10, pady=10)

    button = tk.Button(frame, text="TILE_SOLD(UPDATE)", command=update, font=("Arial", 8, "bold"), bg = 'lightblue')
    button.grid(row=2, column=0, padx=30, pady=10)

    add_record = tk.Button(frame, text='ADD NEW DESIGN', command=new_record, font=("Arial", 8, "bold"), bg = 'lightblue')
    add_record.grid(row=2, column=1, padx=30, pady=10)

    clear_box = tk.Button(frame, text='CLEAR_BOXES', command=clear_boxes, font=("Arial", 8, "bold"), bg = 'lightblue')
    clear_box.grid(row=2, column=2, padx=30, pady=10)

    remove_selected = tk.Button(frame, text='REMOVE_SELECTED_ONE', command=remove_selected_one, font=("Arial", 8, "bold"), bg = 'lightblue')
    remove_selected.grid(row=2, column=3, padx=30, pady=10)
    cols = ['TILE_NAME', 'TILE_NUMBER', 'BOXES(QTY)']
    data(cols)
    check_data()

options = ["12X18", "1X2", "2X4", "2X2", "16X16", "20X20"]
dropdown_frame = tk.Frame(root)
dropdown_frame.pack(fill = 'x')
Tile_type = tk.Label(dropdown_frame, text='SELECT TILE_TYPE', fg = 'Darkblue',font=("Arial", 10, "bold"))
Tile_type.grid(row = 0, column= 0, padx = 10, pady = 10)
combo = ttk.Combobox(dropdown_frame, values=options)
combo.grid(row = 0, column= 1, padx = 10, pady = 10)
button = tk.Button(dropdown_frame, text= "Check_Stock", command = Select_tile_type,
    fg="white",
    bg = 'blue',
    font=("Arial", 8, "bold"),
    height=1)
button.grid(row = 0, column = 3, padx = 30, pady = 3)
sale__ = tk.Button(dropdown_frame, text= "Check_Sale", command = Check_Sale,
    fg="white",
    bg = 'blue',
    font=("Arial", 8, "bold"),
    height=1)
sale__.grid(row = 0, column = 4, padx = 30, pady = 3)
debt__ = tk.Button(dropdown_frame, text= "Check_Debt", command = Check_Debt,
    fg="white",
    bg = 'blue',
    font=("Arial", 8, "bold"),
    height=1)
debt__.grid(row = 0, column = 5, padx = 30, pady = 3)
## Want To add the command
sale_data = tk.Button(dropdown_frame, text= "Check_Sale_Items",
    fg="white",
    bg = 'blue',
    font=("Arial", 8, "bold"),
    height=1)
sale_data.grid(row = 0, column = 6, padx = 30, pady = 3)

main_container = tk.Frame(root)
main_container.pack(fill="both", expand=True)

# ML FRAME
left_panel = tk.Frame(main_container, width=600)
left_panel.pack(side="left", fill="both", expand=True, padx=10, pady=10)

#SALE FRAME
right_panel = tk.Frame(main_container, width=450)
right_panel.pack(side="right", fill="y", padx=10, pady=10)

ml_frame = tk.LabelFrame(left_panel, text="ML Insights", font=("Arial", 12, "bold"))
ml_frame.pack(fill="both", expand=True)

ml_text = tk.Text(ml_frame, height=15, font=("Arial", 10))
ml_text.pack(fill="both", expand=True, padx=10, pady=10)

ml_text.insert("end", "• Frequently Bought Together:\n\n")
ml_text.insert("end", "2X2 → 16X16 (Confidence: 78%)\n")
ml_text.insert("end", "12X18 HL → 1X2 HL (Support: 65%)\n")

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

sale_frame = tk.LabelFrame(right_panel, text="Sale Entry", font=("Arial", 12, "bold"))
sale_frame.pack(fill="both", expand=True)
scroll_container = tk.Frame(sale_frame)
scroll_container.pack(fill="both", expand=True, padx=10, pady=5)
canvas = tk.Canvas(scroll_container)
canvas.pack(side="left", fill="both", expand=True)
scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)
form_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=form_frame, anchor="nw")

form_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.bind_all("<MouseWheel>", _on_mousewheel)
customer_frame = tk.LabelFrame(form_frame, text="Customer Details", padx=10, pady=5, font=("Arial", 11, "bold"))
customer_frame.pack(fill="x", pady=5)

labels = ["Customer Name", "Total Amount", "Fare Amount",
          "Amount Pending", "Address", "Phone Number"]

customer_entries = {}

for i, text in enumerate(labels):
    tk.Label(customer_frame, text=text, width=15, anchor="w", fg = 'indigo',font=("Arial", 9, "bold")).grid(
        row=i, column=0, pady=3, sticky="w"
    )
    entry = tk.Entry(customer_frame, width=25)
    entry.grid(row=i, column=1, pady=3)
    customer_entries[text] = entry

tile_frame = tk.LabelFrame(form_frame, text="Tile Details", padx=10, pady=5, font=("Arial", 11, "bold"))
tile_frame.pack(fill="x", pady=5)


row_counter = 0

tk.Label(tile_frame, text="BASIC TILES", font=("Arial", 10, "bold")).grid(
    row=row_counter, column=0, columnspan=4, pady=5
)
row_counter += 1

basic_tiles = ["2X4", "2X2", "16X16", "20X20"]

for size in basic_tiles:
    tk.Label(tile_frame, text=f"{size} Name", width=12, fg = 'indigo', font = ("Arial",9, "bold" )).grid(
        row=row_counter, column=0, pady=3, sticky="w"
    )
    name_entry = tk.Entry(tile_frame, width=18)
    name_entry.grid(row=row_counter, column=1)

    tk.Label(tile_frame, text="Qty",fg = 'indigo', font = ("Arial",9, "bold" )).grid(row=row_counter, column=2)
    qty_entry = tk.Entry(tile_frame, width=8)
    qty_entry.grid(row=row_counter, column=3)

    tile_entries[size] = {"name": name_entry, "qty": qty_entry}
    row_counter += 1

types = ["HL", "L", "D", "F"]

tk.Label(tile_frame, text="12X18", font=("Arial", 10, "bold")).grid(
    row=row_counter, column=0, columnspan=4, pady=5
)
row_counter += 1

for t in types:
    tk.Label(tile_frame, text=t, width=5, fg = 'indigo', font = ("Arial",9, "bold" )).grid(row=row_counter, column=0, sticky="w")
    name_entry = tk.Entry(tile_frame, width=18)
    name_entry.grid(row=row_counter, column=1)

    tk.Label(tile_frame, text="Qty", fg = 'indigo', font = ("Arial",9, "bold" )).grid(row=row_counter, column=2)
    qty_entry = tk.Entry(tile_frame, width=8)
    qty_entry.grid(row=row_counter, column=3)

    tile_entries[f"12X18_{t}"] = {"name": name_entry, "qty": qty_entry}
    row_counter += 1

tk.Label(tile_frame, text="1X2", font=("Arial", 10, "bold")).grid(
    row=row_counter, column=0, columnspan=4, pady=5
)
row_counter += 1

for t in types:
    tk.Label(tile_frame, text=t, width=5, fg = 'indigo', font = ("Arial",9, "bold" )).grid(row=row_counter, column=0, sticky="w")
    name_entry = tk.Entry(tile_frame, width=18)
    name_entry.grid(row=row_counter, column=1)

    tk.Label(tile_frame, text="Qty", fg = 'indigo', font = ("Arial",9, "bold" )).grid(row=row_counter, column=2)
    qty_entry = tk.Entry(tile_frame, width=8)
    qty_entry.grid(row=row_counter, column=3)

    tile_entries[f"1X2_{t}"] = {"name": name_entry, "qty": qty_entry}
    row_counter += 1

tk.Button(
    sale_frame,
    text="Add Sale",
    bg="lightblue",
    fg="black",
    font=("Arial", 10, "bold"),
    height=2, command = add_sale_record
).pack(fill="x", padx=40, pady=10)

root.mainloop()