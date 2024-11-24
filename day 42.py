mydictionary = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("MokeBeast")
for name, value in mydictionary.items():
    mydictionary[name] = input(f"{name}:")
print()
for name,value in mydictionary.items():
    beast_type = mydictionary["Type"].lower()
    if beast_type == "water":
        print(f"\033[1;34m{name}:{value}\033[0m")
    elif beast_type == "fire":
        print(f"\033[1;31m{name}:{value}\033[0m")
    elif beast_type == "electric":
        print(f"\033[1;33m{name}:{value}\033[0m")
        