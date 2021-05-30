from tkinter import *

window = Tk()
window.geometry("700x400")
window.title("Formularios en Tkinter")

#Header
header = Label(window, text="Formulario:")
header.config(
    fg="White",
    bg="darkgray",
    font=("Arial", 18),
    padx=10,
    pady=10
)
header.grid(row=0, column=0, columnspan=2, sticky=W)

#Field
name = StringVar()
field_name = Entry(window, textvariable=name)
field_name.grid(row=1, column=1, padx=0, pady=5, sticky=W)

#Label field
name = Label(window, text="Nombre")
name.grid(row=1, column=0, padx=20, pady=5, sticky=NW)

#Field
surname = StringVar()
field_surname = Entry(window, textvariable=surname)
field_surname.grid(row=2, column=1, padx=0, pady=5, sticky=W)

#Label field
surname = Label(window, text="Apellidos")
surname.grid(row=2, column=0, padx=20, pady=5, sticky=NW)

#TextArea
description = StringVar()
field_description = Text(window)
field_description.config(width=30, height=5, pady=15, padx=5)
field_description.grid(row=3, column=1)

description = Label(window, text="Descripción")
description.grid(row=3, column=0, padx=20, pady=5, sticky=NW)

#Button
Label(window).grid(row=4, column=1)
button = Button(window, text="Enviar")
button.config(padx=15, pady=5, bg="green", fg="white")
button.grid(row=5, column=1, sticky=W)

window.mainloop()

"""
Check:
Checkbutton(window, text="Description", variable=x, onvalue=1, offvalue=0, command=funtion).pack()

Ratiobutton:
option = StringVar()
option.setValue(None)
Label(window, text="Description").pack()
Radiobutton(window, text="Option 1", value=1, variable=option, command=check).pack()
Radiobutton(window, text="Option 2", value=0, variable=option, comand=check).pack()

Menu:
option = StringVar()
option.set("Option 1")
Label(window, text="Menu").pack()
select = OptionMenu(window, variable=option, "Option 1", "Option 2")
select.pack()

Drop down menus:
menu = Menu(window)
sub_menu = Menu(menu)
menu.add_cascade(label="Option 1")
menu.add_command(label="Option 2")
"""