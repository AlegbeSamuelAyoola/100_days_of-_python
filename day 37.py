print("STAR WARS NAME GENERATOR")

while True:
    firstname = input("Enter your first name > ")
    lastname = input("Enter your last name > ")
    maidenname = input("Enter your mother's maiden name > ")
    city = input("Enter the city you were born > ")

    firststar = f"{firstname[:3].capitalize()}{lastname[:3].lower()}"
    secondstar = f"{maidenname[:2].capitalize()}{city[-3:].lower()}"
    
    starname = f"{firststar} {secondstar}"
    print(f"Your Star Wars name is: {starname}")
    
