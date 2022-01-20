import csv


def display_inventory(inventory):
    for item in inventory.items():
        print(f"{item[0]}: {item[1]}")
               

def add_to_inventory(inventory, added_items):
    for element in added_items:
        if element in inventory:
            inventory[element] += 1
        else:
            inventory[element] = 1
    return inventory


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for element in removed_items:
        if element in inventory:
            if inventory[element] > 1:
                inventory[element] -= 1
            else:
                inventory.pop(element)
    return inventory


def print_table(inventory, order=None):

    key_column_length = len("item name")
    for key, value in inventory.items():
        if len(key) > len("item name"):
            key_column_length = len(key)

    value_column_length = len("count")
    for key, value in inventory.items():
        if len(str(value)) > len("count"):
            value_column_length = len(str(value))

    dashed_line = "-" * key_column_length + "-" * 3 + "-" * value_column_length
    diff_item_name = max(0, key_column_length - len("item name"))
    diff_count = max(0, value_column_length - len("count"))
    header = diff_item_name * " " + "item name" + " | " + diff_count * " " + "count"
    print(dashed_line)
    print(header)
    print(dashed_line)

    ordered_inventory = inventory.items()

    if order == "count,desc":
        ordered_inventory = sorted(inventory.items(), key=lambda item: item[1], reverse = True)
    elif order == "count,asc":
        ordered_inventory = sorted(inventory.items(), key=lambda item: item[1], reverse = False)

    for key, value in ordered_inventory:
        diff_key = key_column_length - len(key)
        diff_value = value_column_length - len(str(value))
        print(diff_key * " " + key + " | " + diff_value * " " + str(value))

    print(dashed_line)


def import_inventory(inventory, filename="test_inventory.csv"):
    """Import new inventory items from a CSV file."""
    try:
        with open(filename, mode = 'r') as csv_file:
            input_csv = csv.reader(csv_file, delimiter=',')
            for line in input_csv:
                line.sort()
                inventory = add_to_inventory(inventory, line)
          
        return inventory

    except FileNotFoundError:
        print(f"File '{filename}' not found!")


def export_inventory(inventory, filename="export_inventory.csv"):

    list_of_items = []
    for key, value in inventory.items():
        for i in range(value):
            list_of_items.append(key)

    try:
        with open(filename, 'a') as f:
            write = csv.writer(f)
            write.writerow(list_of_items)
    except IOError:
        print(f"You don't have permission creating file '{filename}'!")


