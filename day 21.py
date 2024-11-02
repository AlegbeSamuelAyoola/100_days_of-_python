print("====== Multiplication Table ======")
multiple = int(input("Name your number to be multiplied? > "))
counter = 0
for i in range (1,11):
    user_answer = int(input(f"What is {multiple} * {i}? > "))
    correct_answer = multiple * i
    if user_answer == correct_answer:
        counter +=1
        print("Thats the correct answer!")
    else:
        print("Incorrect answer, the answer is",correct_answer)
print("You got",counter,"out of 10 correct!")