import dbm, random, os, time, hashlib, datetime

def menu():
    print()
    print("Login System")
    print("1: Add a user\n2: Login")
    print()
    menuChoice = int(input("> "))
    if menuChoice == 1:
        add_user()
    elif menuChoice == 2:
        login()
    else:
        print("You will return to the menu")
        time.sleep(2)
        os.system('cls')
        menu()

def add_user():
    time.sleep(2)
    os.system('cls')
    username = input("What should your username be? ")
    password = input("What should your password be? ")
    salt = str(random.randint(1000, 9999))
    newPassword = hashlib.sha256(f"{password}{salt}".encode()).hexdigest()
    
    with dbm.open('user_db', 'c') as db:
        db[username] = f"{newPassword}:{salt}"
    
    print("User added successfully! You will return to the menu.")
    time.sleep(3)
    os.system('cls')
    menu()

def login():
    time.sleep(2)
    os.system('cls')
    username = input("What is the username? ")
    password = input("What is the password? ")

    with dbm.open('user_db', 'c') as db:
        if username in db:
            stored_password, salt = db[username].decode().split(':')
            login_password = hashlib.sha256(f"{password}{salt}".encode()).hexdigest()
            
            if login_password == stored_password:
                print("LOGIN SUCCESSFUL")
                diary_menu()
            else:
                print("Login not successful")
        else:
            print("User not found")
    
    time.sleep(3)
    os.system('cls')
    menu()

def diary_menu():
    while True:
        menu = input("Add or View? ").strip().title()
        if menu == "Add":
            add_entry()
        elif menu == "View":
            view_entries()
        else:
            print("Invalid option. Please choose 'Add' or 'View'.")

def add_entry():
    entry = input("Type your thoughts: ")
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    key = f"content_{timestamp}"
    with dbm.open('diary', 'c') as db:
        db[key] = entry.encode('utf-8')
    print("Entry added!")

def view_entries():
    with dbm.open('diary', 'c') as db:
        keys = list(db.keys())
        keys.sort(reverse=True)
        for key in keys:
            if key.decode().startswith('content'):
                print(f"{key.decode('utf-8')}: {db[key].decode('utf-8')}")
                option = input("Next or exit: ").strip().lower()
                if option == "exit":
                    break

menu()
