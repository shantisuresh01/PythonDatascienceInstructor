# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def get_name():
    prompt = 'What is your name? '
    # responses = input(prompt).split()
    # print(f'My name is {responses[0]}')
    n = input(prompt)
    return n
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}') # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Welcome to SimpleScript')
    # Calling a function
    n = get_name()
    print(f'My name is {n}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


