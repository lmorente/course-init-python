from tkinter import *
from tkinter import ttk

#Window
principal = Tk()
#principal.geometry("500x500")
principal.minsize(500,500)
principal.title("Proyecto Tkinter")
principal.resizable(0,0)

#Def views
home_label = Label(principal, text="inicio")

#products_box = Frame(principal, width=250)
#Label(products_box).grid(row=0)

products_table = ttk.Treeview(height=12, columns=2)
products_table.grid(row=1, column=0, columnspan=2)
products_table.heading("#0", text='Producto', anchor=W)
products_table.heading("#1", text='Precio', anchor=W)

add_label = Label(principal, text="Añadir producto")
info_label = Label(principal, text="Información")
data_label = Label(principal, text="Producto")

#Functions views
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=220,
        pady=20
    )
    home_label.grid(row=0, column=0)

    show_products_table()
    #show_products()
    #products_box.grid(row=1, column=0)

    #close other views
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()

def add():
    #header
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=100,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=2)

    #forms
    add_frame.grid(row=1, column=0)
    add_name_label.grid(row=1, column=0, padx=0, pady=5, sticky=W)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=0, pady=5, sticky=W)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=0, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4, column=0)

    save.grid(row=5, column=1, sticky=E)
    save.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    #close other views
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_table.grid_remove()


def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    #close other views
    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    products_table.grid_remove()

def add_product():
    products.append([
        name.get(),
        price.get(),
        add_description_entry.get("1.0", "end-1c")
    ])

    name.set("")
    price.set("")
    add_description_entry.delete("1.0", END)

    home()
    print((products))

'''
def show_products():
    for product in products:
        if(len(product)) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="------").grid()
'''

def show_products_table():
    for product in products:
        if(len(product)) == 3:
            product.append("added")
            products_table.insert('', 0, text=product[0], values=(product[1]))


#forms
name = StringVar()
price = StringVar()
products = []

add_frame = Frame(principal)
add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price)

add_description_label = Label(add_frame, text="Descripción: ")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

save = Button(add_frame, text="Guardar", command=add_product)


#Init home
home()

#Top Menu
top_menu = Menu(principal)
top_menu.add_command(label="Home", command=home)
top_menu.add_command(label="Añadir",command=add)
top_menu.add_command(label="Información", command=info)
top_menu.add_command(label="Salir", command=principal.quit)
principal.config(menu=top_menu)

principal.mainloop()
