from typing import List
from Area import Area
from Person import Person
from House import House
from Constants import TOWN_QUARANTINE


class Town:
    """Initializes a town made up of areas, people and houses

    Attributes:
        list_areas: list of areas in town
        list_people: list of people in town
        list_houses: list of houses
        quarantine: if town quarantine is set True
        quaratine_duration: the number of days a quarantine has been on
        selected: flag for selected town in simulation or not
    """
    list_areas: List[Area]
    list_people: List[Person]
    list_houses: List[House]
    quarantine: bool
    quarantine_duration: int
    selected: bool

    def __init__(self, num_areas: int, num_healthy:int, num_sick: int) -> None:
        """ Initializes a town with certain number of areas and a specific
         number of sick and healthy people"""

        # set-up Areas
        self.list_areas = [Area(i) for i in range(num_areas)]

        # set-up first
        self.list_houses = [House(0)]

        # set-up people
        self.list_people = []
        identity = 0
        for num in range(num_healthy):
            identity += 1
            self.list_people.append(Person(identity, 'Healthy', self))
        for num in range(1, num_sick + 1):
            identity += 1
            self.list_people.append(Person(identity, 'Sick', self))

        self.quarantine = False
        self.quarantine_duration = 0

        self.selected = False    # For future implementation with more towns

    def town_quarantine(self, sick: int) -> bool:
        """Checks if town quarantines it's people and flags true when sick_count
        increases quarantine benchmark

        TOWN_QUARANTINE[0] : Quarantine on/off
        TOWN_QUARANTINE[1] : Quarantine sick Benchmark
        TOWN_QUARANTINE[2] : Quarantine duration
        """
        # if Quarantine on
        if TOWN_QUARANTINE[0]:
            # if time span set
            if TOWN_QUARANTINE[2]:
                # if quarantine on time span not exceeded
                if self.quarantine and self.quarantine_duration < TOWN_QUARANTINE[2]:
                    self.quarantine_duration += 1
                    return True
                elif self.quarantine_duration >= TOWN_QUARANTINE[2]:
                    self.quarantine = False
                    self.quarantine_duration = 0
                    return False
                elif sick >= TOWN_QUARANTINE[1]:
                    self.quarantine = True
                    self.quarantine_duration += 1
                    return True
            elif sick >= TOWN_QUARANTINE[1]:
                return True
        return False

    def people_traveled(self):
        total = 0
        for area in self.list_areas:
            total += len(area.list_people)
        return total

