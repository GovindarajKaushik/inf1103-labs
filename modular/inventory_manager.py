# Lab 05: procedural inventory management using dictionaries and functions.
import os
import json


def get_valid_input():
    try:
        return int(input("Enter option: "))
    except ValueError:
        return "error"


def get_valid_number(prompt, number_type):
    while True:
        try:
            value = number_type(input(prompt))
            if value >= 0:
                return value
            print("Invalid input. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


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


def update_stock(product_ID, product_stock, inventory):
    inventory[product_ID]["Stock"] = product_stock
    return True


def search_product(product_ID, inventory):
    return inventory.get(product_ID)


def display_all(inventory):
    print("\nCurrent Inventory\n")
    print("-" * 48)
    for product_id, product_details in inventory.items():
        print(f"ID: {product_id} | Name: {product_details['Name']} | Price: ${product_details['Price']:.2f} | Stock: {product_details['Stock']}")
    print("-" * 48 + "\n")


def load_inventory(inventory_file):
    if os.path.exists(inventory_file):
        with open(inventory_file, 'r') as f:
            contents = f.read()
            if contents.strip() == "":
                print("\ninventory.json is empty. Starting with an empty inventory.\n")
                return {}
            print("\ninventory.json found.\nInventory loaded successfully.\n")
            return json.loads(contents)
    with open(inventory_file, 'w') as f:
        json.dump({}, f)
    print("No existing inventory found. Created a new one.\n")
    return {}


def save_inventory(inventory_file, inventory):
    try:
        with open(inventory_file, 'w') as f:
            json.dump(inventory, f, indent=4)
    except Exception:
        return False
    return True


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory = load_inventory("inventory.json")
    print("\n----------- MENU -----------")
    print("1. Display All Products\n2. Add Product\n3. Update Stock")
    print("4. Search Product\n5. Save Inventory\n6. Exit")
    print("-" * 30 + "\n")
    while True:
        option_number = get_valid_input()
        if option_number == 1:
            display_all(inventory)
        elif option_number == 2:
            print("\nAdd New Product")
            product_id = ""
            while not product_id:
                product_id = input("Product ID: ").strip().upper()
                if not product_id:
                    print("Product ID cannot be empty.")
            product_name = ""
            while not product_name:
                product_name = input("Product Name: ").strip()
                if not product_name:
                    print("Product Name cannot be empty.")
            product_price = get_valid_number("Price: ", float)
            product_stock_quantity = get_valid_number("Stock Quantity: ", int)
            new_product = {"ID": product_id, "Name": product_name,
                           "Price": product_price, "Stock": product_stock_quantity}
            if add_product(inventory, new_product):
                print("\nProduct added successfully!\n")
            else:
                print("\nFailed to add product.\n")
        elif option_number == 3:
            print("\nUpdate Stock")
            product_id = input("Enter Product ID: ").strip().upper()
            found_product = search_product(product_id, inventory)
            if found_product is not None:
                print(f"\nProduct Found: \nName: {found_product['Name']}\nCurrent Stock: {found_product['Stock']}\n")
                new_stock = get_valid_number("New Stock Quantity: ", int)
                if update_stock(product_id, new_stock, inventory):
                    print("\nStock updated successfully!\n")
            else:
                print("\nProduct not found.\n")
        elif option_number == 4:
            print("\nSearch Product")
            product_id = input("Enter Product ID: ").strip().upper()
            found_product = search_product(product_id, inventory)
            if found_product is not None:
                print("\nProduct Found\n" + "-" * 30)
                print(f"ID: {product_id}")
                for key, value in found_product.items():
                    if key == "Price":
                        print(f"{key}: ${value:.2f}")
                    else:
                        print(f"{key}: {value}")
                print("-" * 30 + "\n")
            else:
                print("\nProduct not found.\n")
        elif option_number in (5, 6):
            print("\nSaving inventory...")
            if not save_inventory("inventory.json", inventory):
                print("Failed to save inventory.\n")
                continue
            print("Inventory saved successfully to inventory.json\n")
            if option_number == 6:
                print("\nThank you for using Inventory Management System.\nProgram terminated.")
                break
        elif option_number == "error":
            print("\nInvalid input. Please try again.\n")
        else:
            print("\nPlease select a valid option in range.\n")


if __name__ == "__main__":
    main()
