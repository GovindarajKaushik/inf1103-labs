# Lab 05
import os
import json


# get input
def get_valid_input():
    try: 
        option_number = int(input("Enter Option: "))
    except ValueError:
        return "error"
    return option_number


# Add products to json file
def add_product(inventory, new_product):
        product_id = new_product["ID"]
        if product_id in inventory:
            print(f"Product with ID {product_id} already exists.")
            return False
        inventory[product_id] = {
            "Name": new_product["Name"],
            "Price": new_product["Price"],
            "Stock": new_product["Stock"]
        }
        return True

# Update json stock locally first before saving to json
def update_stock(product_ID, product_stock):
    return None


# search products 
def search_product(product_ID, inventory):
    if product_ID in inventory:
        return inventory[product_ID]
    else:
        print("Product not found.")
        return None

# Display all inventory
def display_all(inventory):
    print("\nCurrent Inventory:\n")
    print("-" * 50)
    for product_id, product_details in inventory.items():
        print(f"ID:{product_id} | Name: {product_details['Name']} | Price: ${product_details['Price']:.2f} | Stock: {product_details['Stock']}")
    print("-" * 50 + "\n")


# load the inventory if inventory.json exists else create inventory.json
def load_inventory(inventory_file):
    if os.path.exists(inventory_file):
        # load existing inventory
        with open(inventory_file, 'r') as f:
            check_inventory = f.read()
            if check_inventory.strip() == "":
                return {}
            else:
                return json.loads(check_inventory)
    else: 
        # create an empty file
        with open(inventory_file, 'w') as f:
            json.dump({}, f)

# save local json data to inventory.json file
def save_inventory(inventory_file):
    return None



def main():

    # load inventory current inventory
    inventory = load_inventory("inventory.json")
    # load menu
    # print title
    print("=" * 50)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)
    # print menue
    print("\n------------MENU-------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-" * 30 + "\n")
    while True:
        # user input
        option_number = get_valid_input()
        # option 1: Display all
        if option_number == 1:
            display_all(inventory)
        # Option 2: Add Product
        if option_number == 2:
            product_id = input("Product ID: ")
            product_name = input("Product Name: ")
            product_price = input("Price: ")
            product_stock_quantity = input("Stock Quantity: ")
            new_product = {
                "ID": product_id,
                "Name": product_name,
                "Price": float(product_price),
                "Stock": int(product_stock_quantity)
            }
            # Add product
            if add_product(inventory, new_product):
                print("Product added successfully!")
        # Option 3: Update Stock 

        # Option 4: Search Product
        if option_number == 4:
            print("\nSearch Product")
            product_id  = str(input("Enter Product ID: "))
            found_product = search_product(product_id, inventory)
            print("\nProduct Found")
            print("-" * 30)
            print(f"ID: {product_id}")
            for items in found_product.items():
                print(f"{items[0]}: {items[1]}")
            print("-" * 30 + "\n")
        
        # option 6: Quit and save
        if option_number == 6:
            print("\nSaving inventory before exit...")
            print("Inventory saved successfully.")
            print("\nThank you for using  the Inventory Management System.\nProgram terminated.")
            break
        
        # Rejected attempts
        if option_number == "error":
            print("\nInvalid input. Please try again.\n")
            continue
        

main()
