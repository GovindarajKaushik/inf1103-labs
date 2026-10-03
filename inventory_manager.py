# Lab 05
import os
import json


# get input
def get_valid_input():
    try: 
        option_number = int(input("Enter option: "))
    except ValueError:
        return "error"
    return option_number

# get input for valid numbers
def get_valid_number(prompt, number_type):
    while True:
        try:
            value = number_type(input(prompt))
            if value >= 0:
                return value
            else:
                print("Invalid input. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

            

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
def update_stock(product_ID, product_stock, inventory):
    # update stock
    inventory[product_ID]["Stock"] = product_stock
    return True


# search products 
def search_product(product_ID, inventory):
    if product_ID in inventory:
        return inventory[product_ID]
    else:
        return None

# Display all inventory
def display_all(inventory):
    print("\nCurrent Inventory\n")
    print("-" * 48)
    for product_id, product_details in inventory.items():
        print(f"ID: {product_id} | Name: {product_details['Name']} | Price: ${product_details['Price']:.2f} | Stock: {product_details['Stock']}")
    print("-" * 48 + "\n")


# load the inventory if inventory.json exists else create inventory.json
def load_inventory(inventory_file):
    if os.path.exists(inventory_file):
        # load existing inventory
        with open(inventory_file, 'r') as f:
            check_inventory = f.read()
            if check_inventory.strip() == "":
                print("\ninventory.json is empty. Starting with an empty inventory.\n")
                return {}
            else:
                print("\ninventory.json found.\nInventory loaded successfully.\n")
                return json.loads(check_inventory)
    else: 
        # create an empty file
        with open(inventory_file, 'w') as f:
            json.dump({}, f)
            print("No existing inventory found. Created a new one.\n")
            return {}

# save local json data to inventory.json file
def save_inventory(inventory_file, inventory):
    try:
        with open(inventory_file, 'w') as f:
            json.dump(inventory, f, indent=4)
    except Exception as e:
        return False
    return True



def main():

    # load menu
    # print title
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    # load inventory current inventory
    inventory = load_inventory("inventory.json")
    # print menu
    print("\n----------- MENU -----------")
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
        elif option_number == 2:
            print("\nAdd New Product")
            product_id = ""
            while product_id == "":
                product_id = input("Product ID: ").strip().upper()
                if product_id == "":
                    print("Product ID cannot be empty.")
            product_name = ""
            while product_name == "":
                product_name = input("Product Name: ").strip()
                if product_name == "":
                    print("Product Name cannot be empty.")
            product_price = get_valid_number("Price: ", float)
            product_stock_quantity = get_valid_number("Stock Quantity: ", int)
            new_product = {
                "ID": product_id,
                "Name": product_name,
                "Price": product_price,
                "Stock": product_stock_quantity
            }
            # Add product
            if add_product(inventory, new_product):
                print("\nProduct added successfully!\n")
            else:
                print("\nFailed to add product.\n")
        # Option 3: Update Stock 
        elif option_number == 3:
            print("\nUpdate Stock")
            product_id = input("Enter Product ID: ").strip().upper()
            # search for stock
            found_product = search_product(product_id, inventory)
            # update stock if product is found
            if found_product is not None:
                print(f"\nProduct Found: \nName: {found_product['Name']}\nCurrent Stock: {found_product['Stock']}\n")
                new_stock = get_valid_number("New Stock Quantity: ", int)
                if update_stock(product_id, new_stock, inventory):
                    print("\nStock updated successfully!\n")
            else:
                print("\nProduct not found.\n")

        # Option 4: Search Product
        elif option_number == 4:
            print("\nSearch Product")
            product_id  = input("Enter Product ID: ").strip().upper()
            found_product = search_product(product_id, inventory)
            if found_product is not None:
                print("\nProduct Found")
                print("-" * 30)
                print(f"ID: {product_id}")
                for key, value in found_product.items():
                    if key == "Price":
                        print(f"{key}: ${value:.2f}")
                    else:
                        print(f"{key}: {value}")
                print("-" * 30 + "\n")
            else:
                print("\nProduct not found.\n")
        # Option 5: Save inventory to file
        elif option_number == 5:
            print("\nSaving inventory...")
            if save_inventory("inventory.json", inventory):
                print("Inventory saved successfully to inventory.json\n")
            else:
                print("Failed to save inventory.\n")
                continue
            
        # Option 6: Quit and save
        elif option_number == 6:
            print("\nSaving inventory before exit...")
            if save_inventory("inventory.json", inventory):
                print("Inventory saved successfully.")
            else:
                print("Failed to save inventory.")
                continue
            print("\nThank you for using Inventory Management System.\nProgram terminated.")
            break
        
        # Rejected attempts
        elif option_number == "error":
            print("\nInvalid input. Please try again.\n")
            continue
        else:
            print("\nPlease select a valid option in range.\n")
        
if __name__ == "__main__":
    main()
