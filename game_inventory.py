import csv
from io import SEEK_CUR
from multiprocessing.sharedctypes import Value
import pprint
from re import T
from selectors import SelectorKey
from turtle import rt

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

def print_table(inventory, order="count,desc"):

# item name min a characterek hossza
# leghosszabb inventory elem hossza
    key_column_length = len("item name")
    for key, value in inventory.items():
        if len(key) > len("item name"):
            key_column_length = len(key)
# ehhez 3 plusz karakter ami 2 spce közte | jel 
# count hossza vagy a legghosszabb value érték hossza
    value_column_length = len("count")
    for key, value in inventory.items():
        if len(str(value)) > len("count"):
            value_column_length = len(str(value))
# ez adja a tábla felső és alsó dashed line hosszáT
# eközött fejléc elnevezéSEk 
# és jobbra zárt
    dashed_line = "-" * key_column_length + "-" * 3 + "-" * value_column_length
    diff_item_name = max(0, key_column_length - len("item name"))
    diff_count = max(0, value_column_length - len("count"))
    header = diff_item_name * " " + "item name" + " | " + diff_count * " " + "count"
    print(dashed_line)
    print(header)
    print(dashed_line)

# itt jön a törzs, a dict átalakítva key-value párként, hozzárendelve a keyben lévő elemeket az item name column alá
# value elemeket alárendelve a count column alá
# jobbra zártan
# először nyomtassa ki a keyt, majd elválasztó vonl majd a Value
# kiigazitani végül, hogy a | középen legyen hol a headerben is
    if order == "count,desc":
        ordered_inventory = dict(sorted(inventory.items(), key=lambda item: item[1], reverse = True))
    else:
        ordered_inventory = dict(sorted(inventory.items(), key=lambda item: item[1], reverse = False))

    for key, value in ordered_inventory.items():
        diff_key = key_column_length - len(key)
        diff_value = value_column_length - len(str(value))
        print(diff_key * " " + key + " | " + diff_value * " " + str(value))

    print(dashed_line)


print_table(inventory={"rope": 4, "torch": 2})




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

# with open('test_inventory.csv', newline='') as csvfile:
# ...     reader = csv.DictReader(csvfile)
# ...     for row in reader:

#             row.sort()
# ...       print(row['item_name'], row['count'])


# print(add_to_inventory({"rope": 1, "torch": 2}, ["rope", "rope"]))
# print(import_inventory(inventory = {"rope": 1, "torch": 2}))

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


