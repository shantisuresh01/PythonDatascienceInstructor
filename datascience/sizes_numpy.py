# Reference: https://pythonspeed.com/articles/python-integers-memory/
# Vaniila Python objects
def main():
    import sys
    import numpy as np

    size=1000000
    print("Using Vanilla Python int objects")
    print(f'Size of smallint: {sys.getsizeof(123)}')
    list_of_numbers = []
    for i in range(size):
        list_of_numbers.append(i)
    print(f'Sizeof list of {size} int objects: {sys.getsizeof(list_of_numbers)}')

    print('Using Numpy')
    arr = np.zeros((size,), dtype=np.uint64)
    for i in range(size):
        arr[i] = i
    print(f'Sizeof list of {size} int objects: {sys.getsizeof(arr)}')

if __name__=='__main__':
    main()