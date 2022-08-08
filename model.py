from sklearn import cluster
from kmeans import *

import random
import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, fetch_openml
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics.cluster import homogeneity_score
from sklearn.model_selection import train_test_split
import scipy
from scipy.stats import pearsonr
import itertools as iter
import datetime
from datetime import datetime
import sys
import os
import warnings
from numpy import genfromtxt
warnings.filterwarnings('ignore')


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

# Get state if given a state file
if os.path.isfile("stateFile.txt") and not os.path.isfile("seedFile.txt"):
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


# Set random library state the same as numpy
state.append(624)
state = tuple(state)
state = (3, tuple(state), None)
random.setstate(state)



DATASET = sys.argv[1]
NUM_CLUSTERS = int(sys.argv[2])
CPP_REPRODUCE = int(sys.argv[3])


### LOAD DATA SET
if DATASET == 'pima-indians-diabetes':
    X, y = fetch_openml(name='Pima-Indians-Diabetes', return_X_y=True)
    feature_names = fetch_openml(name='Pima-Indians-Diabetes').feature_names
elif DATASET == 'iris':
    X, y = load_iris(return_X_y=True)
    feature_names = load_iris().feature_names

    # Convert to .csv file
    """iris = load_iris()
    iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names']+['target'])
    iris_df.to_csv('iris.csv', header=None, index=None)"""
elif DATASET == 'wbc':
    X, y = load_breast_cancer(return_X_y=True)
    feature_names = load_breast_cancer().feature_names
elif DATASET == 'wine':
    X, y = load_wine(return_X_y=True)
    feature_names = load_wine().feature_names
elif DATASET == 'heart-disease':
    X, y = fetch_openml(name='Heart-Disease-Dataset-(Comprehensive)', return_X_y=True)
    feature_names = fetch_openml(name='Heart-Disease-Dataset-(Comprehensive)').feature_names
else:
    print("Enter a valid numeric data set.")
    exit(0)


### RANDOMLY SPLIT DATA INTO TRAINING AND TESTING
"""X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.7, random_state=seed)

# Write each data set to files
X_train_df = pd.DataFrame(X_train)
X_test_df = pd.DataFrame(X_test)
y_train_df = pd.DataFrame(y_train)
y_test_df = pd.DataFrame(y_test)

X_train_df.to_csv('datasets/X_train.csv', header=None, index=None)
X_test_df.to_csv('datasets/X_test.csv', header=None, index=None)
y_train_df.to_csv('datasets/y_train.csv', header=None, index=None)
y_test_df.to_csv('datasets/y_test.csv', header=None, index=None)"""

X_test = genfromtxt('datasets/X_test.csv', delimiter=',')
y_test = genfromtxt('datasets/y_test.csv', delimiter=',')

# FIT KMEANS AND RETURN LABELS
if (CPP_REPRODUCE == 0):
    centroids, clusterAssignments = kMeans(dataSet=X_test, k=NUM_CLUSTERS, random_state=seed, cpp_reproduce=False)
    outFile = open("out-py-random.txt", 'w')
elif (CPP_REPRODUCE == 1):
    centroids, clusterAssignments = kMeans(dataSet=X_test, k=NUM_CLUSTERS, random_state=seed, cpp_reproduce=True)
    outFile = open("out-py-np.txt", 'w')
else:
    print("Enter 0 or 1 to indicate whether the results should be reproducible in C++.")

labels = [int(row[0]) for row in clusterAssignments.tolist()]

# Calculate accuracy and homogeneity
accuracy = accuracy_score(y_test, labels)
print(accuracy)
#homogeneity = homogeneity_score(y_test, labels)
#next_rand_ints = np.random.randint(0, 256**4, 10)

outFile.write("Accuracy: {}\n".format(accuracy))
#outFile.write("Homogeneity: {}\n".format(homogeneity))
#outFile.write("Next_Rand: {}".format(next_rand_ints))

