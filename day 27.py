import random,time,os

def diceroll(sides):
    roll = random.randint(1,sides)
    return roll

def health():
    hp = ((diceroll(6) * diceroll(12))/2) + 10
    return hp

def strength():
    str = ((diceroll(6) * diceroll(12))/2) + 12
    return str

while True:
    print("====== Character Builder ======")
    time.sleep(1)
    name = input("Name your Legend > \n")
    print()
    character = input("Enter your Character Type (Human,Elf,Wizard,Orc)\n")
    print()
    time.sleep(1)
    print("NAME:",name)
    time.sleep(1)
    print("HEALTH:",health())
    time.sleep(1)
    print("STRENGTH:",strength())
    time.sleep(1)
    print("May Your Enemies Know Fear....")
    time.sleep(2)
    print()
    again = input("Would you like to go again?\n ")
    if again == "Yes" or again == "yes":
        os.system('cls')
        continue
    else:
        break