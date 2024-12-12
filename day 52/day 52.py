import os
import time

folder_path = r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 52"
file_path = os.path.join(folder_path, "pizza.txt")

order = {"name": [], "toppings": [], "size": [], "quantity": [], "total": []}

try:
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split('| ')
                if len(parts) == 5:
                    name, toppings, size, quantity, total = parts
                    order["name"].append(name)
                    order["toppings"].append(toppings)
                    order["size"].append(size)
                    order["quantity"].append(int(quantity))
                    order["total"].append(float(total))
except Exception as e:
    print(f"Error loading file: {e}")

while True:
    try:
        item = int(input("1: Add pizza\n2: View pizzas\n> "))
        if item == 1:
            name = input("Name on the order: ")
            toppings = input("Toppings: ")
            size = input("Size (L,M,S): ")
            try:
                quantity = int(input("How many pizzas?: "))
                total = quantity * 5.99

                order["name"].append(name)
                order["toppings"].append(toppings)
                order["size"].append(size)
                order["quantity"].append(quantity)
                order["total"].append(total)

                try:
                    with open(file_path, "a") as f:
                        f.write(f"{name}| {toppings}| {size}| {quantity}| {total}\n")
                except Exception as e:
                    print(f"Error saving file: {e}")
            except ValueError:
                print("Invalid input for quantity. Please enter a number.")
        elif item == 2:
            print("All Pizza Orders:")
            for i in range(len(order["name"])):
                print(f"Order {i+1}: Name - {order['name'][i]}, Toppings - {order['toppings'][i]}, Size - {order['size'][i]}, Quantity - {order['quantity'][i]}, Total - ${order['total'][i]:.2f}")

        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
