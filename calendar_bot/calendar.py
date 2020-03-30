import datetime
import dateutil.parser
import requests
import pprint
from .event import Event
from . import config
from calendar_bot.logging import logger


def get_next_event(now):
    now = datetime.datetime.now()
    try:
        events = get_all_events()['items']
    except:
        logger.warning("Cannot fetch events from calendar/malformed response")

    ## sort calendar
    cal_event = Event()
    next_event = {}

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
        cal_event.organiser_id = meta['organiser_id']
        cal_event.organiser_name = meta['organiser']
        cal_event.type = meta['type']
    except:
        logger.warning(
            f" - Missing required JSON fields in event '{next_event['summary']}' on '{next_event['start']['dateTime']}'")

    return cal_event


def get_all_events():
    id = config.creds['calendar']['id']
    key = config.creds['calendar']['token']
    logger.debug(f"Fetching events from '{id}'")
    r = requests.get(
        f'https://www.googleapis.com/calendar/v3/calendars/{id}/events?key={key}')
    #pprint.pprint(r.json()['items'])
    return r.json()

def sort_calendar():
    pass
