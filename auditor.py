
rejected_inventory = 0
total_inventory = 0

while True:
    inventory = input("Please Enter Stock quantity: ")

    if inventory.lower() == "quit":
        break

    elif not inventory.isdigit():
        rejected_inventory += 1
        print("Please enter a valid number.")
        continue

    elif int(inventory) < 0:
        rejected_inventory += 1
        print("Please enter a valid number greater than or equal to 0.")
        continue

    total_inventory += int(inventory)
