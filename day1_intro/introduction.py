# Screen output
import day1_intro.day1_strings_ranges
import day1_intro.index_work

if __name__ == "__main__":
    first_name = 'Fred'
    print(first_name)

    # Initializing variables
    my_first_var: int = 3
    print(my_first_var)

    # Getting inpout from the user
    prompt = 'What is your name? '
    n = input(prompt)
    print(n)

    day1_intro.day1_strings_ranges.very_useful_utility()
    print(f"__name__ for day1_strings_ranges: {day1_intro.day1_strings_ranges.__name__}")
    print(f"My __name__ :  {__name__}")

