# # Screen output
# first_name:str = "Fred"
# print(first_name)
#
# # Extend a string
# first_name = 'Fred' + " " + "O'Connor"
# print(first_name)
#
# # Re-assigning and "int" type to a previously declared "str" type
# # Python allows this as it is a dynamically types language.
# first_name:int = 1
# print(first_name)
#
# # Initializing variables
# my_first_int: int = 3
# print(my_first_int)
#
# # Exploring backslash
# # Screen output
# first_name:str = "Fred \\ \n"
# print(first_name)
#
# # Exploring f-string
# print(f'My first integer is: {my_first_int}')
#
# str1 = 'xyz123'
# strlen = len(str1) # 'len()' is a built-in function
# print(strlen)
#
# # Exploring string positions
# str1 = 'abcdef'
# print(str1[0], str1[1])
#
# str = 'abcdefghi'
# print(str[2:6])

# str = 'abcdefghijklmno'
# print(str[3:11:2])

# str = 'abcdefghi'
# last = str[-1]
# print(last)
# print(str[-2])
#
# str = 'abcdefghi'
# print(str[0:-2])
# print(str[:])
# print(str[::-2])
# print(str[::2])

# str = 'abcdefghi'
# print(str[-4:-2])

# bigstr = 'abc' * 3
# print(bigstr)
# divider = '=' * 30
# print(divider)
# str = 'First Name\tLast Name'
# print(str)
#
# str1 = """Hello everybody
# this is a long string that
# takes up multiple lines!
# We use triple-quotes for it!"""
# print(str1)

# str1 = r'I need a backslash\in this string. And the \t does not make a tab!'
# str1 = r'\Users\john\earnings.xlsx'
# print(str1)

str = 'hello'
print(str + ' world!')
str = str + ' world!'
print(str + "yay it worked!")

# immutable: str, int, float, tuple
# mutable: l = list ['a', 'b', 'c']
# l.extend("d")
# l looks like this ['a', 'b', 'c', 'd']

# h e l l o
# h e l l o w o r l d


# division: /
# backslash: \\


# Getting input from the user
# prompt:str = 'What is your name? '
# resp = input(prompt)
# print(resp)