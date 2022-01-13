from typing import List
from random import choice
from Constants import AVERAGE_HOUSEHOLD


class House:
    """ Sets up a house where a person or a group of people live together

    Attributes:
        identity: unique identifier for the house
        capacity: number of people in the house based on AVERAGE_HOUSEHOLD
        inhabitants: list of people living in the house

    """
    identity: int
    inhabitants: list
    capacity: int

    def __init__(self, identity: int):
        """Initializes the house with a certain number of people"""
        self.identity = identity
        self.capacity = choice([x for x in range(AVERAGE_HOUSEHOLD[0],
                                                 AVERAGE_HOUSEHOLD[1])])
        self.inhabitants = []

    def __repr__(self):
        return 'House {}'.format(self.identity)

    def add_person(self, person):
        """ Adds person to inhabitants"""
        self.inhabitants.append(person)

    def remove_person(self, person):
        """ Removes person from inhabitants"""
        self.inhabitants.remove(person)

    def num_sick(self):
        count = 0
        for person in self.inhabitants:
            if person.status == 'Sick':
                count += 1
        return count
