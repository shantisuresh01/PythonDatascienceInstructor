def order_pizza():
    import pizzashop

    pizzashop.print_menu()

    pizzashop.make_pizza(14, True, 'mozzarella', 'tomato')
    pizzashop.make_pizza(16, False, 'mozzarella/cheddar', 'pesto')

if __name__ == '__main__':
    order_pizza()