from numpy import random as random
import numpy as np
matrix_1 = random.normal(size=(4,4))
matrix_2 = random.normal(size=(4,4))
print(f"{matrix_1}\n")
print(f"{matrix_2}\n")
multiplied_array = np.multiply(matrix_1,matrix_2)
print(f"Multiplied matrices\n {multiplied_array}\n")
# 1 sposób: wykorzystanie biblioteki numpy
diag1 = np.diagonal(multiplied_array)
print(diag1)
# 2 sposób: skonstruowanie prostej listy składanej a następnie zaokrąglenie wartości w liście przy użyciu biblioteki numpy
diag2 = [multiplied_array[i][i] for i in range(len(multiplied_array))]
diag2 = np.around(diag2, 8)
print(diag2)
# 3 sposób: skosntruowanej innej listy składanej
multiplied_array = list(multiplied_array)
diag3 = [row[i] for i, row in enumerate(multiplied_array)]
diag3 = np.around(diag3,8)
print(diag3)
