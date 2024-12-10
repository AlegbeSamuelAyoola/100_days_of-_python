import os,time,random

folder_path = r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 50"
file_path = os.path.join(folder_path, "my.ideas")
f = open(file_path, "r")


contents = f.readlines()

ideas = [line.strip() for line in contents]

while True:
    print("IDEAS")
    print()
    time.sleep(1)
    print("1: Add an Idea")
    print("2: Load up a random idea")
    Q1 = int(input("> "))
    print()
    if Q1 == 1:
        add = input("1: ")
        with open(file_path, "a") as f:
            f.writelines(add + "\n")
        ideas.append(add)
    elif Q1 == 2:
        ridea = random.choice(ideas)
        print(f"Random idea: {ridea}")
    time.sleep(3)
    os.system('cls')

