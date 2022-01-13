from random import random, randint, uniform
from Town import Town
from Monitor import Monitor
import Constants


class Simulation:
    """Runs the simulation

    """

    def __init__(self):
        self.monitor = Monitor()

    def simulate(self, num_area: int, num_healthy: int, num_sick:int, days: int):
        """ Iterates day by day and stores stats"""

        town = Town(num_area, num_healthy, num_sick)

        for day in range(days):
            print()
            print('Day ', day)
            for areas in town.list_areas:
                print(areas)

            # each day stats
            healthy = 0
            sick = 0
            recovered = 0
            dead = 0

            # updating stats
            for person in town.list_people:
                person.area.update_sick_count()
                updates = person.checkup()
                healthy += updates[0]
                sick += updates[1]
                recovered += updates[2]
                dead += updates[3]

            # recording stats
            self.monitor.notify(healthy, sick, recovered, dead, day)

            # Making people travel
            for person in town.list_people:
                if person.status != 'Dead':
                    person.travel()


if __name__ == "__main__":
    A = Simulation()
    A.simulate(Constants.NUM_AREAS, Constants.NUM_HEALTHY, Constants.NUM_SICK,
               Constants.ITERATIONS)
    A.monitor.print_represent()
    A.monitor.graph_represent()




