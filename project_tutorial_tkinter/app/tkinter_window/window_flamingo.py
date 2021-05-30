from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("700x600")

#Frame
frame = Frame(window, widt=500, height=50)
frame.config(bg="pale violet red",
             bd=12,
             relief="raised")
frame.pack(anchor=CENTER)

#Text
frame_text = Label(frame, text=str("Bienvenido a mi programa"))
frame_text.config(fg="black",
                  bg="pale violet red",
                  font=("Consolas", 15),
                  bd=3,
                  width=450,
                  height=40,
                  relief=SOLID)
frame_text.pack(side=TOP, anchor=CENTER)
frame.pack_propagate(False)


my_text = Label(window, text="By Lourdes")
my_text.config(cursor="spider",
               bg="CadetBlue")
my_text.pack(side=BOTTOM, fill=X)


flamingo_text = Label(window,text="Flamingo")
flamingo_text.config(width=20,
                     height=2,
                     bg="LightSalmon2")
flamingo_text.pack(side=LEFT)


flamingo_text_2 = Label(window,text="Flamingo")
flamingo_text_2.config(width=20,
                     height=2,
                     bg="orchid",
                     fg="gray")
flamingo_text_2.pack(side=LEFT)


#Add image
image = Image.open("../resources/imagen/flamingo.png")
render = ImageTk.PhotoImage(image)
Label(window, image=render).pack()


window.mainloop()
