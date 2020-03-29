class Event:

    def __init__(self, day, month, year, hour, minute, title, description, organiser_id, organiser_nick, host):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.title = title
        self.description = description
        self.organiser_id = organiser_id
        self.organiser_nick
        self.host

    def get_event_info(self):
        return self.title, self.description, self.organiser_id
    
    def get_announcement(self):
        if self.organiser_nick:
            return f"What is UP @here! We have @{self.organiser_nick} giving a talk on '{self.title}' in 10 minutes on Twitch.tv! Head over and check it out!\nhttps://hackquarantine.com/stream"
        else:
            return f"What is UP @here! We have a talk on '{self.title}' in 10 minutes on Twitch.tv! Head over and check it out!\nhttps://hackquarantine.com/stream"

    def __str__(self):
        return f"<Workshop> [{self.title}] by [id={self.organiser_id}]"
