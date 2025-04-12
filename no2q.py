products = [
    {"id": 1, "name": "Janak_Product1_24101", "price": 70},
    {"id": 2, "name": "Jnak_Product2_24101", "price": 120},
    {"id": 3, "name": "Janak_Product3_24101", "price": 180}
]

cart = []

# Function to add a product to cart
def add_to_cart():
    display_products()
    product_id = input("Enter product id: ")
    cart.append(products[int(product_id)-1])
    print(f"\nProduct has been added to the cart.")

# Function to display all products
def display_products():
    print("Product List:")
    for product in products:
        print(f"{product['id']}. {product['name']} - Rs {product['price']}")

# Function to display all products in cart
def display_cart():
    if not cart:
        print("\nNo products in the cart.")
    else:
        print("Product List:")
        for product in cart:
            print(f"{product['id']}. {product['name']} - Rs {product['price']}")
    

# Main program loop
while True:
    print("\nStore Menu:")
    print("1. Add to Cart")
    print("2. Display Cart")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == "1":
        add_to_cart()
        input()
    elif choice == "2":
        display_cart()
        input()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose the valid option")
