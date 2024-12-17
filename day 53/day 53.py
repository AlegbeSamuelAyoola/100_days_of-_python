import os
from ast import literal_eval

inventory = []

folder_path = r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 53"
file_path = os.path.join(folder_path, "inventory.txt")

try:
    with open(file_path, "r") as f:
        inventory = literal_eval(f.read())
except:
    print("ERROR: No existing inventory list, using a blank list")
os.system('cls')

def inventorylist():
    inventory_summary = {}
    for item in inventory:
        inventory_summary[item] = inventory_summary.get(item, 0) + 1
    for item, count in inventory_summary.items():
        print(f"{item}: {count}")

print(f"\033[0;32m INVENTORY\033[0m".center(140))

while True:
    #menu options = view, add, remove, edit and replace on special condition
    menu = input(f"""\033[0;36m Do you want to view, add, remove or edit the list?\033[0m \n\033[0;31m PRESS 'F' TO CLEAR THE INVENTORY\033[0m \n >>> """)
    if menu == "add":
        item = input(f"\033[0;36m What do you want to add to the inventory? >\033[0m \n ").capitalize()
        inventory.append(item)
    elif menu == "view":
        print(f"\033[0;32m This is the current list >\033[0m \n ")
        inventorylist()
    elif menu == "edit":
        item = input(f"\033[0;32m What do you want to edit? >\033[0m \n ")
        if item in inventory:
            inventory.remove(item)
            replace = input("What do you want to replace it with? > ")
            inventory.append(replace)
        else: 
            print("Item not found in the inventory.")
        continue 
    elif menu == "remove":
        item = input("What do you want to remove? ")   
        if item in inventory:
            rremove = input(f"\033[0;31mDo you really want to remove {item} from the inventory?\033[0m > \n")
            if rremove == "yes" or rremove == "Yes":
                inventory.remove(item)
            else:
                continue
        else:
            print("Item not found in the inventory")
        continue
    elif menu == "F" or menu == "f":
        inventory.clear()
    else:
        print("This is not in the menu")
        continue
    with open(file_path, "w") as f:
        f.write(str(inventory))
    print("Inventory successfully saved to file!")
