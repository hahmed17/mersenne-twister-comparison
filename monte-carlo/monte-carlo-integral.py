# importing the modules
from scipy import random
import numpy as np
from numpy import random
import os
import sys
import datetime
from datetime import datetime
import math

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

# limits of integration
a = 0
b = 1
N = 1000
  
# array of zeros of length N
ar = np.zeros(N)
  
# iterating over each Value of ar and filling
# it with a random value between the limits a 
# and b
for i in range(len(ar)):
    """randInt = np.random.randint(256**4, dtype='<u4', size=1)[0]
    randInt *= 2
    if (i < 5):
     print(randInt)

    # Divide rand in to be between 0 and 1
    div = 10**len(str(randInt))  
    ar[i] = randInt / div"""
    #ar[i] = np.random.uniform(a, b)
    ar[i] = np.random.rand()
    #ar[i] = np.random.randint(256**4, dtype='<u4', size=1)[0] / 256**4
  
# variable to store sum of the functions of 
# different values of x
integral = 0.0
  
# function to calculate the sin of a particular 
# value of x
def f(x):
    return math.exp(-x**2)
  
# iterates and sums up values of different 
# functions of x
for i in ar:
    integral += f(i)
  
# we get the answer by the formula derived adobe
ans = (b-a)/float(N)*integral
  
# prints the solution
print("The value calculated by monte carlo integration is {}.".format(ans))

outFile = open("out-py-integral.txt", 'w')
outFile.write(str(ans))