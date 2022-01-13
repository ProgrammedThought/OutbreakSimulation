from typing import List, Tuple, Optional
from random import uniform, randint, random, choice
from Area import Area
from Virus import Virus
from House import House
import Constants


class Person:
    """Sets up a person

    Attributes:
        status: Can be one of four things: Healthy, Sick, Recovered or Dead
        sick_duration: number of days a person has been sick
        area : Area they are currently in
        immunity: represents how well they can avoid getting infected
        virus: a virus strand if they are infected
        social: social rate of this person which makes him travel
    """
    identity: int
    status: str
    sick_duration: int
    area: Optional[Area]
    immunity: float
    virus: Optional[Virus]

    def __init__(self, identity: int,  status: str, town):
        """ Initializes Person class"""

        self.identity = identity

        # set-up virus
        self.status = status
        if self.status == 'Sick':
            self.virus = Virus()
        else:
            self.virus = None
        self.sick_duration = 0

        # set-up house
        self.house = None
        while not self.house:
            house = town.list_houses[-1]
            if len(house.inhabitants) >= house.capacity:
                index = house.identity + 1
                house = House(index)
                town.list_houses.append(house)
            self.house = house
            house.add_person(self)

        self.town = town
        self.list_areas = town.list_areas
        self.area = None

        # Check if recurrence is True and set time
        time = Constants.RECURRENCE_TIME
        if time:
            rec =[x for x in range(time[0], time[1])]
            self.recurrence = choice(rec)
        else:
            self.recurrence = False

        self.recovered_duration = 0
        self.immunity = uniform(Constants.AVERAGE_IMMUNITY[0],
                                Constants.AVERAGE_IMMUNITY[1])
        self.social = choice(Constants.SOCIAL_RATE_RANGE)

    def __repr__(self):
        return '{} is {}'.format(Constants.NAMES[self.identity], self.status)

    def infected(self):
        """ Sets status of person to sick, increments number of sick people in
        the area and the sick duration of the person"""
        self.status = 'Sick'
        self.virus = Virus()

    def sick(self) -> Tuple[int, int, int]:
        """Checks how long the person has remained sick and updates the person
        as dead with the probability DEATH_PROBABILITY, if he's been sick longer
        then DURATION_UNTIL_DEATH. If death is not probable then he recovers. If
        the person has been sick less than DURATION_UNTIL_DEATH then the sick
        count updates"""

        sick = 0
        dead = 0
        recovered = 0

        if self.virus.cycle_complete(self.sick_duration):
            if self.virus.lethal:
                self.status = 'Dead'
                dead = 1
            else:
                self.status = 'Recovered'
                recovered = 1
        else:
            sick += 1
            self.sick_duration += 1
        return sick, recovered, dead

    def healthy_simulate(self):
        """Only simulates healthy people without returning any stats and without
        considering the fact that one day has passed. (This is important as the
        sick_duration and other factors that one complete iteration changes are
        unchanged)"""

        # checks location
        if self.area:
            place = self.area
        else:
            place = self.house
        num_sick = place.num_sick()
        infec_chance = Constants.INFECTION_RATE * num_sick
        # infection_chance considers a person's immunity
        infection_chance = ((2 / 3) * infec_chance) + \
                           ((1 / 3) * (infec_chance * (1 - self.immunity)))

        if (num_sick > 0) and (random() <= infection_chance):
            self.infected()

    def healthy(self) -> Tuple[int, int]:
        """The Get Sick Function:
        Checks whether a healthy person has been surrounded by enough sick
        people to get infected himself based on his immunity
        """

        healthy = 0
        sick = 0
        if self.area:
            place = self.area
        else:
            place = self.house
        num_sick = place.num_sick()
        infec_chance = Constants.INFECTION_RATE * num_sick
        infection_chance = ((2 / 3) * infec_chance) + \
                           ((1 / 3) * (infec_chance * (1 - self.immunity)))
        # TODO take immunity to recovered
        if (num_sick > 0) and (random() <= infection_chance):
            self.infected()
            sick = 1
        else:
            healthy = 1
        return healthy, sick

    def recovered(self):
        if self.recovered_duration and self.recovered_duration < self.recurrence:
            self.status = 'Healthy'
            self.sick_duration = 0
            self.recovered_duration = 0
        else:
            self.recovered_duration += 1

    def travel(self):
        """Makes people travel random areas based on the Social_Rate and their
        quarantine status. Quarantine is based on if the community follows self
        quarantine and the person shows symptoms. This function also, adds and
         removes people from that area accordingly"""

        if random() <= self.social and not self.quarantine() and\
                not self.status == "Dead":
            if self.area:
                self.area.remove_person(self)
            self.area = self.list_areas[randint(0, len(self.list_areas) - 1)]
            self.area.add_person(self)

    def quarantine(self):
        return Constants.SELF_QUARANTINE and self.know_sick()

    def back_home(self):
        """At the end of the day, people leave areas and return home"""
        if self.area:
            self.area.remove_person(self)
            self.area = None

    def know_sick(self):
        """Returns true if incubation period has passed so symptoms are showing
        and so the person knows they're sick and would act accordingly ex. not
        travel"""

        if self.status == 'Sick' and self.virus.has_symptoms(self.sick_duration):
            return True
        return False

    def checkup(self):
        """Everyday checkup that records the status of the person and updates it
        according to their circumstances in the function utilized within"""
        healthy = 0
        sick = 0
        recovered = 0
        dead = 0

        if self.status == 'Healthy':
            healthy, sick = self.healthy()
        elif self.status == 'Sick':
            sick, recovered, dead = self.sick()
        elif self.status == 'Recovered':
            recovered = 1
            self.recovered()
        else:
            dead = 1
        return healthy, sick, recovered, dead

    def update_count(self):
        """Just returns the count based on person's status"""
        healthy = 0
        sick = 0
        recovered = 0
        dead = 0

        if self.status == 'Healthy':
            healthy = 1
        elif self.status == 'Sick':
            sick = 1
        elif self.status == 'Recovered':
            recovered = 1
        elif self.status == 'Dead':
            dead = 1
        return healthy, sick, recovered, dead
