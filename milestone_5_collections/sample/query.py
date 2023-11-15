import sys
import os
from data import stock

def list_all_items(stock):
    total_counter = 0
    warehouse1_counter = 0
    warehouse2_counter = 0

    for item in stock:
        total_counter += 1
        if item['warehouse'] == 1:
            warehouse1_counter += 1
        elif item['warehouse'] == 2:
            warehouse2_counter += 1

        full_name = f"{item['state']} {item['category']}"
        print(f"- {full_name}")

    print(f"\nTotal items in warehouse 1: {warehouse1_counter}")
    print(f"Total items in warehouse 2: {warehouse2_counter}")
    print(f"\nThank you for your visit, {user_name}!")

def search_and_place_order(stock):
    search_query = input("What is the name of the item? ").lower()
    matching_items = []
    max_availability = 0
    locations = []

    for item in stock:
        full_name = f"{item['state']} {item['category']}"
        if search_query in full_name.lower():
            matching_items.append(item)
            locations.append(f"Warehouse {item['warehouse']} (in stock for {item['date_of_stock']} days)")

    if matching_items:
        print(f"Amount available: {len(matching_items)}")
        print("Location:")
        for location in locations:
            print(f"- {location}")

        if len(matching_items) > 1:
            max_availability = max(item['warehouse'] for item in matching_items)
            max_availability_count = sum(1 for item in matching_items if item['warehouse'] == max_availability)
            print(f"Maximum availability: {max_availability_count} in Warehouse {max_availability}")
    else:
        print("Location: Not in stock")

    print(f"\nThank you for your visit, {user_name}!")

def browse_by_category(stock):
    categories = {}
    category_counter = 1

    for item in stock:
        category = item['category']
        if category not in categories:
            categories[category] = category_counter
            category_counter += 1

    print("Available categories:")
    for category, code in categories.items():
        count = sum(1 for item in stock if item['category'] == category)
        print(f"{code}. {category} ({count})")

    category_number = input("Type the number of the category to browse: ")
    selected_category = None

    for category, code in categories.items():
        if str(code) == category_number:
            selected_category = category
            break

    if selected_category:
        print(f"\nList of {selected_category}s available:")
        for item in stock:
            if item['category'] == selected_category:
                print(f"{item['state']} {item['category']}, Warehouse {item['warehouse']}")
    else:
        print("\nInvalid category number. Please try again.")

    print(f"\nThank you for your visit, {user_name}!")

def main_menu(stock):
    print(f"\nHello, {user_name}!")
    print("What would you like to do?")
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Browse by category")
    print("4. Quit")
    operation_number = input("Type the number of the operation: ")

    if operation_number == '1':
        list_all_items(stock)
    elif operation_number == '2':
        search_and_place_order(stock)
    elif operation_number == '3':
        browse_by_category(stock)
    elif operation_number == '4':
        print("\nGoodbye!")
        return
    else:
        print("\nInvalid operation number. Please try again.")

    main_menu(stock)  # After performing the selected operation, return to the main menu


user_name = input("What is your user name? ")

main_menu(stock)