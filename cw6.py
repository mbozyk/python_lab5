from numpy import random as random
import numpy as np
array = np.random.random(20)
array = np.around(array,8)
array = list(array)
def n_largest(array, n):
    array_of_largest_values = []

    for i in range(0, n):
        maks = 0

        for k in range(len(array)):
            if  array[k] > maks:
                maks = array[k]
        array.remove(maks)
        array_of_largest_values.append(maks)
    array_of_largest_values = np.around(array_of_largest_values,8)
    print(array_of_largest_values)
def main():
    print(array)
    n = 5
    n_largest(array,n)
if __name__ == '__main__':
    main()