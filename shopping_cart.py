# from IPython.display import clear_output

def shopping_cart():

    print("""
        -----Welcome to Shopping_Cart_3000!----
        
        You can:
        - add items to your cart -- type 'add'
        - remove items from you cart-- type 'remove'
        - view the contents of your -- type 'view'
        - or quit  -- type 'quit'
        """)

    cart = {}
    
    while True:

        action = input("What would you like to do? ")
        if action.lower() == 'quit':
            break
        
        elif action.lower() == 'add':
            item = input("Enter the grocery item: ")
            price = input("Enter it's price: ")
            cart[item] = price
            # clear_output()
        
        elif action.lower() == 'view':
            for key, value in cart.items():
                print(key + " @ " + value)
            # clear_output()

        elif action.lower() == 'remove':
            print("So far you have: ")
            for key in cart.keys():
                    print(key)
            to_remove = input("Which item would you like to remove? ")
            del cart[to_remove]
            # clear_output()

    if cart:
        print("At the time of checkout, your cart contains:")
        for key, value in cart.items():
            print(key + " @ " + value)
    elif cart == {}:
        print("Your cart doesn't have anything in it :(((")

shopping_cart()