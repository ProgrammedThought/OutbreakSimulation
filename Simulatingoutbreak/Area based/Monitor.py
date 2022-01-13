from typing import List
from matplotlib import pyplot as plt


class Day:
    """ Stores data recorded in a single day in a town
    """

    def __init__(self, num_healthy: int, num_sick: int, num_recovered: int,
                 num_dead: int, day: int):
        self.healthy = num_healthy
        self.sick = num_sick
        self.recovered = num_recovered
        self.dead = num_dead
        self.day = day


class Monitor:
    """ Records data in our simulation

    Attributes:
        Days_history: list of all days with thier stats
        healthy_history: number of healthy at the start
        sick_history: number if sick people at the start
        recovered: number of recovered people at the end
        dead: number of dead people at the end
        """
    days_history: List[Day]

    def __init__(self):
        """ Initializes our monitor class"""
        self.days_history = []

    def notify(self, num_healthy: int, num_sick: int, num_recovered: int,
               num_dead: int, day: int):
        self.days_history.append(Day(num_healthy, num_sick, num_recovered,
                                     num_dead, day))

    def print_represent(self):
        healthy = 0
        sick = 0
        recovered = 0
        dead = 0

        for day in self.days_history:
            healthy += day.healthy
            sick += day.sick
            recovered += day.recovered
            dead += day.dead
            print()
            print('Day ', day.day)
            print('Healthy: {}, Sick: {}, Recovered: {}, Dead: {}'.format(
                day.healthy, day.sick, day.recovered, day.dead))

    def create_lists(self):
        healthy_list = []
        sick_list = []
        recovered_list = []
        dead_list = []
        days_list = [x for x in range(1, len(self.days_history) + 1)]

        for day in self.days_history:
            healthy_list.append(day.healthy)
            sick_list.append(day.sick)
            recovered_list.append(day.recovered)
            dead_list.append(day.dead)
        return healthy_list, sick_list, recovered_list, dead_list, days_list

    def graph_represent(self):
        healthy, sick, recovered, dead, days = self.create_lists()
        fig, axs = plt.subplots(4, sharex=True, sharey=False)
        fig.suptitle('Virus Simulation')
        axs[0].plot(days, healthy)
        axs[0].set_title('Healthy')
        axs[1].plot(days, sick, 'tab:orange')
        axs[1].set_title('Sick')
        axs[2].plot(days, recovered, 'tab:green')
        axs[2].set_title('Recovered')
        axs[3].plot(days, dead, 'tab:red')
        axs[3].set_title('Dead')

        plt.show()


