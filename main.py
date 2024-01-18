import tkinter as tk
from tkinter import ttk
import calculator_logic as calc

def enter_number(number):
    entry.insert(tk.END, number)

def set_operation(operation):
    global first
    global oper
    first = float(entry.get())
    oper = operation
    entry.delete(0, tk.END)

def calc():
    second = float(entry.get())
    if oper == '+':
        result = calc.add(first, second)
    elif oper == '-':
        result = calc.subtract(first, second)
    elif oper == '*':
        result = calc.multiply(first, second)
    elif oper == '/':
        result = calc.divide(first, second)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

def clear_entry():
    entry.delete(0, tk.END)

# Создаем окно приложения
window = tk.Tk()
window.title("Calculator")

entry = ttk.Entry(width=20)
entry.grid(row=0, column=0, columnspan=3)

# Цифровые кнопки
ttk.Button(text="1", command=lambda: enter_number('1')).grid(row=1, column=0)
ttk.Button(text="2", command=lambda: enter_number('2')).grid(row=1, column=1)
ttk.Button(text="3", command=lambda: enter_number('3')).grid(row=1, column=2)
ttk.Button(text="4", command=lambda: enter_number('4')).grid(row=2, column=0)
ttk.Button(text="5", command=lambda: enter_number('5')).grid(row=2, column=1)
ttk.Button(text="6", command=lambda: enter_number('6')).grid(row=2, column=2)
ttk.Button(text="7", command=lambda: enter_number('7')).grid(row=3, column=0)
ttk.Button(text="8", command=lambda: enter_number('8')).grid(row=3, column=1)
ttk.Button(text="9", command=lambda: enter_number('9')).grid(row=3, column=2)
ttk.Button(text="0", command=lambda: enter_number('0')).grid(row=4, column=0)

# Кнопки арифметических операций
ttk.Button(text="+", command=lambda: set_operation('+')).grid(row=1, column=3)
ttk.Button(text="-", command=lambda: set_operation('-')).grid(row=2, column=3)
ttk.Button(text="*", command=lambda: set_operation('*')).grid(row=3, column=3)
ttk.Button(text="/", command=lambda: set_operation('/')).grid(row=4, column=3)

# Кнопка равно и очистки
ttk.Button(text="=", command=calc).grid(row=4, column=2)
ttk.Button(text="C", command=clear_entry).grid(row=4, column=1)

first = None
oper = None

window.mainloop()
