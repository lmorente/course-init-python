"""
   calculator:
   - two field
   - four button: sum, subtract, multiply and divide
   - show result in alert
"""

from tkinter import *
from tkinter import messagebox as Messagebox


calculator = Tk()
calculator.geometry("400x400")
calculator.title("Calculadora")

frame = Frame(calculator, width=250, height=250)
frame.config(
    bd=5,
    relief=SOLID,
    padx=15,
    pady=15
)
frame.pack(anchor=CENTER)
frame.pack_propagate(False)

#Data
num_1 = StringVar()
num_2 = StringVar()
result = StringVar()

#Fuction
def parseFloat(num):
    result = 0
    try:
        result = float(num)
    except:
        Messagebox.showerror("Error", "Complete los datos con valores númericos")
    return result

def add():
    result.set(parseFloat(num_1.get()) + parseFloat(num_2.get()))
    show()

def subtract():
    result.set(parseFloat(num_1.get()) - parseFloat(num_2.get()))
    show()

def multiply():
    result.set(parseFloat(num_1.get()) * parseFloat(num_2.get()))
    show()
def divide():
    result.set(parseFloat(num_1.get()) / parseFloat(num_2.get()))
    show()

def show():
    Messagebox.showinfo("Resultado", f"Resultado de la operación es: {result.get()}")
    delete()

def delete():
    num_1.set("")
    num_2.set("")

#Fields
Label(frame, text="Primer Número").pack()
Entry(frame, textvariable=num_1, justify="center").pack()

Label(frame, text="Segundo Número").pack()
Entry(frame, textvariable=num_2, justify="center").pack()

Button(frame, text="Sumar", command=add).pack(side="left", fill=X, expand=YES)
Button(frame, text="Restar", command=subtract).pack(side="left", fill=X, expand=YES)
Button(frame, text="Múltiplicar", command=multiply).pack(side="left", fill=X, expand=YES)
Button(frame, text="Dividir", command=divide).pack(side="left", fill=X, expand=YES)

calculator.mainloop()