import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        # Entry for displaying input and results
        self.entry = ttk.Entry(root, font=('Arial', 18), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('log', 5, 2), ('exp', 5, 3)
        ]

        for (text, row, col) in buttons:
            ttk.Button(root, text=text, command=lambda t=text: self.button_click(t)).grid(row=row, column=col, sticky='nsew')

        # Configure row and column weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        current_text = self.entry.get()

        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == '√':
            try:
                result = math.sqrt(float(current_text))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == 'log':
            try:
                result = math.log10(float(current_text))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == 'exp':
            try:
                result = math.exp(float(current_text))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
