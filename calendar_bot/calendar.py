import datetime
import dateutil.parser
import requests
import pprint
from . import event
from . import config
from calendar_bot.logging import logger

def check_calendar():
    now = datetime.datetime.now()
    day = int(now.strftime('%d'))
    month = int(now.strftime('%m'))
    year = int(now.strftime('%Y'))
    hour = int(now.strftime('%H'))
    minute = int(now.strftime('%M'))
    cal_event = get_next_event()

    if day == cal_event.day and month == cal_event.month and year == cal_event.year:

        if abs(hour - cal_event.hour) <= 1 and abs(minute - cal_event.minute) == 10:
            cal_event.announcement = True
    return cal_event


def get_all_events():
    id = config.creds['calendar']['id']
    key = config.creds['calendar']['token']
    logger.debug(f"Fetching events from '{id}'")
    r = requests.get(
        f'https://www.googleapis.com/calendar/v3/calendars/{id}/events?key={key}')
    #pprint.pprint(r.json()['items'])
    return r.json()

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

    try:
        events = get_all_events()['items']
    except:
        pass
        logger.warning("Cannot fetch events from calendar/malformed response")
    now = datetime.datetime()

    ## sort calendar

    next_event = {}
    for event in events:

        try:
            meta = json.loads(event['description'])
        except:
            bad_events += 1
            logger.warning(
                f" - Malformed JSON in event '{event['summary']}' on '{event['start']['dateTime']}'")
            continue
        try:
            start = dateutil.parser.parse(event['start']['dateTime'])
            print(start)
        except:
            logger.warning("F")
        if start < now:
            # Do stuff with it

            event.organiser_id = meta['organiser_id']
            event.organiser_name = meta['organiser']
            pass


    
    cal_event = event.Event(day, month, year, hour, minute, title, description, organiser_id)
    
    return cal_event
