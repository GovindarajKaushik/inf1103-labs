"""Lab 06: command-line interface for the OOP inventory system."""
import math
from pathlib import Path
from inventory_storage import load_inventory, save_inventory
from product import Product

INVENTORY_FILE = Path(__file__).resolve().with_name("inventory.json")


def get_valid_input():
    try:
        return int(input("Enter option: "))
    except ValueError:
        return "error"


def get_valid_number(prompt, number_type):
    while True:
        try:
            value = number_type(input(prompt))
            if value >= 0 and (number_type is int or math.isfinite(value)):
                return value
        except ValueError:
            pass
        print("Invalid input. Please enter a finite, non-negative number.")


def get_nonempty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def main():
    print("=" * 40 + "\nINVENTORY MANAGEMENT SYSTEM\n" + "=" * 40)
    try:
        inventory = load_inventory(INVENTORY_FILE)
    except (OSError, ValueError) as error:
        print(f"Could not load inventory: {error}")
        return
    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products\n2. Add Product\n3. Update Stock")
        print("4. Search Product\n5. Save Inventory\n6. Exit")
        print("-" * 30)
        option = get_valid_input()
        if option == 1:
            inventory.display_all()
        elif option == 2:
            product_id = get_nonempty_text("Product ID: ").upper()
            if inventory.search_product(product_id) is not None:
                print(f"Product with ID {product_id} already exists.")
                continue
            name = get_nonempty_text("Product Name: ")
            price = get_valid_number("Price: ", float)
            stock = get_valid_number("Stock Quantity: ", int)
            inventory.add_product(Product(product_id, name, price, stock))
            print("Product added successfully!")
        elif option in (3, 4):
            product = inventory.search_product(input("Enter Product ID: "))
            if product is None:
                print("Product not found.")
                continue
            product.display_information()
            if option == 3:
                product.update_stock(get_valid_number("New Stock Quantity: ", int))
                print("Stock updated successfully!")
        elif option in (5, 6):
            if not save_inventory(INVENTORY_FILE, inventory):
                print("Failed to save inventory. Please try again.")
                continue
            print("Inventory saved successfully to inventory.json")
            if option == 6:
                print("Thank you for using Inventory Management System.\nProgram terminated.")
                break
        else:
            print("Invalid input. Please select an option from 1 to 6.")


if __name__ == "__main__":
    main()
