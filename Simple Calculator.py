import tkinter as tk

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(value))

def clear_display():
    display.delete(0, tk.END)

def evaluate_expression():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

window = tk.Tk()
window.title("Simple Calculator")

display = tk.Entry(window, width=20, font=("Arial", 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('C', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('/', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('-', 4, 3),
    ('=', 5, 0)
]

for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(window, text=text, width=10, height=2, font=("Arial", 18), command=clear_display)
    elif text == '=':
        btn = tk.Button(window, text=text, width=10, height=2, font=("Arial", 18), command=evaluate_expression)
    else:
        btn = tk.Button(window, text=text, width=10, height=2, font=("Arial", 18), command=lambda value=text: button_click(value))
    
    btn.grid(row=row, column=col)

window.mainloop()
