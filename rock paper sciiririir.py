import tkinter as tk
from tkinter import messagebox
import random

# Possible choices
CHOICES = ["Rock", "Paper", "Scissors"]

# Game logic to determine winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Function to handle user choice
def play(choice):
    global user_score, comp_score

    comp_choice = random.choice(CHOICES)
    result = determine_winner(choice, comp_choice)

    # Update scores
    if result == "You Win!":
        user_score += 1
    elif result == "Computer Wins!":
        comp_score += 1

    # Update labels
    user_choice_label.config(text=f"Your Choice: {choice}")
    comp_choice_label.config(text=f"Computer's Choice: {comp_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")

# Function to reset the game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_choice_label.config(text="Your Choice: ")
    comp_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Initialize scores
user_score = 0
comp_score = 0

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x350")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Choice buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Labels for choices and results
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack()

comp_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12))
comp_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game, bg="red", fg="white")
reset_btn.pack(pady=10)

# Run the application
root.mainloop()