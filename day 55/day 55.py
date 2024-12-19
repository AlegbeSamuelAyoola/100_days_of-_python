import os
import time

folder_path = r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 55"
file_path = os.path.join(folder_path, "to.do")

backup_folder_path = r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 55 backup"
backup_file_path = os.path.join(backup_folder_path, "to.do")

mytodolist = {"tasks": [], "due": [], "priority": {"high": [], "medium": [], "low": []}}

if os.path.exists(file_path):
    with open(file_path, "r") as f:
       for line in f:
           item, duedate, importance = line.strip().split(', ')
           mytodolist["tasks"].append(item)
           mytodolist["due"].append(duedate)
           mytodolist["priority"][importance].append(item)

mytodo = mytodolist["tasks"]
due = mytodolist["due"]
priority = mytodolist["priority"]

def todolist():
    for i, item in enumerate(mytodo):
        print(f"{item} (Due: {due[i]})")

print(f"\033[0;32m TODO LIST MANAGEMENT SYSTEM\033[0m".center(140))

while True:
    menu = input("\033[0;36m Do you want to view, add, or edit the list? >\033[0m \n").lower()
    if menu == "add":
        item = input(f"\033[0;36m What do you want to add to the list? >\033[0m \n")
        mytodo.append(item)
        duedate = input(f"\033[0;36m When is it due? >\033[0m \n")
        due.append(duedate)
        importance = input(f"\033[0;36m How important is it (high, medium, low)? >\033[0m \n").lower()
        if importance in priority:
            priority[importance].append(item)
        print("Added to List!")
        
        # Save to both primary and backup files
        with open(file_path, "a") as f, open(backup_file_path, "a") as backup_f:
            f.write(f"{item}, {duedate}, {importance}\n")
            backup_f.write(f"{item}, {duedate}, {importance}\n")
    
    elif menu == "view":
        view_list = input(f"\033[0;32m View all or View priority? >\033[0m \n").lower()
        if view_list == "view all":
            todolist()
        elif view_list == "view priority":
            wpriority = input("High, Medium, or Low? \n").lower()
            if wpriority in priority:
                print(f"Items with {wpriority} priority: ")
                for item in priority[wpriority]:
                    print(item)
            else:
                print(f"No items with {wpriority} priority found.")
    
    elif menu == "edit":
        item = input("\033[0;32m What do you want to edit? >\033[0m \n")
        if item in mytodo:
            index = mytodo.index(item)
            new_item = input("What do you want to replace it with? > ")
            mytodo[index] = new_item
            due[index] = input("When is it due? > ")
            importance = input(f"\033[0;36m How important is it (high, medium, low)? >\033[0m \n").lower()
            for level in priority:
                if item in priority[level]:
                    priority[level].remove(item)
            priority[importance].append(new_item)
        else:
            print("Item not found in the list.")
        continue    
    else:
        print("This is not in the menu")
        continue
    
    mytodolist = {"tasks": mytodo, "due": due, "priority": priority}

    # Save the updated list to both primary and backup files
    with open(file_path, "w") as f, open(backup_file_path, "w") as backup_f:
        for task, duedate in zip(mytodolist["tasks"], mytodolist["due"]):
            for priority_level, items in mytodolist["priority"].items():
                if task in items:
                    f.write(f"{task}, {duedate}, {priority_level}\n")
                    backup_f.write(f"{task}, {duedate}, {priority_level}\n")
    
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
