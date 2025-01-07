import os
import time
import random

# Initialize the lists
todo = []
listOfEmail = []

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls')

def newPrint(color, word):
    """Print the word in the specified color."""
    colors = {"red": "\033[31m", "green": "\033[32m", "blue": "\033[34m"}
    print(colors.get(color, "\033[0m"), word, sep="", end="")

def rollDice(sides):
    """Simulate rolling a dice with a specified number of sides."""
    while True:
        number = random.randint(1, sides)
        print(number)
        print()
        thing = input("Roll again? (yes/no): ")
        if thing.lower() == "no":
            break

def prettyPrint():
    """Print the list of emails."""
    clear_screen()
    print("listOfEmail")
    print()
    for idx, email in enumerate(listOfEmail, start=1):
        print(f"{idx}: {email}")
    time.sleep(1)

def remove():
    """Remove a todo item by its name."""
    time.sleep(1)
    clear_screen()
    find = input("Name of todo to remove > ")
    for row in todo:
        if find in row:
            todo.remove(row)
            print(f"Removed: {find}")
            break
    else:
        print(f"Todo item '{find}' not found.")

def view():
    """View todo items, either all or by priority."""
    time.sleep(1)
    clear_screen()
    options = input("1: All\n2: By Priority\n> ")
    if options == "1":
        for row in todo:
            print(" | ".join(row))
    else:
        priority = input("What priority? > ").capitalize()
        for row in todo:
            if priority in row:
                print(" | ".join(row))
    time.sleep(1)

def edit():
    """Edit an existing todo item."""
    time.sleep(1)
    clear_screen()
    find = input("Name of todo to edit > ")
    for row in todo:
        if find in row:
            todo.remove(row)
            name = input("Name > ")
            date = input("Due Date > ")
            priority = input("Priority > ").capitalize()
            todo.append([name, date, priority])
            print(f"Edited: {find}")
            return
    print(f"Couldn't find todo item '{find}'.")

def add():
    """Add a new todo item."""
    time.sleep(1)
    clear_screen()
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority > ").capitalize()
    todo.append([name, date, priority])
    print("Added")

