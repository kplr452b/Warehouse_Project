from data import personnel, stock

# Global variables
user_name = ""
actions_taken = []

# Functions
def get_user_name():
    global user_name
    user_name = input("Enter your name: ")

def greet_user():
    print(f"Welcome, {user_name}!")

def get_selected_operation():
    print("Operations:")
    print("1. List items")
    print("2. Search and order item")
    print("3. Browse by category")
    print("4. Quit")

    return input("Enter the operation number: ")

def list_items_by_warehouse():
    if isinstance(stock, list):
        for item in stock:
            print(f"Item: {item['category']}, State: {item['state']}, Warehouse: {item['warehouse']}, Date of Stock: {item['date_of_stock']}")
        print()
    else:
        print("Invalid stock data. Please check the data.py module.")

    actions_taken.append("Listed items")

def search_item(item_name):
    results = []
    if isinstance(stock, list):
        for item in stock:
            if item_name.lower() in item["category"].lower():
                results.append(item)
    else:
        print("Invalid stock data. Please check the data.py module.")

    return results

def print_search_results(results):
    for item in results:
        print(f"Item: {item['category']}, State: {item['state']}, Warehouse: {item['warehouse']}, Date of Stock: {item['date_of_stock']}")
    if not results:
        print("No items found.")

def order_item(item):
    global user_name
    global actions_taken

    print(f"Ordering item: {item['category']}")
    print(f"State: {item['state']}")
    print("Please enter your password to confirm the order.")
    password = input("Password: ")

    # Validate user
    user_found = False
    for person in personnel:
        if person["user_name"] == user_name and person.get("password") == password:
            user_found = True
            break

    if user_found:
        print(f"Item ordered: {item['category']}")
        actions_taken.append(f"Ordered item: {item['category']}")
    else:
        print("Invalid username or password.")

def search_and_order_item():
    item_name = input("Enter the item name to search: ")

    results = search_item(item_name)
    print_search_results(results)

    if results:
        choice = input("Do you want to order any of the above items? (y/n): ")
        if choice.lower() == "y":
            item_index = int(input("Enter the index of the item to order: "))
            if item_index >= 0 and item_index < len(results):
                order_item(results[item_index])

def browse_by_category():
    if isinstance(stock, list):
        categories = set(item["category"] for item in stock)
        print("Categories:")
        for category in categories:
            print(category)
        print()
    else:
        print("Invalid stock data. Please check the data.py module.")

    actions_taken.append("Browsed by category")

# Additional functions
def print_actions_taken():
    print(f"\nThank you for your visit, {user_name}!")
    print("In this session you have:")
    for index, action in enumerate(actions_taken):
        print(f"{index + 1}. {action}.")

def main():
    get_user_name()
    greet_user()

    while True:
        operation = get_selected_operation()
        print()

        # Execute the operation
        if operation == "1":
            list_items_by_warehouse()

        elif operation == "2":
            search_and_order_item()

        elif operation == "3":
            browse_by_category()

        elif operation == "4":
            break

        else:
            print("*" * 50)
            print(operation, "is not a valid operation.")
            print("*" * 50)

        print()

        # Ask for another operation
        choice = input("Do you want to perform another operation? (y/n): ")
        if choice.lower() != "y":
            break

    print_actions_taken()

# Run the program
if __name__ == "__main__":
    main()