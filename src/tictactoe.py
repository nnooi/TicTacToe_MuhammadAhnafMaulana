import tkinter as tk
import random
from random import choice
from tkinter import *

# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Create a tkinter window
root = tk.Tk()
root.geometry("330x550")
root.title("Tic Tac Toe")


# Create a function to check for a win or draw
def check_winner():
    for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Draw"
    return None

def evaluate_board():
    for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        a, b, c = combo
        if board[a] == board[b] == "O" and board[c] == " ":
            return c
        if board[b] == board[c] == "O" and board[a] == " ":
            return a
        if board[a] == board[c] == "O" and board[b] == " ":
            return b
    return None

# Create a function to make the AI's move (random move)
def ai_move():
    best_move = None
    best_score = -float("inf")
    
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = evaluate_board()
            board[i] = " "
            
            if score is not None:
                if score > best_score:
                    best_score = score
                    best_move = i
    
    if best_move is not None:
        board[best_move] = "O"
        buttons[best_move].config(text="O", state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                result_label.config(text="It's a Draw!", )
            else:
                result_label.config(text="AI wins!", )
            for button in buttons:
                button.config(state="disabled")
    else:
        # If there is no winning move, make a random move
        random_ai_move()

# Create a function for the AI's random move (fallback)
def random_ai_move():
    if " " in board:
        ai_choice = random.choice([i for i, val in enumerate(board) if val == " "])
        board[ai_choice] = "O"
        buttons[ai_choice].config(text="O", state="disabled", )
        winner = check_winner()
        if winner:
            if winner == "Draw":
                result_label.config(text="It's a Draw!", )
            else:
                result_label.config(text="AI wins!", )
            for button in buttons:
                button.config(state="disabled")

# Create buttons for the Tic-Tac-Toe grid
buttons = []
for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(root,  text=" ", width=15, height=6, command=lambda i=i: player_move(i))
    button.grid(row=row, column=col)
    buttons.append(button)

# Create a function for the player's move
def player_move(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                result_label.config(text="It's a Draw!")
            else:
                result_label.config(text="You win!")
            for button in buttons:
                button.config(state="disabled")
        else:
            ai_move()
            
def restart_game_bot():
    for i in range(9):
        board[i] = " "
        buttons[i].config(text=" ", state="active")
    result_label.config(text="")
    ai_move()

def restart_game_kita():
    for i in range(9):
        board[i] = " "
        buttons[i].config(text=" ", state="active")
    result_label.config(text="")

    
# Create a label for the game result
result_label = tk.Label(root, text=" ", font=("Helvetica", 16))
result_label.grid(row=3, columnspan=3)

restart_button = tk.Button(root, text="Restart(player jalan awal)", command=restart_game_kita)
restart_button.grid(row=4, columnspan=3)
restart_button = tk.Button(root, text="Restart(bot jalan awal)", command=restart_game_bot)
restart_button.grid(row=5, columnspan=4)

root.mainloop()
