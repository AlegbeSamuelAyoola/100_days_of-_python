import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(event):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')

# Setting up the main window
window = tk.Tk()
window.title("Simple Calculator")

entry = tk.Entry(window, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Button click function
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

# Button creation
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

# Positioning buttons in the grid
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, width=10, height=3, command=lambda: evaluate_expression(None)).grid(row=row, column=col, columnspan=2)
    else:
        tk.Button(window, text=button, width=5, height=3, command=lambda button=button: button_click(button)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Binding the 'Enter' key to evaluate the expression
window.bind('<Return>', evaluate_expression)

window.mainloop()
