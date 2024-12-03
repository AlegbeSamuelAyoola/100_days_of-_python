beastbook = {}

def prettyprint():
    print()
    for key, value in beastbook.items():
        print(key, end=" | ")
        for subkey, subvalue in value.items():
            print(subkey, end=": ")
            print(subvalue, end=" | ")
        print()

print("MokeBeast")

while True:
    beastname = input("Beast Name: ")
    type = input("Beast Type: ")
    specialmove = input("Special Move: ")
    mp = input("MP: ")
    hp = input("HP: ")
    beastbook[beastname] = {"Beast Type": type, "Special Move": specialmove, "MP": mp, "HP": hp}
    prettyprint()
        