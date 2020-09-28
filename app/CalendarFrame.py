print(__package__)


import os
import tkinter as tk
import tkcalendar
from datetime import datetime
from tkinter import ttk
from tkinter import font

from ClockWindow import ClockWindow

class CalendarFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.shift_calendar = self.start_calendar()
        self.shift_calendar.tag_config('on_select', background='blue', foreground='white')
        self.shift_calendar.tag_config('selected', background='green', foreground='white')
        # self.shift_calendar.bind("<<DateEntrySelected>>", print_sel)

    def start_calendar(self):
        def __select_date(event):
            # w = event.widget
            # date = w.get_date()
            # print('Selected Date:{}'.format(date))
            # <ref to Calendar>.calevent_create(date, 'Hello ...`)
            # cal.calevent_create(date, 'Hello ...')
            print('hihi')
            selected_date = self.shift_calendar.get_date()
            print(selected_date)
            selected_date = datetime.strptime(selected_date, '%m/%d/%y').date()
            print(selected_date)
            self.on_select(selected_date)

        shift_calendar = tkcalendar.Calendar(self, selectmode='day', year=2020, month=9, day=27)
        # shift_calendar.place(relx=0, rely=0, relwidth=1, relheight=1)
        shift_calendar.pack(fill='both', expand=True)
        shift_calendar.bind('<<CalendarSelected>>', __select_date)
        return shift_calendar

    def on_select(self, selected_date):
        # id = self.shift_calendar.calevent_create(selected_date, 'Selected Date', 'selected')
        # self.shift_calendar.calevent_create(selected_date, 'Selecting', 'on_select')
        ClockWindow(self, selected_date)

    def set_selected_date(self, selected_date):
        id = self.shift_calendar.calevent_create(selected_date, 'Selected Date', 'selected')
        print('id = '+ str(id))
        print(self.shift_calendar.get_calevents(date=selected_date, tag='selected'))
        return id

    def reset_selected_date(self, selected_date):
        print('in reset')
        print(self.shift_calendar.get_calevents(date=selected_date, tag='selected'))
        self.shift_calendar.calevent_remove(date=selected_date, tag='selected')
