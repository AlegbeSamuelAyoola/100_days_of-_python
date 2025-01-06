import dbm
import datetime

def Add(db):
    entry = input("Type your thoughts: ")
    timestamp = datetime.datetime.now()
    key = f"content_{timestamp}"
    db[key] = entry
    print("Entry added!")

def View(db):
    keys = list(db.keys())
    keys.sort(reverse=True)
    for key in keys:
        if key.startswith(b'content'):
            print(f"{key.decode('utf-8')}: {db[key].decode('utf-8')}")
            option = input("Next or exit: ").strip().lower()
            if option == "exit":
                break

password = "Mylife"

guess = input("What's the password? ").strip().capitalize()
if password != guess:
    print("Incorrect password.")
    exit()
else:
    print("Welcome!")
    with dbm.open('diary', 'c') as db:
        while True:  
            menu = input("Add or View? ").strip().title()
            if menu == "Add":
                Add(db)
                continue
            elif menu == "View":
                View(db)
                continue
            else:
                print("Invalid option. Please choose 'Add' or 'View'.")
