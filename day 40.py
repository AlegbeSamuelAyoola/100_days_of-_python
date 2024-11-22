print(f"====== Contact Card Generator  ======".center(80))
name = input("Name: ")
DOB = input("Date of Birth: ")
pnumber = input("Phone Number: ")
email = input("Email Address: ")
address = input("House Address: ")

userinfo = {"name":name, "DOB":DOB, "pnumber":pnumber, "email":email, "address":address}

print()
print("-------------------------------------------------------".center(80))
print()
print("Here's your contact card".center(80))
print(f"Name: {userinfo['name']}")
print(f"Date of Birth: {userinfo['DOB']}")
print(f"Phone Number: {userinfo['pnumber']}")
print(f"Email Address: {userinfo['email']}")
print(f"House Address: {userinfo['address']}")    