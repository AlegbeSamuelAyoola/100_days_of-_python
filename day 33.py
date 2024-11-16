mytodo = []

def todolist():
    for item in mytodo:
        print(item)

print(f"\033[0;32m TODO LIST MANAGER\033[0m".center(140))

while True:
    #menu options = view, add, edit and replace on special condition
    menu = input("\033[0;36m Do you want to view, add or edit the list? >\033[0m \n")
    if menu == "add":
        item = input(f"\033[0;36m What do you want to add to the list? >\033[0m \n")
        mytodo.append(item)
    elif menu == "view":
        print(f"\033[0;32m This is the current list >\033[0m \n")
        todolist()
    elif menu == "edit":
        item = input("\033[0;32m What do you want to edit? >\033[0m \n")
        if item in mytodo:
            mytodo.remove(item)
            replace = input("What do you want to replace it with? > ")
            mytodo.append(replace)
        else: 
            print("Item not found in the list.")
        continue    
    else:
        print("This is not in the menu")
        continue