from typing import List
from Area import Area
from Person import Person


class Town:
    """Initializes a town made up of areas with people inside

    Attributes:
        list_areas: list of areas in town
        list_people: list of people in town
        selected: flag for selected town in simulation or not
    """
    list_areas: List[Area]
    list_people: List[Person]
    selected: bool

    def __init__(self, num_areas: int, num_healthy:int, num_sick: int) -> None:
        """ Initializes a town with certain number of areas and a specific
         number of sick and healthy people"""

        self.list_areas = [Area(i) for i in range(num_areas)]

        self.list_people = []
        identity = 0
        for num in range(num_healthy):
            identity += 1
            self.list_people.append(Person(identity, 'Healthy', self.list_areas))
        for num in range(1, num_sick + 1):
            identity += 1
            self.list_people.append(Person(identity, 'Sick', self.list_areas))

        self.selected = False


