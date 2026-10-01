# Lab 04


# load inventory (read text file)
def load_inventory(file_name):
    try:
        with open(file_name, "r") as inventory_file:
            inventory_list = inventory_file.readlines()
            cleaned_order_list = [line.strip() for line in inventory_list] 
            return cleaned_order_list
    except FileNotFoundError:
        with open(file_name, "w") as inventory_file:
            pass
        return []


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
        is_empty = inventory_file.read() == ""
        inventory_file.seek(0, 2)  

        for order in inventory_list:
            formatted_order = ", ".join(order)

            if is_empty:
                inventory_file.write(formatted_order)
                is_empty = False
            else:
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
    next_id = 1001
    
    # Printing the previously saved inventory file
    print("Current Orders:\n")
    existing_order_list = load_inventory("inventory.txt")
    for order in existing_order_list:
        print(order)
        # Update next_id based on existing orders
        if order:
            existing_id = int(order.split(",")[0])
            next_id = existing_id + 1

    while True:
        inventory = get_valid_input()
        
        # Quit and save
        if inventory == "quit":
            save_inventory(current_orders, "inventory.txt")
            print("\nOrder successfully saved to inventory.txt")
            break
        
        # Rejected attempts
        if inventory == "error":
            rejected_inventory += 1
            continue
        
        # Create order with ID (no spaces)
        new_order = [str(next_id)] + inventory
        formatted_order = ",".join(new_order)
        
        # Print new order
        print(f"New Order Added:")
        print(formatted_order)
        
        # Track order
        current_orders.append(new_order)
        next_id += 1
        
        # Alert if over 500
        if total_inventory > 500:
            print(f"ALERT! Total inventory exceeds 500 units. Currently at: {total_inventory}")
            break



main()


