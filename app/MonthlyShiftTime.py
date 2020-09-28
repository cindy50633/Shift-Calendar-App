class MonthlyShiftTime():
    monthly_shift_time_dict = {}

    @classmethod
    def update_shift_time(cls, shift_date, shift_time_arr):
        cls.monthly_shift_time_dict[shift_date] = shift_time_arr
