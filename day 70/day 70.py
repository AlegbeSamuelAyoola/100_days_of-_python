from dotenv import load_dotenv
import os
import getpass

# Load environment variables from .env file
load_dotenv()
user = os.getenv('user')
admin = os.getenv('admin')
userpassword = os.getenv('userpassword')
adminpassword = os.getenv('adminpassword')

while True:
    print("Enter 'exit' as the username to quit.")
    username = input("Username> ")
    if username.lower() == "exit":
        print("Goodbye!")
        break
    
    if username == user:
        userpass = getpass.getpass("Password> ")  # Hide password input
        if userpass == userpassword:
            print("Welcome User")
        else:
            print("Incorrect Credentials")
    elif username == admin:
        adminpass = getpass.getpass("Password> ")  # Hide password input
        if adminpass == adminpassword:
            print("Welcome Admin")
        else:
            print("Incorrect Credentials")
    else:
        print("Username not recognized.")
