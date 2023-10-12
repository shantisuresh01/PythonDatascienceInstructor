def get_sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

def confirm_my_input(n = None):
    return 6 if n is not None else -1  # ternary if statement


# def confirm_my_input(n = None):
#     # Comments are missing
#     if n is not None:
#         return n
#     else:
#         return -1

def validate_input_cards():
    c1 = input("C1:")
    c2 = input("C2:")
    c3 = input("C3:")
    return c1, c2, c3 # 0-9, A, J, Q, K

