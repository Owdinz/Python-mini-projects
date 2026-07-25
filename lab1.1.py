import tkinter as tk
import tkinter.messagebox as messagebox

#item clas
class Item:
    def __init__(self, item_id, name, price):
        self.id = item_id
        self.name = name
        self.price = float(price)
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Price: ${self.price:.2f}"
#item store
items = []
#func
def add_item():
    try:
        item_id = entry_id.get()
        name = entry_name.get()
        price = float(entry_price.get())
        new_item = Item(item_id, name, price)
        items.append(new_item)
        output.delete("1.0", tk.END)
        output.insert(tk.END, "New item added!\n")
        output.insert(tk.END, str(new_item))
        clear_entries()
    except ValueError:
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Enter a valid number for the price!\n")
def delete_item():
    item_id = entry_id.get()
    for item in items:
        if item.id == item_id:
            items.remove(item)
            output.delete("1.0", tk.END)
            output.insert(tk.END, "Item Deleted Successfully!\n")
            clear_entries()
            return
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Item not found.\n")
def view_item():
    item_id = entry_id.get()

    output.delete("1.0", tk.END)
    for item in items:
        if item.id == item_id:
            output.insert(tk.END, str(item))
            return
    output.insert(tk.END, "Item not found.")
def view_all():
    output.delete("1.0", tk.END)
    if not items:
        output.insert(tk.END, "No items available.")
        return
    for item in items:
        output.insert(tk.END, str(item) + "\n")
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    
#pop up ui
root = tk.Tk()
root.title("Item Management System")
root.geometry("500x450")

#label
#id
tk.Label(root, text="Item ID").pack()
entry_id = tk.Entry(root, width=30)
entry_id.pack()
#item name
tk.Label(root, text="Item Name").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack()
#price
tk.Label(root, text="Item Price").pack()
entry_price = tk.Entry(root, width=30)
entry_price.pack(pady=5)

#button
tk.Button(root, text="Add Item", width=20, command=add_item).pack(pady=2) #add
tk.Button(root, text="Delete Item", width=20, command=delete_item).pack(pady=2) #del
tk.Button(root, text="View Item", width=20, command=view_item).pack(pady=2)#view
tk.Button(root, text="View All Items", width=20, command=view_all).pack(pady=2)#view all

#output
output = tk.Text(root, height=10, width=60)
output.pack(pady=10)

#start
root.mainloop()