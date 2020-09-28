print(__package__)
import os
import tkinter as tk
import tkcalendar
from tkinter import ttk
from tkinter import font

from ClockTimeDefine import ClockTimeDefine

class ClockTimeCombobox(ttk.Combobox):
    def __init__(self, parent, options_arr, x_start, y_start, *args, **kwargs):
        ttk.Combobox.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.options_arr = options_arr

        self.set_options()
        self.set_default()
        self.set_place(x_start, y_start)

    def set_options(self):
        self['values'] = self.options_arr

    def set_default(self):
        self.set(self.options_arr[0])

    def set_place(self, x_start, y_start):
        self.place(relx=x_start, rely=y_start, relwidth=0.12, relheight=0.1)
