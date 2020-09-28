import tkinter as tk
from tkinter import ttk
from tkinter import font

from MonthlyShiftTime import MonthlyShiftTime
from CommonWidgets import CommonWidgets
from ClockTimeDefine import ClockTimeDefine
from ClockTimeCombobox import ClockTimeCombobox

class ClockFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_date = parent.selected_date
        self.start_hour = ''
        self.start_minute = ''
        self.end_hour = ''
        self.end_minute = ''
        self.set_clock_elements()

    def set_clock_elements(self):
        CommonWidgets.set_label(self, 0.1, 0.2, 'Start Time : ')
        self.start_hour_combobox = ClockTimeCombobox(self, ClockTimeDefine.hour_arr, 0.4, 0.2)
        self.start_minute_combobox = ClockTimeCombobox(self, ClockTimeDefine.minute_arr, 0.6, 0.2)
        CommonWidgets.set_label(self, 0.55, 0.2, ':')

        CommonWidgets.set_label(self, 0.1, 0.4, 'End Time : ')
        self.end_hour_combobox = ClockTimeCombobox(self, ClockTimeDefine.hour_arr, 0.4, 0.4)
        self.end_minute_combobox = ClockTimeCombobox(self, ClockTimeDefine.minute_arr, 0.6, 0.4)
        CommonWidgets.set_label(self, 0.55, 0.4, ':')
        CommonWidgets.set_button(self, 0.2, 0.6, 0.15, 0.2, 'set', custom_func=self.set_time)
        CommonWidgets.set_button(self, 0.7, 0.6, 0.15, 0.2, 'reset', custom_func=self.reset_time)

    def set_time(self):
        self.start_hour = self.start_hour_combobox.get()
        self.start_minute = self.start_minute_combobox.get()
        self.end_hour = self.end_hour_combobox.get()
        self.end_minute = self.end_minute_combobox.get()
        shift_time_arr = [self.start_hour, self.start_minute, self.end_hour, self.end_minute]
        MonthlyShiftTime.update_shift_time(self.selected_date, shift_time_arr)
        print(MonthlyShiftTime.monthly_shift_time_dict)
        self.parent.parent.set_selected_date(self.selected_date)
        self.parent.destroy()

    def reset_time(self):
        MonthlyShiftTime.update_shift_time(self.selected_date, [])
        self.parent.parent.reset_selected_date(self.selected_date)
        print(MonthlyShiftTime.monthly_shift_time_dict)
