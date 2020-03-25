import datetime
from . import event

def check_calendar():
    now = datetime.datetime.now()
    day = int(now.strftime('%d'))
    month = int(now.strftime('%m'))
    year = int(now.strftime('%Y'))
    hour = int(now.strftime('%H'))
    minute = int(now.strftime('%M'))
    cal_event = get_next_event()

    if day == cal_event.day and month == cal_event.month and year == cal_event.year:

        if abs(hour - cal_event.hour) == 1 and abs(minute - cal_event.minute) == 0:
            cal_event.send_token = True
        elif abs(hour - cal_event.hour) <= 1 and abs(minute - cal_event.minute) == 30:
            cal_event.host_reminder = True
            cal_event.announcement = True

        elif abs(hour - cal_event.hour) <=1 and abs(minute - cal_event.minute) == 10:
            cal_event.announcement = True
    return cal_event


def get_next_event():
    # google calendar part
    day = ""
    month = ""
    year = ""
    hour = ""
    minute = ""
    title = ""
    description = ""
    organiser_id = 0
    
    cal_event = event.Event(day, month, year, hour, minute, title, description, organiser_id)
    
    return cal_event
