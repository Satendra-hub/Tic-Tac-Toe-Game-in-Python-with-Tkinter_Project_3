import tkinter as tk
from tkinter import messagebox

def check_winner():
    """
    Check all winning combinations to see if a player has won.
    If a winner is found, highlight the winning buttons, show a message,
    and end the game.
    Also checks for a draw if all buttons are filled without a winner.
    """
    global winner
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for combo in winning_combinations:
        # Check if the three buttons in combo have the same non-empty text
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            winner = True  # Set winner flag to True
            # Highlight the winning buttons in green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            # Show a popup message announcing the winner
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()  # Close the application
            return

    # If no winner, check if all buttons are filled (draw)
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        root.quit()

def button_click(index):
    """
    Handle the event when a button is clicked.
    If the button is empty and no winner yet, mark it with current player's symbol,
    check for winner, and toggle player turn.
    """
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player  # Mark button with current player's symbol
        check_winner()  # Check if this move wins the game
        if not winner:
            toggle_player()  # Switch to the other player if no winner

def toggle_player():
    """
    Switch the current player from X to O or O to X,
    and update the label showing whose turn it is.
    """
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize current player and winner flag
current_player = "X"
winner = False

# Label to show which player's turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=3)

# Create 9 buttons for the Tic-Tac-Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: button_click(i))  # Pass index i to handler
    button.grid(row=(i//3)+1, column=i%3)  # Arrange buttons in 3x3 grid starting from row 1
    buttons.append(button)

# Start the Tkinter event loop
root.mainloop()
