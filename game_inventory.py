import csv


def display_inventory(inventory):
    for item in inventory.items():
        print(f"{item[0]}: {item[1]}")
               

def add_to_inventory(inventory, added_items):
    for element in added_items:
        if element in inventory:
            inventory[element] += 1
    return inventory
   
    """Add to the inventory dictionary a list of items from added_items."""


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for element in removed_items:
        if element in inventory:
            if inventory[element] > 1:
                inventory[element] -= 1
            # if inventory[element] == 0
            else:
                inventory.pop(element)
    return inventory

def print_table(inventory, order=None):




    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """

    pass


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""
     # with open('test_inventory.csv', 'r') as csv_file:
    #     inventory = csv.reader(csv_file)
    #     for line in inventory:
    #         for item in line:
    #             for key, value in item:
    #                 print(key, ' : ', value)
    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass
