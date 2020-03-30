import datetime
import random
import calendar_bot.setup

class Event:

    def __init__(self):
        self.start = None
        self.title = None
        self.description = None
        self.organiser_id = None
        self.organiser_discord_name = None
        self.organiser = None
        self.type = None

    def get_event_info(self):
        return self.title, self.description, self.organiser_id


    def get_announcement(self):
        if type == "workshop" or "talk":
            if self.organiser_discord_name:
                return f"Hey @here! We have @{self.organiser_nick} giving a {self.type} on '{self.title}' in 10 minutes on Twitch.tv! Head over and check it out!\nhttps://hackquarantine.com/stream"
            elif self.organiser:
                return f"{self.get_message_start()} We have {self.organiser} giving a {self.type} on '{self.title}' in 10 minutes on `Twitch.tv`! Head over and check it out!\nhttps://hackquarantine.com/stream"
            else: 
                return f"Hey @here! We have a {self.type} on '{self.title}' in 10 minutes on Twitch.tv!\n\nHead over and check it out!\n\nhttps://hackquarantine.com/stream"

    def get_discord_nick(self):
        self.organiser_discord_name = bot.get_guild(config.creds['guild_id']).get_member(int(self.organiser_id))

    def get_message_start(self):
        random_num = random.randint(1, 5)

        if random_num == 1:
            return "Hey @here!"
        elif random_num == 2:
            return "What's up in @here!"
        elif random_num == 3:
            return "Hello @here!"
        elif random_num == 4:
            return "How are we all doing in @here?"
        elif random_num == 5:
            return "Yo yo yo @here!"        

    def __str__(self):
        return f"<Workshop> [{self.title}] by [id={self.organiser_id}]"
