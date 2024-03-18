from participant import Participant

class Competition:
    def __init__(self, participants):
        self.participants = [Participant(**data) for data in participants]

    def sort_key(self, participant):
        return -participant.score, participant.name

    def scoreboard(self):
        # Sort participants by score and name
        self.participants.sort(key=self.sort_key)
        # Return scoreboard
        return [{'name': p.name, 'score': p.score} for p in self.participants]
