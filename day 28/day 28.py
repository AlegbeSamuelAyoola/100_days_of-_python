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

def battle_die_roll():
    broll = diceroll(6) 
    return broll

while True:
    print("      ⚔️ BATTLE ROYAL ⚔️      ")
    time.sleep(1)
    name1 = input("Name your Legend > \n")
    print()
    character1 = input("Enter your Character Type (Human,Elf,Wizard,Orc)\n")
    print()
    time.sleep(1)
    print("NAME:",name1)
    time.sleep(1)
    print("RACE:",character1)
    time.sleep(1)
    hp1 = health()
    print("HEALTH:",hp1)
    time.sleep(1)
    str1 = strength()
    print("STRENGTH:",str1)
    print()
    time.sleep(1)
    print("      Who will be their opponent?      ")
    time.sleep(1)
    print()
    name2 = input("Name your Legend > \n")
    print()
    character2 = input("Enter your Character Type (Human,Elf,Wizard,Orc)\n")
    print()
    time.sleep(1)
    print("NAME:",name2)
    time.sleep(1)
    print("RACE:",character2)
    time.sleep(1)
    hp2 = health()
    print("HEALTH:",hp2)
    time.sleep(1)
    str2 = strength()
    print("STRENGTH:",str2)
    time.sleep(1)
    print()
    os.system('cls')

    print("      ⚔️   BATTLE TIME   ⚔️      ")
    print()
    print("The Battle Begins")
    round = 1
    while True:
        str1 = strength()
        str2 = strength()
        hp1 = health()
        hp2 = health()
        roll1 = battle_die_roll()
        roll2 = battle_die_roll()
        if roll1 < roll2:
            damage = ((str2 - str1) + (1))
            hp1 -= damage
            print(name1,"Rolls",roll1)
            print(name2,"Rolls",roll2)
            print(name1,"HEALTH:",hp1)
            print(name2,"HEALTH:",hp2)
            print(name2,"Wins Round",round)
            time.sleep(3)
            os.system('cls')
        elif roll1 == roll2:
            print(name1,"Rolls",roll1)
            print(name2,"Rolls",roll2)
            print(name1,"HEALTH:",hp1)
            print(name2,"HEALTH:",hp2)
            print("Draw!",round)
            time.sleep(3)
            os.system('cls')
        elif roll2 < roll1:
            damage = ((str1 - str2) + (1) )
            hp2 -= damage
            print(name1,"Rolls",roll1)
            print(name2,"Rolls",roll2)
            print(name1,"HEALTH:",hp1)
            print(name2,"HEALTH:",hp2)
            print(name1,"Wins Round",round)
            time.sleep(3)
            os.system('cls')

        if hp1 <= 0:
            print(name1,"Rolls",roll1)
            print(name2,"Rolls",roll2)
            print(name1,"HEALTH:",hp1)
            print(name2,"HEALTH:",hp2)
            print(name1,"Has Died!")
            print()
            print(name2,"Has Won! After",round,"Rounds!")
            break
        elif hp2 <= 0:
            print(name1,"Rolls",roll1)
            print(name2,"Rolls",roll2)
            print(name1,"HEALTH:",hp1)
            print(name2,"HEALTH:",hp2)
            print(name2,"Has Died!")
            print(name1,"Has Won! After",round,"Rounds!")
            break
        round += 1
    exit()

