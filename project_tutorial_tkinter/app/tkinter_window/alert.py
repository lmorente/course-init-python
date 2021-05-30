from tkinter import *
from tkinter import messagebox as Messagebox

window = Tk()
window.config(bd=70)

def getAlert():
    Messagebox.showinfo("Alerta", "Hola!!")

def getExit():
    result = Messagebox.askquestion("¿Quieres salir?", "Dejarás a un flamingo triste si te vas")
    if result == "yes":
        window.destroy()

button = Button(window, text="Mostrar alerta", command=getExit)
button.pack()

window.mainloop()