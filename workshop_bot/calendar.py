import datetime


def check_calendar():
    now = datetime.datetime.now()
    day = int(now.strftime('%d'))
    month = int(now.strftime('%m'))
    year = int(now.strftime('%Y'))
    hour = int(now.strftime('%H'))
    minute = int(now.strftime('%M'))

    cal_day, cal_month, cal_year, cal_hour, cal_minute = get_next_event()

    return "Title", "Description"

def get_next_event():

    return day, month, year, hour, minute