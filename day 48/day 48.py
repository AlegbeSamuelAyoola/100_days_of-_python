import os,time

while True:
    print("HIGH SCORE TABLE")
    print()
    folder_path = r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 48"
    file_path = os.path.join(folder_path, "high.score")
    f = open(file_path, "a+")
    time.sleep(1)
    playername = input("INITIALS > ")
    time.sleep(1)
    playerscore = input("SCORE > ")
    time.sleep(1)
    print()
    print("ADDED")
    f.write(f"{playername} {playerscore}\n")
    f.close()
    time.sleep(2)
    os.system('cls')