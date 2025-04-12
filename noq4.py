# Initialize product names and prices
products = {
    "Janak_Product1_24101": 199,
    "Janak_Product2_24101": 299,
    "Janak_Product3_24101": 399,
    "Janak_Product4_24101": 499,
}

# Initialize an empty cart as a list
cart = []

# Function to display available products
def display_products():
    print("Available Products:")
    for product, price in products.items():
        print(f"{product}: Rs {price}")

# Function to add a product to the cart
def add_to_cart(product_name):
    if product_name in products:
        cart.append((product_name, products[product_name]))
        print(f"{product_name} added to the cart.")
    else:
        print("Product not found. Please choose a valid product.")

# Function to calculate the total cost of items in the cart
def calculate_total():
    total = sum(price for _, price in cart)
    return total

# Main program loop
while True:
    print("\nMenu:")
    print("1. Display Products")
    print("2. Add to Cart")
    print("3. Checkout")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        display_products()
    elif choice == "2":
        product_name = input("Enter the name of the product you want to add to your cart: ")
        add_to_cart(product_name)
    elif choice == "3":
        if not cart:
            print("Your cart is empty. Please add products to your cart first.")
        else:
            print("Items in Your Cart:")
            for item, price in cart:
                print(f"{item}: Rs {price}")
            print(f"Total Cost: Rs {calculate_total()}")
            cart.clear()
            print("Thank you for shopping with us!")
    elif choice == "4":
        print("Thank you for visiting our store!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
