import tkinter as tk
import math

def on_button_click(event):
    button_text = event.widget.cget("text")
    current_text = entry.get()

    if button_text == "AC":
        entry.delete(0, tk.END)
    elif button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "sqrt":
        try:
            result = math.sqrt(float(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "DEL":
        current_text = entry.get()
        updated_text = current_text[:-1]
        entry.delete(0, tk.END)
        entry.insert(tk.END, updated_text)
  
    else:
        entry.insert(tk.END, button_text)

# Create the main application window
root = tk.Tk()
root.title(" Calculator ")

# Entry widget to display and input expressions
entry = tk.Entry(root, font="Arial 20")
entry.grid(row=0, column=0, columnspan=5)

# Buttons for digits, operators, and functions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("AC", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("DEL", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("%" , 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("sqrt", 4, 4),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font="Arial 20", padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_button_click)

# Start the main event loop
root.mainloop()