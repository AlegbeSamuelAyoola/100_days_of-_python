mytodo = []
due = []
priority = {"high": [], "medium": [], "low": [] }

def todolist():
    for item in mytodo:
        print(item)

print(f"\033[0;32m TODO LIST MANAGEMENT SYSTEM\033[0m".center(140))

while True:
    #menu options = view, add, edit and replace on special condition
    menu = input("\033[0;36m Do you want to view, add or edit the list? >\033[0m \n")
    if menu == "add":
        item = input(f"\033[0;36m What do you want to add to the list? >\033[0m \n")
        mytodo.append(item)
        duedate = input(f"\033[0;36m When is it due? >\033[0m \n")
        due.append(duedate)
        importance = input(f"\033[0;36m How important is it? >\033[0m \n :")
        if importance in priority:
            priority[importance].append(item)    
        print("Added to List!")
    elif menu == "view":
        view_list = input(f"\033[0;32m View all or View priority? >\033[0m \n")
        if view_list == "view all":
            todolist()
        elif view_list == "view priority":
            wpriority = input("High, Medium, or Low? \n").lower()
            if wpriority in priority:
                print(f"Items with {wpriority} priority: ")
                for item in priority[wpriority]:
                    print(item)
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