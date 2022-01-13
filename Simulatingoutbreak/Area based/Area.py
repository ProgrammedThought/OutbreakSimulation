from typing import List


class Area:
    """ Sets up a visitable area

    Attributes:
        area_id: unique identifier for the area
        num_sick: number of sick people in this area
    """
    area_id: int
    num_sick: int
    list_people: list

    def __init__(self, id: int):
        """ Initializes an area """
        self.area_id = id
        self.list_people = []
        self.num_sick = 0

    def __str__(self):
        return 'Area {} with {} sick people: {}'.format(self.area_id,
                                                        self.num_sick,
                                                        self.list_people)

    def add_person(self, person):
        if person not in self.list_people:
            self.list_people.append(person)
            self.update_sick_count()

    def remove_person(self, person):
        self.list_people.remove(person)
        self.update_sick_count()

    def update_sick_count(self):
        count = 0
        for person in self.list_people:
            if person.status == 'Sick':
                count += 1
        self.num_sick = count



