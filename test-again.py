import numpy as np

np.random.seed(12345)
print(np.random.randint(256**4, dtype='<u4', size=1)[0])