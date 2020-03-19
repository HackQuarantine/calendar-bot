import datetime


def check_calendar():
    now = datetime.datetime.now()
    day = int(now.strftime('%d'))
    month = int(now.strftime('%m'))
    year = int(now.strftime('%Y'))
    hour = int(now.strftime('%H'))
    minute = int(now.strftime('%M'))

    return "Title", "Description"