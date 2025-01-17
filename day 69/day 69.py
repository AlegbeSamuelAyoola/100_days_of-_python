import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys

def start_game():
    global current_scene
    current_scene = "start"
    display_scene(current_scene)

def display_scene(scene):
    global current_scene
    current_scene = scene

    if scene == "start":
        image_label.config(image=start_image)
        text_label.config(
            text="You find yourself in a dark forest. Two paths lie ahead: "
                 "one shrouded in shadows and the other dappled with light. "
                 "Which path will you choose?"
        )
        button1.config(text="Take the left path", command=lambda: display_scene("left_path"))
        button2.config(text="Take the right path", command=lambda: display_scene("right_path"))
        button2.pack()
    elif scene == "left_path":
        image_label.config(image=left_path_image)
        text_label.config(
            text="As you walk along the left path, you encounter a friendly fox. "
                 "The fox speaks, 'Greetings, traveler! I can guide you out of the forest safely, "
                 "but only if you trust me.'"
        )
        button1.config(text="Accept the fox's help", command=lambda: display_scene("good_ending"))
        button2.config(text="Decline the fox's help", command=lambda: display_scene("bad_ending"))
        button2.pack()
    elif scene == "right_path":
        image_label.config(image=right_path_image)
        text_label.config(
            text="The right path is treacherous. Suddenly, you spot a trap hidden among the leaves. "
                 "It looks dangerous, but you might have a chance to disarm it."
        )
        button1.config(text="Attempt to disarm the trap", command=lambda: display_scene("good_ending"))
        button2.config(text="Run away from the trap", command=lambda: display_scene("bad_ending"))
        button2.pack()
    elif scene == "good_ending":
        image_label.config(image=good_ending_image)
        text_label.config(
            text="Congratulations! With courage and quick thinking, you made it out of the forest safely. "
                 "The forest now seems less menacing as the sunlight streams through the trees. Well done!"
        )
        button1.config(text="Play Again", command=start_game)
        button2.pack_forget()
    elif scene == "bad_ending":
        image_label.config(image=bad_ending_image)
        text_label.config(
            text="Oh no! Your choices have led to an unfortunate end. The forest grows darker, "
                 "and you feel the weight of danger looming. Perhaps you'll have better luck next time."
        )
        button1.config(text="Try Again", command=start_game)
        button2.pack_forget()

root = tk.Tk()
root.title("Simple Visual Novel")
root.geometry("600x600")

# Load and resize images
try:
    start_image = ImageTk.PhotoImage(Image.open(r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 69\start.png").resize((400, 300)))
    left_path_image = ImageTk.PhotoImage(Image.open(r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 69\left_path.png").resize((400, 300)))
    right_path_image = ImageTk.PhotoImage(Image.open(r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 69\right_path.png").resize((400, 300)))
    good_ending_image = ImageTk.PhotoImage(Image.open(r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 69\good_ending.png").resize((400, 300)))
    bad_ending_image = ImageTk.PhotoImage(Image.open(r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 69\bad_ending.png").resize((400, 300)))
except FileNotFoundError as e:
    messagebox.showerror("Error", f"Image not found: {e}")
    root.quit()
    sys.exit()  # Ensures the program exits gracefully

# Create UI elements
image_label = tk.Label(root)
image_label.pack(pady=10)

text_label = tk.Label(root, text="", wraplength=500, pady=10, font=("Helvetica", 14))
text_label.pack()

button1 = tk.Button(root, text="", width=25, pady=5, font=("Helvetica", 12))
button1.pack(pady=5)
button2 = tk.Button(root, text="", width=25, pady=5, font=("Helvetica", 12))
button2.pack(pady=5)

# Start the game
start_game()

root.mainloop()
