# Vaniila Python objects
from sys import getsizeof
import numpy as np

print("Using Vanilla Python int objects")
print(f'Size of smallint: {sys.getsizeof(123)}')
list_of_numbers = []
for i in range(1000000):
    list_of_numbers.append(i)
print(f'Sizeof list of 100000 int objects: {getsizeof(list_of_numbers)}')

print('Using Numpy')
arr = np.zeros((1000000,), dtype=np.uint64)
for i in range(1000000):
    arr[i] = i
print(f'Sizeof list of 100000 int objects: {getsizeof(arr)}')

