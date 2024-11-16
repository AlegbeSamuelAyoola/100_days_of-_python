import random

def greet():
    gr = ["Hello there!" #english
          ,"Hola!" #spanish
          ,"Ahlaan bik!" #Arabic
          ,"Bonjur!" #french
          ,"Henle nibe yen!" #yoruba
          ]
    greeting = random.choice(gr)
    return greeting

title = "====== Hello in Different Languages ======"
print(f"{title}".center(170))
print()
print(f"{greet()}".center(170))
print()

1 = input("name")

