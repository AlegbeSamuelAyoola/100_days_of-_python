def login():
    while True:
        username = input("Enter your username > ")
        password = input("Enter your password > ")
        if username == "Goku" and password == "Vegita123":
            print("Login successful")
            break
        else:
            print("Login unsuccessful, try again")
        continue

print("====== BEERUS LOGIN SYSTEM ======")
login()