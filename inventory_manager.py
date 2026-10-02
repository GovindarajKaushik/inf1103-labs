# Lab 05
import os
import json


# get input
def get_valid_input():
    option_number = int(input("Enter Option: "))
    if not isinstance(option_number, int):
        print("Please enter a valid option number.")
        return "error"
    return option_number


# Add products to json file
def add_product():
    return None

# Update json stock locally first before saving to json
def update_stock():
    return None


# search products 
def search_product():
    return None

# Display all inventory
def display_all(inventory):
    print("\nCurrent Inventory:\n")
    print("-" * 50)
    for product_id, product_details in inventory.items():
        print(f"ID:{product_id} | Name: {product_details['Name']} | Price: {product_details['Price']} | Stock: {product_details['Stock']}")
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
        # option 1 Display all
        if option_number == 1:
            display_all(inventory)
        # Quit and save
        if option_number == 6:
            print("\nSaving inventory before exit...")
            print("Inventory saved successfully.")
            print("\nThank you for using  the Inventory Management System.\nProgram terminated.")
            break
        
        # Rejected attempts
        if option_number == "error":
            print("Invalid input. Please try again.")
            continue
        

main()
