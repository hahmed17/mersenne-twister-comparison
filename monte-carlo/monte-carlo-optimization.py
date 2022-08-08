import numpy as np
from numpy import random
import os
import sys

# Set random number seed and write to file
if os.path.isfile("seedFile.txt"):
    # If seed file already exists, read from file
    seed_file = open("seedFile.txt", "r")
    seed = int(seed_file.read())
elif not os.path.isfile("seedFile.txt") or os.stat("seedFile.txt").st_size==0:
    # If no seed file exists, generate new seed from time method
    seed = int(datetime.utcnow().timestamp())

    # Create seed file and write to file
    seed_file = open("seedFile.txt", "w")
    seed_file.write(str(seed))

seed_file.close()  # Close seed file
np.random.seed(seed)  # Set global numpy seed
np.random.MT19937(seed)

# Get state if given a state file
if os.path.isfile("stateFile.txt"):
    stateFile = open("stateFile.txt")
    state_lines = stateFile.read().split(' ')
    new_state = [int(i) for i in state_lines[:-1]]
    new_state_tuple = ('MT19937', new_state, 624, 0, 0.0)
    np.random.set_state(new_state_tuple)

# Write current state to file
state = [int(s) for s in list(np.random.get_state()[1])]
# Write numpy mt state to file
stateFile = open("stateFile.txt", 'w')
for state_int in state:       
    stateFile.write(str(state_int) + " ")


n = 100000
max_area = 0.0
max_a = 0.0

np.random.seed(23456)

for i in range(n):
    a = 100 * np.random.randint(256**4, dtype='<u4', size=1)[0] / (256**4+1)
    b = 100 - a
    area = a*b
    if (area > max_area):
        max_area = area
        max_a = a


print(max_a)
