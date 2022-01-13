import Constants
from random import choice, random


class Virus:
    """ A class that contains a virus that goes through an incubation period and
    develops itself with or without symptoms and dies after a certain period of
     time"""

    def __init__(self):
        """ Initializes Virus"""
        time = Constants.INCUBATION_PERIOD
        self.active = True
        self.incubation_time = choice([x for x in range(time[0], time[1] + 1)])
        self.symptoms = random() > Constants.SYMPTOMLESS_CHANCE
        self.virus_duration = Constants.DURATION_UNTIL_DEATH
        self.lethal = random() <= Constants.LETHALITY

    def has_symptoms(self, sick_duration: int):
        if sick_duration >= self.incubation_time and self.symptoms:
            return True
        return False

    def cycle_complete(self, sick_duration: int):
        """ Ends virus. Return true if person dies and false if he recovers"""
        if sick_duration >= self.virus_duration:
            self.active = False
            return True
        return False

