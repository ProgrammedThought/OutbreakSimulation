
# Simulation basics
NUM_HEALTHY = 10000                # 25
NUM_SICK = 50                    # 1
NUM_AREAS = 200                   # 5
ITERATIONS = 500             # 40

# Virus characteristics
DURATION_UNTIL_DEATH = 15       # 15
INFECTION_RATE = 0.01       # 0.03
INCUBATION_PERIOD = (4, 8)
SYMPTOMLESS_CHANCE = 0
LETHALITY = 0.2
RECURRENCE_TIME = (60, 80)        # days until a person can get infected again

# Community Characteristic
AVERAGE_IMMUNITY = (0.5, 1)
AVERAGE_HOUSEHOLD = (2, 6)          # Average number of people in a house
SOCIAL_RATE = 0.9              # 0.9
SOCIAL_RATE_RANGE = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
TRAVELLING_PROB = (0.6, 0.8)
SOCIAL_DISTANCE = (0.3, 0.5)
SELF_QUARANTINE = False
TOWN_QUARANTINE = (True, 6000, 30)       # (on/off, sick_benchmark, Duration_on)


# Misc
NAMES = []
with open('Names.txt', 'r') as Names:
    for line in Names.readlines():
        NAMES.append(line.strip())

"""
    New constants:
        AVERAGE_IMMUNITY
        RECURRENCE_TIME
        TOWN_QUARANTINE
        

"""
