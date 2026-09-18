# Lab 03 

# functionalities:
# Add the delivery amount to the running total
# Calculate the tax for that delivery.
# Update any counters and records you are tracking

rejected_inventory = 0
total_inventory = 0

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

def calculate_tax(amount):
    return amount * 0.08


while True:
    # inventory = input("Please Enter Stock quantity: ")

    # if inventory.lower() == "quit":
    #     print(f"Total inventory: {total_inventory}, rejected entries: {rejected_inventory}")
    #     break

    # elif not inventory.isdigit():
    #     rejected_inventory += 1
    #     print("Please enter a valid number.")
    #     continue

    # elif int(inventory) < 0:
    #     rejected_inventory += 1
    #     print("Please enter a valid number greater than or equal to 0.")
    #     continue
    inventory = get_valid_input()
    if inventory == "quit":
        print(f"Total inventory: {total_inventory}, rejected entries: {rejected_inventory}")
        break
    if inventory == "error":
        rejected_inventory += 1
        continue
    total_inventory = process_delivery(total_inventory, inventory)

    if total_inventory > 500:
        print(f"ALERT! Total inventory exceeds 500 units. Currently at: {total_inventory}")
        break
