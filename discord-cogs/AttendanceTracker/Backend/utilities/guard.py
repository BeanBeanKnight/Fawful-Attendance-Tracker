from AttendanceTracker.Backend.helpers.string_helper import convert_to_discord_user
from AttendanceTracker.Backend.utilities.message_reader import MessageReader


class Guard:
    def __init__(self, message_reader=MessageReader()):
        self.message_reader = message_reader

    def against_self_plus_plus(self, target_user, message_author):
        formatted_author = f"{convert_to_discord_user(message_author)}>"
        if formatted_author == target_user:
            return "You silly goose you can't updoot yourself o_O"
        else:
            return None
