# Sample product data in a dictionary format
products = {
    "Janak_Product1_24101": 120,
    "Janak_Product2_24101": 160,
    "Janak_Product3_24101": 190,
    "Janak_Product4_24101": 220,
    "Janak_Product5_24101": 240,
}

# Initialize an empty wish list
wish_list = []

# Function to display the product list
def display_product_list():
    print("Product List:")
    for product, price in products.items():
        print(f"{product}: Rs {price}")

# Function to add a product to the wish list
def add_to_wish_list(product_name):
    if product_name in products:
        wish_list.append(product_name)
        price = products[product_name]  # Get the price of the product
        print(f"{product_name} (Rs {price}) added to your wish list.")
    else:
        print(f"{product_name} is not in the product list. Cannot add to wish list.")

# Function to display the wish list
def display_wish_list():
    print("Wish List:")
    for product in wish_list:
        print(f"{product}: Rs {products[product]}")  # Display the price of each product in the wish list

# Main program loop
while True:
    print("\nOptions:")
    print("1. View Product List")
    print("2. Add Product to Wish List")
    print("3. View Wish List")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_product_list()
    elif choice == '2':
        product_name = input("Enter the product name to add to wish list: ")
        add_to_wish_list(product_name)
    elif choice == '3':
        display_wish_list()
    elif choice == '4':
        print("Thank you for visiting us")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
