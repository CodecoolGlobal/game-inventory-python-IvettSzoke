import csv
import pprint

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
            # if inventory[element] == 0
            else:
                inventory.pop(element)
    return inventory

def print_table(inventory, order=None):
    inventory = {"rope": 1, "torch": 2}
    my_list = inventory.items()

    for key, value in my_list:
        item_name, count = key, value
        print ("{:<10} {:<10}".format('item_name', 'count'))

        
    # for row in zip(*([key] + value for key, value in sorted(inventory.items()))):
    #     print(*row)
# Insert data into dictionary
# dict1 = {1: ["Samuel", 21, 'Data Structures'],
#      2: ["Richie", 20, 'Machine Learning'],
#      3: ["Lauren", 21, 'OOPS with java'],
# #      }
 
# # Print the names of the columns.
#     # print ("{:<10} {:<10}".format('item_name', 'count'))
#     print('item name', 'count')
# # print each data item.
#     # for key, value in inventory.items():
#     #     item_name, count = value
#     # print ("{:<10} {:<10}".format('item_name', 'count'))
#     for i in range(2):
#         for j in range(2):
#             print(inventory[(i, j)])
    # for each_row in zip(*([i] + (j)
    #     for i, j in inventory.items())):
    #         print(*each_row, " ")

print_table(inventory={"rope": 1, "torch": 2})







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


# print(add_to_inventory({"rope": 1, "torch": 2}, ["rope", "rope"]))
# print(import_inventory(inventory = {"rope": 1, "torch": 2}))

def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass
