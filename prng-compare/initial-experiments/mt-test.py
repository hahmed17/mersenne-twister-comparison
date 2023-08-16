import numpy as np
import os
import random

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
random.seed(seed)

outNumpy = open("out-numpy.txt", 'w')
outNumpyUniform = open("out-np-uniform.txt", 'w')
outFile = open("out-py.txt", 'w')
outUniform = open("out-py-uniform.txt", 'w')


rand_max_file = open("RAND_MAX.txt")
RAND_MAX = int(rand_max_file.read())
for i in range(10):
    rand_int_numpy = np.random.randint(0, RAND_MAX)
    outNumpy.write("{}\n".format(rand_int_numpy))
    
    rand_int_uniform_np = np.random.uniform(0, RAND_MAX)
    outNumpyUniform.write("{}\n".format(rand_int_uniform_np))

    rand_int = random.randint(0, RAND_MAX)
    outFile.write("{}\n".format(rand_int))

    rand_int_uniform = random.uniform(0, RAND_MAX)
    outUniform.write("{}\n".format(rand_int_uniform))
