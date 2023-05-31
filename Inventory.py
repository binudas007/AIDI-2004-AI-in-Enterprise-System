# Inventory Management System

inventory = {}

def add_item():
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

    print("Item added successfully.")

def update_quantity():
    item_name = input("Enter item name: ")
    if item_name in inventory:
        new_quantity = int(input("Enter new quantity: "))
        inventory[item_name] = new_quantity
        print("Quantity updated successfully.")
    else:
        print("Item not found in inventory.")

def generate_report():
    print("Current Inventory:")
    print("------------------")
    for item_name, quantity in inventory.items():
        print(f"{item_name}: {quantity}")

# Main program loop
while True:
    print("\nInventory Management System")
    print("---------------------------")
    print("1. Add Item")
    print("2. Update Quantity")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_quantity()
    elif choice == "3":
        generate_report()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
