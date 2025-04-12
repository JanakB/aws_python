# Create an empty dictionary to store products
products = {}

# Function to add a product
def add_product():
    product_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    description = input("Enter product description: ")

    product_info = {
        'name': product_name,
        'price': price,
        'description': description
    }

    products[product_id] = product_info
    print(f"{product_name} has been added to the store with ID: {product_id}")

# Function to display all products
def display_products():
    print("List of products in the store:")
    for product_id, product in products.items():
        print(f"Product ID: {product_id}")
        print(f"Name: {product['name']}")
        print(f"Price: Rs {product['price']:.2f}")
        print(f"Description: {product['description']}")
        print("------------")

# Function to search for a product
def search_product(product_id):
    product = products.get(product_id)
    if product:
        print("Product found:")
        print(f"Product ID: {product_id}")
        print(f"Name: {product['name']}")
        print(f"Price: Rs {product['price']:.2f}")
        print(f"Description: {product['description']}")
    else:
        print("Product not found.")

# Main menu
while True:
    print("\nE-commerce Store Menu:")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_product()
    elif choice == '2':
        display_products()
    elif choice == '3':
        product_id = input("Enter product ID to search: ")
        search_product(product_id)
    elif choice == '4':
        print("Thank you for using our Store")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")
