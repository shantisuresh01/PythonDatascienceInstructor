from time import sleep
import sys

# Conceptually, \r moves the cursor to the beginning
# of the line and then keeps outputting characters as normal.
# Put the \r at the beginning or end of your printed string, e.g. '\rthis string will start at the beginning of the line'. or
#  'the next string will start at the beginning of the line\r'.
print("FOR LOOP: have a definite number of iterations. Here the variable declaration, increment and condition are all in one convenient, easy-to-read place.")
print('Print the range of numbers in one line')
for i in range(10):
    print(str(i) + ',', end='')

print('\n')
print('Print the range of numbers in the same spot')
for i in range(10):
    print('\r' + str(i) + ',', end='')
    sleep(1)
    sys.stdout.flush() # flush the output buffer immediately

print("\nWHILE LOOP: has an indefinite number of iterations and one completion condition.")