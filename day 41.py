mydictionary = {"name": None, "url": None, "des": None, "rate": None}

for name, value in mydictionary.items():
    mydictionary[name] = input(f"{name}:")

for name,value in mydictionary.items():
    print(f"{name}:{value}")