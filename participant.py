class Participant:
    def __init__(self, name, chickenwings, hamburgers, hotdogs):
        self.name = name
        self.score = chickenwings * 5 + hamburgers * 3 + hotdogs * 2
