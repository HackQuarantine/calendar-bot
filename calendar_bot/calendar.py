import datetime
import dateutil.parser
import pytz
import requests
import pprint
import json
from .event import Event
from . import config
from calendar_bot.logging import logger


def get_next_event(now, skip):
    now = datetime.datetime.now()
    try:
        events = get_all_events()['items']
    except:
        logger.warning("Cannot fetch events from calendar/malformed response")
    sorted_events = sort_calendar(events)
    cal_event = Event()

    if skip:
        next_event = sorted_events[1]
    else:
        next_event = sorted_events[0]

    try:
        meta = json.loads(next_event['description'])
    except:
        logger.warning(
            f" - Malformed JSON in event '{next_event['summary']}' on '{next_event['start']['dateTime']}'")
    try:
        cal_event.start = dateutil.parser.parse(
            next_event['start']['dateTime'])
        cal_event.title = next_event['summary']
        cal_event.description = meta['description']
        cal_event.organiser_id = ''
        cal_event.organiser = meta['organiser']
        cal_event.type = meta['type']
    except:
        logger.warning(
            f" - Missing required JSON fields in event '{next_event['summary']}' on '{next_event['start']['dateTime']}'")
    return cal_event


def get_all_events():
    id = config.creds['calendar']['id']
    key = config.creds['calendar']['token']
    r = requests.get(
        f'https://www.googleapis.com/calendar/v3/calendars/{id}/events?key={key}')
    return r.json()

def sort_calendar(events):
    utc = pytz.UTC
    now = datetime.datetime.now()

    sorted_events = sorted(events, key=lambda x:dateutil.parser.parse(x['start']['dateTime']))
    for event in events:
        start = dateutil.parser.parse(event['start']['dateTime'])
        if start.replace(tzinfo=utc) < now.replace(tzinfo=utc):
            sorted_events.remove(event)

    return sorted_events
