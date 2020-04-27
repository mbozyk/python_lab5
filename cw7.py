
import numpy as np

array = np.zeros(10)
array = list(array)
# print(array)

class MyException(Exception):
    def __init__(self,a,b,lista):
        super().__init__("assignment destination is read-only".format(a,b,lista))

def intend(a,b,lista):
    if a != lista[b]:
        raise MyException(a,b,lista)

print(intend(5,7,array))