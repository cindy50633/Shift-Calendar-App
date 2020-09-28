print('Start Time Window')

import platform
import tkinter as tk
from tkinter import ttk
from tkinter import font

from ClockFrame import ClockFrame


class ClockWindow(tk.Toplevel):
    def __init__(self, parent, selected_date, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_date = selected_date
        self.geometry('350x150')
        self.clock_frame = ClockFrame(self)
        self.clock_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        # self.transient(root)
        # print(root)

# if __name__ == "__main__":
#     main = ClockWindow()
#     main.title('Shift Clock')
#     main.mainloop()
