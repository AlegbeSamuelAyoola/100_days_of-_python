import os,time,random

top_trumps = {
    "Lion": {
        "Speed": 80,
        "Strength": 90,
        "Intelligence": 70
    },
    "Elephant": {
        "Speed": 40,
        "Strength": 100,
        "Intelligence": 60
    },
    "Cheetah": {
        "Speed": 120,
        "Strength": 70,
        "Intelligence": 50
    }
}

def obj1_stat():
    print()
    stat = input("Choose stat to compare (Speed, Strength, Intelligence)\n>").capitalize()
    print()
    return stat

def compare_stats(obj1, obj2, stat):
    if top_trumps[obj1][stat] > top_trumps[obj2][stat]:
        print()
        print(f"{obj1} wins in {stat}!")
    elif top_trumps[obj1][stat] < top_trumps[obj2][stat]:
        print()
        print(f"{obj2} wins in {stat}!")
    else:
        print()
        print(f"It's a tie in {stat}!")


while True:
    print("Top Trumps")
    print("-------------")
    print("Characters")
    print()
    print("Lion\nElephant\nCheetah\n")
    time.sleep(1)
    obj1 = input("Pick your Character\n>").title()
    time.sleep(1)
    print()
    obj2 =  random.choice(list(top_trumps.keys()))
    print(f"Computer has picked {obj2}")
    time.sleep(1)
    stat = obj1_stat()
    compare_stats(obj1, obj2, stat)
    time.sleep(1)
    play_again = input("do you want to play again?\n>").lower()
    if play_again.lower() == "yes":
        os.system('cls')
        continue
    else:
        break