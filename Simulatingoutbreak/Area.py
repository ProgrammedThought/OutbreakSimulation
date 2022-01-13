from typing import List


class Area:
    """ Sets up a visitable area

    Attributes:
        area_id: unique identifier for the area
        num_sick: number of sick people in this area
    """
    area_id: int
    list_people: list

    def __init__(self, id: int):
        """ Initializes an area """
        self.area_id = id
        self.list_people = []

    def __str__(self):
        return 'Area {} with {} sick people: {}'.format(self.area_id,
                                                        self.num_sick(),
                                                        self.list_people)

    def add_person(self, person):
        if person not in self.list_people:
            self.list_people.append(person)

    def remove_person(self, person):
        self.list_people.remove(person)

    def num_sick(self):
        count = 0
        for person in self.list_people:
            if person.status == 'Sick':
                count += 1
        return count



