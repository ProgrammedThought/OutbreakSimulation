from random import random, randint, uniform
from Town import Town
from Monitor import Monitor
import Constants


class Simulation:
    """
        Runs the simulation
    """

    def __init__(self):
        self.monitor = Monitor()

    def simulate(self, num_area: int, num_healthy: int, num_sick: int, days: int):
        """ Iterates day by day and stores stats"""

        town = Town(num_area, num_healthy, num_sick)

        # Initializing stats for day 0
        self.monitor.notify(num_healthy, num_sick, 0, 0, 0, 0)

        # Running simulation day by day
        for day in range(1, days):

            # Simulating Healthy people's interaction with sick
            for person in town.list_people:
                person.healthy_simulate()

            # Making people travel
            if not town.town_quarantine(self.monitor.days_history[-1].sick):
                for person in town.list_people:
                    if person.status != 'Dead':
                        person.travel()

            # simulating spread and recording stats at the end of the day
            healthy, sick, recovered, dead, travelled = self.update_stats(town)
            self.monitor.notify(healthy, sick, recovered, dead, travelled, day)

            #  To be removed   ###########
            print()
            print('Day ', day)
            for areas in town.list_areas:
                print(areas)
            print()
            print(' -  Sick people stats:')
            for person in town.list_people:
                if person.status ==  'Sick':
                    print()
                    print('{} -  Social: {}, Immunity: {}, Know sick: {}'.format(
                        Constants.NAMES[person.identity],
                        person.social, person.immunity, person.know_sick()))
                    print('Virus- ', person.virus)
                    print('House: ', person.house.inhabitants)
            ##############################

            # Returning people home
            for person in town.list_people:
                person.back_home()

    def update_stats(self, town: Town):
        """ Updates the statistics of people in a Town"""
        healthy = 0
        sick = 0
        recovered = 0
        dead = 0
        traveled = town.people_traveled()

        for person in town.list_people:
            updates = person.checkup()
            healthy += updates[0]
            sick += updates[1]
            recovered += updates[2]
            dead += updates[3]

        return healthy, sick, recovered, dead, traveled


if __name__ == "__main__":
    A = Simulation()
    A.simulate(Constants.NUM_AREAS, Constants.NUM_HEALTHY, Constants.NUM_SICK,
               Constants.ITERATIONS)
    A.monitor.print_represent()
    A.monitor.graph_represent(Constants.NUM_HEALTHY + Constants.NUM_SICK)




