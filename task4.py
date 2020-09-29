import numpy as np

arr1 = np.zeros(5)

arr2 = arr1

for i in range(4):
    arr1[i] = float(input('Znachenie {0}:'.format(i)))
print(arr1)

arr2[i+1] = arr1[i]