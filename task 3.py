import numpy as np

n = int(input('кол-во строк: '))
m = int(input('кол-во столбцов: ')) 

arr1 = np.ndarray(shape=(n,m))
arr2 = np.ndarray(shape=(n,m))
arr3 = np.ndarray(shape=(n,m)) 

for i in range(n):
    for k in range(m):
        arr1[i,k] = float(input('Массив 1, строка {0}, столбцов {1}: '.format(i,k)))
        arr2[i,k] = float(input('Массив 2, строка {0}, столбцов {1}: '.format(i,k)))
    if arr1[i,k] > arr2[i,k]:
        arr3[i,k] = arr1[i,k]
    else:
        arr3[i,k] = arr2[i,k]
print(arr3)
