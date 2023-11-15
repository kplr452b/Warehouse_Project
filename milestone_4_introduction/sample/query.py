from data import warehouse1, warehouse2

# Get the user name
user_name = input("Enter your name: ")

# Greet the user
print(f"Hello, {user_name}! Welcome to the stock query system.")

# Show the menu and ask to pick a choice
print("Menu:")
print("1. Search item by name")
print("2. Check item availability")
print("3. List all items")
choice = input("Enter your choice (1, 2, or 3): ")

# If they pick 1
if choice == '1':
    # Get the item name from the user
    item_name = input("Enter item name: ")

    # Search for the item in both warehouses
    matching_items = []
    for item in warehouse1 + warehouse2:
        if item_name.lower() in item.lower():
            matching_items.append(item)

    # Display the search results
    if matching_items:
        print("Matching items:")
        for item in matching_items:
            print(item)
    else:
        print("No matching items found.")

# Else, if they pick 2
elif choice == '2':
    # Get the item name from the user
    item_name = input("Enter item name: ")

    # Check item availability in both warehouses
    availability = False
    if item_name in warehouse1 or item_name in warehouse2:
        availability = True

    # Display the availability status
    if availability:
        print(f"The item '{item_name}' is available.")
    else:
        print(f"The item '{item_name}' is not available.")

# Else, if they pick 3
elif choice == '3':
    # Combine and display all items from both warehouses
    all_items = warehouse1 + warehouse2
    print("All items:")
    for item in all_items:
        print(item)

# Else
else:
    print("Invalid choice. Please select a valid option (1, 2, or 3).")

# Thank the user for the visit
print("Thank you for using the stock query system. Goodbye!")