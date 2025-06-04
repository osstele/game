import tkinter as tk
from PIL import Image, ImageTk
import random

# Choices
choices = ['Rock', 'Paper', 'Scissors']

# Score counters
user_score = 0
computer_score = 0
tie_score = 0

# Game logic
def play(user_choice):
    global user_score, computer_score, tie_score

    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a Tie!"
        tie_score += 1
    elif (
        (user_choice == 'Rock' and comp_choice == 'Scissors') or
        (user_choice == 'Paper' and comp_choice == 'Rock') or
        (user_choice == 'Scissors' and comp_choice == 'Paper')
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=f"You chose {user_choice}, Computer chose {comp_choice}\n{result}")
    score_label.config(text=f"Score => You: {user_score} | Computer: {computer_score} | Ties: {tie_score}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("420x400")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20))
title_label.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Score
score_label = tk.Label(root, text="Score => You: 0 | Computer: 0 | Ties: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Load Images
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((64, 64)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((64, 64)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((64, 64)))

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Buttons with images
rock_button = tk.Button(button_frame, image=rock_img, command=lambda: play('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, image=paper_img, command=lambda: play('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, image=scissors_img, command=lambda: play('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Main loop
root.mainloop()