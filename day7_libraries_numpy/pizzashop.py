def make_pizza(size, stuff_crust, cheese_type, sauce_type):
    if stuff_crust:
        print (f'Your {size} inch stuff crust pizza with {cheese_type} cheese and {sauce_type} sauce will be ready soon!')
    else:
        print (f'Your {size} inch pizza with {cheese_type} cheese and {sauce_type} sauce will be ready soon!')

def print_menu():
    print ('Welcome to the GC Pizza Shop!')
    print ('To make a pizza, call make_pizza.')
    print ('Please pass in the size, whether it is stuffed crust, cheese type, and sauce type')

print (f"Testing out pizzashop's __name__ variable. Here's what's in it: {__name__}.")