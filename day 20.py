print("====== List Generator ======")
start_num = int(input("What number will you like the list to start at? > "))
print()
end_num = int(input("What number would like the list to end before? > "))
print()
incrment = int(input("What would you like the increment between values to be? > "))
print()
for i in range (start_num,end_num,incrment):
    print(i)