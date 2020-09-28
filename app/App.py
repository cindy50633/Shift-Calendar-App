print('Start App')

import ctypes
import pathlib
import platform
import tkinter as tk
from tkinter import ttk
from tkinter import font

from CalendarFrame import CalendarFrame


class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.script_path = self.parent.script_path
        # self.make_dpi_aware()

        self.calendar_frame = CalendarFrame(self)
        self.calendar_frame.place(relx=0, rely=0, relwidth=1, relheight=0.9)

    @staticmethod
    def make_dpi_aware():
        if int(platform.release()) >= 8:
            ctypes.windll.shcore.SetProcessDpiAwareness(True)


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)
        self.geometry('800x600')
        self.script_path = pathlib.Path(__file__).parent.absolute()
        self.main_frame = MainFrame(self)
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

if __name__ == "__main__":
    main = MainWindow()
    main.title('Shift Calendar Trial')
    main.mainloop()
