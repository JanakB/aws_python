cart = [
    {"id": 1, "name": "Janak_Product1_24101", "price": 55},
    {"id": 2, "name": "Janak_Product2_24101", "price": 175},
    {"id": 3, "name": "Janak_Product3_24101", "price": 135},
    {"id": 4, "name": "Janak_Product4_24101", "price": 225}
]

def display_cart():
    if not cart:
        print("\nNo products in the cart.")
    else:
        print("Product List:")
        for product in cart:
            print(f"{product['id']}. {product['name']} - Rs {product['price']}")

while True:
    print("\nStore Menu:")
    print("1. Display Cart")
    print("2. Empty Cart")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == "1":
        display_cart()
        input()
    elif choice == "2":
        cart.clear()
        print("The cart has been emptied.")
        input()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose valid option")