import dbm, random, os, time, hashlib

def menu():
    print()
    print("Login System")
    print("1: Add a user\n2: Login")
    print()
    menuChoice = int(input("> "))
    if menuChoice == 1:
        addUser()
    elif menuChoice == 2:
        login()
    else:
        print("You will return to the menu")
        time.sleep(2)
        os.system('cls')
        menu()

def addUser():
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
            else:
                print("Login not successful")
        else:
            print("User not found")
    
    time.sleep(3)
    os.system('cls')
    menu()

menu()
