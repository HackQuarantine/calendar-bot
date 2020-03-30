import datetime

class Event:

    def __init__(self):
        self.start = None
        self.title = None
        self.description = None
        self.host_discord_name = None
        self.host = None
        self.type = None

    def get_event_info(self):
        return self.title, self.description, self.organiser_id

    def get_announcement(self):
        if type == "workshop" or "talk":
            if self.host_discord_name:
                return f"What is UP @here! We have @{self.organiser_nick} giving a {self.type} on '{self.title}' in 10 minutes on Twitch.tv! Head over and check it out!\nhttps://hackquarantine.com/stream"
            elif self.host:
                return f"What is UP @here! We have {self.host} giving a {self.type} on '{self.title}' in 10 minutes on Twitch.tv! Head over and check it out!\nhttps://hackquarantine.com/stream"
            else: 
                return f"What is UP @here! We have a {self.type} on '{self.title}' in 10 minutes on Twitch.tv! Head over and check it out!\nhttps://hackquarantine.com/stream"


    def __str__(self):
        return f"<Workshop> [{self.title}] by [id={self.organiser_id}]"
