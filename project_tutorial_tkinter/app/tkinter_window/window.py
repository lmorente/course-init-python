import os.path
from tkinter import *

class Program:

    def __init__(self, title, path_icon, size, resizable = False):
        self.__window_container = ''
        self.title = title
        self.icon = path_icon
        self.size = size
        self.resizable = resizable

    def create(self):
        # create
        new_window = Tk()

        # title
        new_window.title(self.title)

        # add ico
        path_icon = os.path.abspath(self.icon)
        if os.path.isfile(path_icon):
            new_window.iconbitmap(str(path_icon))

        # size
        new_window.geometry(self.size)
        if self.resizable:
            new_window.resizable(0, 0)  # lock size

        self.__window_container = new_window

    def addText(self, window):
        text_win = Label(window,)
        text_win.pack()

    def run(self):
        self.__window_container(mainloop())



