import tkinter as tk

# Function to update the display
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to evaluate the final expression
def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

# Function to clear the display
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("280x450")
root.configure(bg="light blue")

# StringVar to store the input expression
input_text = tk.StringVar()
expression = ""

# Entry widget to display the input expression
input_entry = tk.Entry(root, textvariable=input_text, font=("Arial", 20, "bold"), bd=5, insertwidth=4, width=10, bg="powder blue", justify="right")
input_entry.grid(row=0, column=0, columnspan=4)

# Buttons for digits and operators
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+')
]

# Create buttons and place them on the window
row_num = 1
col_num = 0
for row in buttons:
    for button_text in row:
        button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 15, "bold"), bg="light blue", command=lambda x=button_text: button_click(x))
        button.grid(row=row_num, column=col_num)
        col_num += 1
    row_num += 1
    col_num = 0

# Create equal and clear buttons
equal_button = tk.Button(root, text="=", padx=20, pady=20, font=("Arial", 15, "bold"), bg="yellow", command=button_equal)
equal_button.grid(row=5, column=0, columnspan=2)

clear_button = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 15, "bold"), bg="yellow", command=button_clear)
clear_button.grid(row=5, column=2, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
