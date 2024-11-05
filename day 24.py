import random

def diceroll(sides):
    while True:
        roll = random.randint(1, sides)
        print("You rolled",roll)
        
        Q1 = input("Would you like to roll again? (yes/no) > ")
        if Q1 == "yes":
            continue
        else:
            print("Thank you for playing!")
            break

print("====== Let's roll the dice! ======")
sides = int(input("How many sides do you want to roll? > "))
diceroll(sides)
