import time
import os

listofemails = []

def prettyprint():
    os.system('cls')
    print("listOfEmail")
    print()
    counter = 1
    for email in listofemails:
        print(f"{counter}: {email}")
        counter += 1
    time.sleep(1)

while True:
    print("SPAMMER Inc.")
    print()
    menu = input(f"1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n >  ")
    if menu == "1":
        email = input("Email > \n")
        listofemails.append(email)
    elif menu == "2":
        email = input("Email > \n")
        if email in listofemails:
            listofemails.remove(email)
        else:
            print("Email not found in the list.")
    elif menu == "3":
        prettyprint()
    elif menu == "4":
        counter = 0
        for email in listofemails:
            counter += 1
            if counter <= 10:
                os.system('cls')
                print(f"""Dear {email},
It has come to our attention that you're missing out on the amazing Replit 100 days of code.
We insist you do it right away. If you don't, we will pass on your email address to every spammer we've ever encountered
and also sign you up to the My Little Pony newsletter, because that's neat.
We might just do that anyway.

Love and hugs,
Ian Spammington III""")
                print()
                time.sleep(4)
                os.system('cls')
    else:
        print("This is not in the menu.")
