import tkinter as tk
from tkinter import ttk
from tkinter import font

class CommonWidgets:
    @staticmethod
    def set_label(parent, x_start, y_start, text=':'):
        label = ttk.Label(parent, text=text)
        label.place(relx=x_start, rely=y_start)

    @staticmethod
    def set_button(parent, x_start, y_start, width, height, text, custom_func):
        label = ttk.Button(parent, text=text, command=custom_func)
        label.place(relx=x_start, rely=y_start, relwidth=width, relheight=height)
