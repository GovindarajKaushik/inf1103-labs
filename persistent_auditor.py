# Lab 04


# load inventory (read text file)
def load_inventory(file_name):
    try:
        with open(file_name, "r") as inventory_file:
            return inventory_file.read()
    except FileNotFoundError:
        with open(file_name, "w") as inventory_file:
            pass
        return ""


# Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal
def get_valid_input():
    inventory_list = []
    product_name = input("\nPlease Enter Product Name: ")
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
    inventory_list.append(str(product_name))
    inventory_list.append(str(inventory))
    return inventory_list

# Create new order list (array)
def save_inventory(inventory_list, file_name):
    with open(file_name, "r+") as inventory_file:
        if inventory_file.read() == "":
            inventory_file.write(str(inventory_list))
        else:
            inventory_file.seek(0)
            lines = inventory_file.readlines()
            # remove \n
            fixed_lines = []
            fixed_lines.append(lines[-1].strip())

            # Get the last index to add to new order
            last_entry = fixed_lines[0]
            last_id = int(last_entry.split(",")[0])
            new_id = last_id + 1
            # New order List
            new_order_list = []
            new_order_list.append(str(new_id))
            for inventory in inventory_list:
                new_order_list.append(inventory)
            formatted_order = ", ".join(new_order_list)

            # Write new order into inventory.txt
            inventory_file.write("\n" + formatted_order)


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
    current_orders = []
    # Printing the previously saved inventory file
    print("Current Orders:\n")
    with open("inventory.txt", "r") as inventory_file:
        inventory_list = inventory_file.readlines()
    cleaned_order_list = [line.strip() for line in inventory_list] 
    for order in cleaned_order_list:
        print(order)
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
        # Keeping track of current orders
        current_orders.append(inventory)
        # print warning and break loop when total inventory is more than 500
        if total_inventory > 500:
            print(f"ALERT! Total inventory exceeds 500 units. Currently at: {total_inventory}")
            break


main()


