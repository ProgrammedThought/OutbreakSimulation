
# Simulation basics
NUM_HEALTHY = 25                # 25
NUM_SICK = 1                    # 1
NUM_AREAS = 5                   # 5
ITERATIONS = 80              # 40

# Virus characteristics
DURATION_UNTIL_DEATH = 15       # 15
INFECTION_RATE = 0.07           # 0.008
INCUBATION_PERIOD = (4, 8)
SYMPTOMLESS_CHANCE = 0
LETHALITY = 0.2
RECURRENCE_TIME = None #(60, 80)        # days until a person gets infected again


# Community Characteristic
AVERAGE_IMMUNITY = (0.5, 1)
AVERAGE_HOUSEHOLD = (2, 6)          # Average number of people in a house
SOCIAL_RATE = 0.9              # 0.9
SOCIAL_RATE_RANGE = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
TRAVELLING_PROB = (0.6, 0.8)
SOCIAL_DISTANCE = (0.3, 0.5)
SELF_QUARANTINE = True
TOWN_QUARANTINE = (False, 6000,30)       # (on/off, sick_benchmark, Duration_on)


# Misc
NAMES = []
with open('Names.txt', 'r') as Names:
    for line in Names.readlines():
        NAMES.append(line.strip())
