import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")

description_label = tk.Label(root, text="This app multiplies two numbers entered by the user.", fg="blue")
description_label.pack(pady=5)

label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Product: {product}")
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers.")

calc_button = tk.Button(root, text="Calculate Product", command=calculate_product, bg="#90EE90")
calc_button.pack(pady=5)

result_text = tk.Text(root, height=2, width=30)
result_text.pack(pady=5)

root.mainloop()