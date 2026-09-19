# Lab 03 


# Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal
def get_valid_input():
    inventory = input("Please Enter Stock quantity: ")
    if inventory.lower() == "quit":
        return "quit"

    if not inventory.isdigit():
        print("Please enter a valid number.")
        return "error"

    if int(inventory) < 0:
        print("Please enter a valid number greater than or equal to 0.")
        return "error"

    return int(inventory)

# Calculates the new total inventory and processes it
def process_delivery(total_inventory, inventory):
    total_inventory += inventory
    return total_inventory

# takes a delivery amount and returns the tax of 10% of specific delivery
def calculate_tax(amount):
    return amount * 0.10

# prints out final summary
def generate_report(total_inventory, rejected_inventory):
    print(f"Total inventory: {total_inventory}, rejected entries: {rejected_inventory}")

# main function to remove global variables
def main():
    total_inventory = 0
    rejected_inventory = 0

    while True:
        inventory = get_valid_input()
        #quit the loop and prints summary
        if inventory == "quit":
            generate_report(total_inventory, rejected_inventory)
            break
        #count rejected attempts
        if inventory == "error":
            rejected_inventory += 1
            continue
        #calculate tax 10% for each delivery
        tax = calculate_tax(inventory)
        #count total_inventory
        total_inventory = process_delivery(total_inventory, inventory)
        # print warning and break loop when total inventory is more than 500
        if total_inventory > 500:
            print(f"ALERT! Total inventory exceeds 500 units. Currently at: {total_inventory}")
            break


main()


