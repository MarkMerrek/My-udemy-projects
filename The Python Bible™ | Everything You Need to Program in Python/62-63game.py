# Create a list for our board
board = ["   " for i in range(9)]


# Create a function to print out a board
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


# Create a function for players moves
def player_move(icon):

    if icon == " X ":
        number = 1
    elif icon == " O ":
        number = 2

    print("Your turn player {}".format(number))

    # Let players choose which space on the board they want to take
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == "   ":
        board[choice - 1] = icon
    # If space is taken, show a message and return to the start of the function
    else:
        print()
        print("That space is taken!")
        player_move(icon)


# Check if someone has won
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
            (board[3] == icon and board[4] == icon and board[5] == icon) or \
            (board[6] == icon and board[7] == icon and board[8] == icon) or \
            (board[0] == icon and board[3] == icon and board[6] == icon) or \
            (board[1] == icon and board[4] == icon and board[7] == icon) or \
            (board[2] == icon and board[5] == icon and board[8] == icon) or \
            (board[0] == icon and board[4] == icon and board[8] == icon) or \
            (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


# Check if it's a draw
def is_draw():
    if "   " not in board:
        return True
    else:
        return False


# Create a gaming loop
while True:
    print_board()
    player_move(" X ")
    print_board()
    # Check if player X has won
    if is_victory(" X "):
        print("X Wins! Congratulations!")
        break
    # Check for a draw
    elif is_draw():
        print("It's a draw!")
        break
    player_move(" O ")
    # Check if player O has won and print a board one last time
    if is_victory(" O "):
        print_board()
        print("O Wins! Congratulations!")
        break
    # Check for a draw
    elif is_draw():
        print("It's a draw!")
        break
