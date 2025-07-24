# Calculator
✅ 1. Importing the Library
python
Copy
Edit
import tkinter as tk
tkinter is the standard Python library for creating Graphical User Interfaces (GUIs).

We use tk as an alias for easy reference.

✅ 2. Functions Used
a) update_display(value)
python
Copy
Edit
def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)
Purpose: Updates the calculator display when a button is clicked.

If the display shows 0, replace it with the new value.

Otherwise, append the new value to the current display text.

b) clear_display()
python
Copy
Edit
def clear_display():
    display_var.set("0")
Resets the calculator display to 0.

c) calculate_result()
python
Copy
Edit
def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")
Evaluates the expression entered by the user using eval().

Displays the result on the screen.

If an error occurs (like invalid syntax), it shows "Error".

⚠ Note: Using eval() is risky for security because it can execute arbitrary code. For a real app, use a safe math parser.

✅ 3. Creating Main Window
python
Copy
Edit
root = tk.Tk()
root.title("Calculator")
tk.Tk() creates the main application window.

root.title("Calculator") sets the window title.

✅ 4. Display Area
python
Copy
Edit
display_var = tk.StringVar()
display_var.set("0")

display_label = tk.Label(root, textvariable=display_var, font=("Arial", 24), anchor="e", bg="lightgray", padx=10, pady=10)
display_label.grid(row=0, column=0, columnspan=4)
display_var: A StringVar that stores the current display text dynamically.

display_label: A Label widget showing the text (connected to display_var).

anchor="e" aligns text to the right (like real calculators).

Placed on row 0, spanning 4 columns.

✅ 5. Button Layout
python
Copy
Edit
button_layout = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]
A list of tuples defining button text and grid position (row, column).

✅ 6. Creating Buttons
python
Copy
Edit
for (text, row, col) in button_layout:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                       command=lambda t=text: update_display(t) if t != "=" else calculate_result())
    button.grid(row=row, column=col)
Creates buttons dynamically for each item in button_layout.

lambda t=text: ensures the correct value is passed to the function when clicked.

If the button is "=", it calls calculate_result(). Otherwise, it updates the display.

✅ 7. Clear Button
python
Copy
Edit
clear_button = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 18), command=clear_display)
clear_button.grid(row=5, column=0, columnspan=3)
A special Clear button (C) placed in row 5, spanning 3 columns.

Calls clear_display() to reset the screen.

✅ 8. Start Event Loop
python
Copy
Edit
root.mainloop()
Keeps the GUI running and responsive until the user closes it.
