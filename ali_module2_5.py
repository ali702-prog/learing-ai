# X / O Game - Two Players

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


# Function to display the board
def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Function to check the winner
def check_winner(player):
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True

    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True

    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False


# Start the game
player = "X"

for turn in range(9):

    show_board()

    print("Player", player)

    choice = int(input("Choose a number (1-9): "))

    # Check if the position is available
    if board[choice - 1] == "X" or board[choice - 1] == "O":
        print("This position is already taken!")
        continue

    board[choice - 1] = player

    # Check winner
    if check_winner(player):
        show_board()
        print("Player", player, "wins!")
        break

    # Change player
    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    show_board()
    print("Draw!")