import time

print("30 Days Down - What did you think?")
print()

for i in range(1,31):
    time.sleep(2)
    print(f"Day {i} of 100")
    thought = input(f"What did you think of day {i}?\n")
    print(f"You thought day {i} was {thought}".center(40))
    print()