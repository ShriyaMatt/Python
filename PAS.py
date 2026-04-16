import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_strength():
    password = entry_password.get()

    # Input validation
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    length = len(password)

    # Determine strength based on length
    if length < 6:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 10:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    # Update label with strength
    label_result.config(text=f"Password Strength: {strength}", fg=color)


# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

# Password label and entry
label_password = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*", font=("Arial", 12), width=25)
entry_password.pack()

# Check button
btn_check = tk.Button(root, text="Check Strength", font=("Arial", 12), command=check_strength)
btn_check.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

# Run the application
root.mainloop()