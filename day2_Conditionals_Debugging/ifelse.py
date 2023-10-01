# Conditionals
# Ask for an integer input
# Check if it is an integer
# Print whether the number is even or odd
# Introduce:
# a = list(map(int,input().split()))

n = input("Please enter a number: ").split()
if(n[0].isdigit()):
    print("First response is an Integer")
else:
    print("Sorry, non-integer response given")