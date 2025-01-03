import datetime

today = datetime.date.today()

print("Event Countdown")

event = input("Enter the Event: ")
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

date = datetime.date(year, month, day)
difference = (date - today).days

if date > today:
    print(f"Coming Soon! Only {difference} days remain until {event}.")
elif date < today:
    print(f"Oh no! You missed the {event} by {-difference} days.")
else:
    print(f"Today's the big day for {event}!")
