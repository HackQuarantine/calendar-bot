class Event:

    def __init__(self, day, month, year, hour, minute, title, description, organiser_id):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.title = title
        self.description = description
        self.organiser_id = organiser_id
        self.announcement = False
        self.send_token = False
        self.host_reminder = False

    def get_event_info(self):
        return self.title, self.description, self.organiser_id
