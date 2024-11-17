mytodo = []

def todolist():
    for item in mytodo:
        print(item)

print(f"\033[0;32m TODO LIST MANAGER\033[0m".center(140))

while True:
    #menu options = view, add, remove, edit and replace on special condition
    menu = input(f"""\033[0;36m Do you want to view, add, remove or edit the list?\033[0m \n\033[0;31m PRESS 'F' TO CLEAR THE TODO LIST\033[0m \n >>> """)
    if menu == "add":
        item = input(f"\033[0;36m What do you want to add to the list? >\033[0m \n ")
        if item in mytodo:
            print(f"{item}is already in the todo list")
        else:
            mytodo.append(item)
    elif menu == "view":
        print(f"\033[0;32m This is the current list >\033[0m \n ")
        todolist()
    elif menu == "edit":
        item = input(f"\033[0;32m What do you want to edit? >\033[0m \n ")
        if item in mytodo:
            mytodo.remove(item)
            replace = input("What do you want to replace it with? > ")
            mytodo.append(replace)
        else: 
            print("Item not found in todo list.")
        continue 
    elif menu == "remove":
        item = input("What do you want to remove? ")   
        if item in mytodo:
            rremove = input(f"\033[0;31mDo you really want to remove {item} from the todo list?\033[0m > \n")
            if rremove == "yes" or rremove == "Yes":
                mytodo.remove(item)
            else:
                continue
        else:
            print("Item not found in todo list")
        continue
    elif menu == "F" or menu == "f":
        mytodo.clear()
    else:
        print("This is not in the menu")
        continue