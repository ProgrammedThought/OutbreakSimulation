
# Simulation basics
NUM_HEALTHY = 25                # 25
NUM_SICK = 1                    # 1
NUM_AREAS = 5                   # 5
ITERATIONS = 40                 # 40

# Virus characteristics
DURATION_UNTIL_DEATH = 15       # 15
INFECTION_RATE = 0.09           # 0.008
INCUBATION_PERIOD = (1, 1)
SYMPTOMLESS_CHANCE = 0
LETHALITY = 0.2

# Community Characteristic
SOCIAL_RATE = 0.9              # 0.9
SOCIAL_RATE_RANGE = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
TRAVELLING_PROB = (0.6, 0.8)
SOCIAL_DISTANCE = (0.3, 0.5)
SELF_QUARANTINE = True


# Misc
NAMES = []
with open('Names.txt', 'r') as Names:
    for line in Names.readlines():
        NAMES.append(line.strip())
