import numpy as np
from numpy import random
import os
import sys
import datetime 
from datetime import datetime

INTERVAL = 1000

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
sameState = sys.argv[1]

sameState = int(sys.argv[1])
if (sameState == 1):
    print("New state given.")
    stateFile = open("stateFile.txt", 'r')
    state_lines = stateFile.read().split(' ')
    new_state = [int(i) for i in state_lines[:-1]]
    new_state_tuple = ('MT19937', new_state, 624, 0, 0.0)
    np.random.set_state(new_state_tuple)
    stateFile.close()
elif (sameState == 0):
    print("No PRNG state given.")
    state = [int(s) for s in list(np.random.get_state()[1])]
    stateFile = open("stateFile.txt", 'w')
    for i in state:
        stateFile.write("{} ".format(i))
    stateFile.close()



circle_points = 0
square_points = 0

# Total Random numbers generated= possible x
# values* possible y values

for i in range(INTERVAL**2):

	# Randomly generated x and y values from a
	# uniform distribution
	# Range of x and y values is -1 to 1
	if (sameState == 1):
		rand_x = (np.random.randint(0,256**4, dtype='<u4', size=1)[0] % (INTERVAL + 1)) / INTERVAL
		rand_y = (np.random.randint(0,256**4, dtype='<u4', size=1)[0] % (INTERVAL + 1)) / INTERVAL
	elif (sameState == 0):
		rand_x = (np.random.randint(0,256**4) % (INTERVAL + 1)) / INTERVAL
		rand_y = (np.random.randint(0,256**4) % (INTERVAL + 1)) / INTERVAL
	#if (i <=5): print(np.random.randint(256**4, dtype='<u4', size=1)[0])
	#if (i <=5): print(rand_x, rand_y)

	# Distance between (x, y) from the origin
	origin_dist = rand_x**2 + rand_y**2

	# Checking if (x, y) lies inside the circle
	if origin_dist <= 1:
		circle_points += 1

	square_points += 1

	# Estimating value of pi,
	# pi= 4*(no. of points generated inside the
	# circle)/ (no. of points generated inside the square)
	pi = 4 * circle_points / square_points

## print(rand_x, rand_y, circle_points, square_points, "-", pi)
# print("\n")

print("Final Estimation of Pi=", pi)

if (sameState == 1):
	outFile = open("out-py-estimate-sameState.txt", 'w')
elif (sameState == 0):
	outFile = open("out-py-estimate-sameSeed.txt", 'w')
outFile.write(str(pi))
