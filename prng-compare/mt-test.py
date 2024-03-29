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
if (sys.argv[1] != "null"):
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
random.seed(seed)




# Initialize and seed numpy mt generator
np.random.MT19937(seed)

if (int(sys.argv[2]) == 1):
    sameState = int(sys.argv[2])
else:
    sameState = 0

if (sameState == 1):
    if os.path.isfile("stateFile.txt"):
        stateFile = open("stateFile.txt")
        state_lines = stateFile.read().split(' ')
        state = [int(i) for i in state_lines[:-1]]
        np_state = ('MT19937', state, 624, 0, 0.0)
        np.random.set_state(np_state)
    else:
        state = [int(s) for s in list(np.random.get_state()[1])]
        np_state = ('MT19937', state, 624, 0, 0.0)
        # Write numpy mt state to file
        stateFile = open("stateFile.txt", 'w')
        for state_int in state:       
            stateFile.write(str(state_int) + " ")

    # Set random library state the same as numpy
    state.append(624)
    state = tuple(state)
    state = (3, tuple(state), None)
    random.setstate(state)


# Numpy output files
outNumpy = open("out-numpy.txt", 'w')
outNpFloat = open("out-np-float.txt", 'w')
#outNumpyUniform = open("out-np-uniform.txt", 'w')

# Random library output files
outFile = open("out-py.txt", 'w')
outFloat = open("out-py-float.txt", 'w')
outUniform = open("out-py-uni.txt", 'w')

# Get maximum random value
rand_max_file = open("../../RAND_MAX.txt")
RAND_MAX = int(rand_max_file.read())


for i in range(10):
    # Test random floats
    rand_float_np = np.random.rand()
    outNpFloat.write("{}\n".format(rand_float_np))

np.random.seed(seed) 
if (sameState == 1): 
    np.random.set_state(np_state)
for i in range(10):
    rand_uni_np = np.random.uniform(0,1)
    outUniform.write("{}\n".format(rand_uni_np))

random.seed(seed) 
if (sameState == 1): random.setstate(state)
for i in range(10):
    rand_float = random.random()
    outFloat.write("{}\n".format(rand_float))



# Set seed for numpy and random libraries
np.random.seed(seed) 
if (sameState == 1): 
    np.random.set_state(np_state)
for i in range(10):
    # Test randint
    #rand_int_numpy = np.random.randint(256**4, dtype='<u4')
    rand_int_numpy = np.random.randint(256**4)
    outNumpy.write("{}\n".format(rand_int_numpy))

random.seed(seed) 
if (sameState == 1): random.setstate(state)
for i in range(10):
    rand_int = random.randint(0, 256**4-1)
    outFile.write("{}\n".format(rand_int))


