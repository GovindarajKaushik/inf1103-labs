# Lab 04


# load inventory (read text file)
def load_inventory(filename):
    try:
        inventory_file = open(filename, "r")
        return inventory_file.read()
    except FileNotFoundError:
        inventory_file = open(filename, "x")
        return inventory_file.read()


# Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal
def get_valid_input():
    inventory_list = list()
    product_name = input("Please Enter Product Name: ")
    if product_name.lower() == "quit":
        return "quit"
    inventory = input("Please Enter Stock quantity: ")

    # stop program when user types quit
    if inventory.lower() == "quit":
        return "quit"
    elif not inventory.isdigit():
        print("Please enter a valid number.")
        return "error"

    elif int(inventory) < 0:
        print("Please enter a valid number greater than or equal to 0.")
        return "error"

    elif not isinstance(product_name, str):
        print("Please enter a valid product name.")
        return "error"
    inventory_list.append((str(product_name), int(inventory)))
    return inventory_list

# Calculates the new total inventory and processes it
def process_delivery(current_total,new_value):
    return current_total + new_value

# takes a delivery amount and returns the tax of 10% of specific delivery
def calculate_tax(amount):
    return amount * 0.10

# prints out final summary
def generate_report(total_units,failed_attempts):
    print(f"Total inventory: {total_units}, rejected entries: {failed_attempts}")

# main function to remove global variables
def main():
    total_inventory = 0
    rejected_inventory = 0
    print("Current Inventory:\n")
    print(load_inventory("inventory.txt") + "\n")
    while True:
        inventory = get_valid_input()
        print(inventory)
        #quit the loop and prints summary
        if inventory == "quit":
            generate_report(total_inventory, rejected_inventory)
            break
        #count rejected attempts
        if inventory == "error":
            rejected_inventory += 1
            continue
        #calculate tax 10% for each delivery
        # tax = calculate_tax(inventory)
        #count total_inventory
        # total_inventory = process_delivery(total_inventory, inventory)
        # print warning and break loop when total inventory is more than 500
        if total_inventory > 500:
            print(f"ALERT! Total inventory exceeds 500 units. Currently at: {total_inventory}")
            break


main()


