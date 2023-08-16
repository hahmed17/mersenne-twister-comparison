import numpy as np
from numpy.random import MT19937, SeedSequence
import os
import random
import datetime
from datetime import datetime
from pandas import UInt32Dtype
import sys
import os

# Set random number seed and write to file
if len(sys.argv) > 1:
    seed = int(sys.argv[1])
    seed_file = open("seedFile.txt", "w")
    seed_file.write(str(seed))
elif os.path.isfile("seedFile.txt"):
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

# Set seed for numpy and random libraries
np.random.seed(seed)  # Set global numpy seed


<<<<<<< HEAD
=======
# Initialize and seed numpy mt generator
np.random.MT19937(seed)

>>>>>>> 4a502d889508883406676f58bd6b49cac7383bd8
if os.path.isfile("stateFile.txt"):
    stateFile = open("stateFile.txt")
    state_lines = stateFile.read().split(' ')
    new_state = [int(i) for i in state_lines[:-1]]
    new_state_tuple = ('MT19937', new_state, 624, 0, 0.0)
    np.random.set_state(new_state_tuple)


state = [int(s) for s in list(np.random.get_state()[1])]
# Write numpy mt state to file
stateFile = open("stateFile.txt", 'w')
for state_int in state:       
    stateFile.write(str(state_int) + " ")

<<<<<<< HEAD
stateFile.close()

for i in range(5):
    print(np.random.rand())

np.random.seed(seed)
np.random.set_state(('MT19937', state, 0, 0, 0.0))
for i in range(5):
    print(np.random.uniform(0,1,size=1))
=======
for i in range(5):
    print(np.random.rand())

np.random.seed()
np.random.set_state(('MT19937', state, 0, 0, 0.0))
for i in range(5):
    print(np.random.uniform(0,1,size=1))
>>>>>>> 4a502d889508883406676f58bd6b49cac7383bd8
