import numpy as np
from numpy import random as random
vec = random.random(size=(1,10))
print(vec)
new_list = []
indexes = [0,1,2,3,4,5,6,7,8,9]

for i in range(len(indexes)):
    if i % 2 == 0:
        x = vec[0,i]**2
        x = np.around(x,8)
        new_list.append(x)
        i = i+1
    else:
        vec[0,i] = 0
        new_list.append(vec[0,i])
        i = i + 1
print(new_list)
