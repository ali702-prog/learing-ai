import random


# Create 4 x 4 board
def create_board():
    return [[0, 0, 0, 0] for i in range(4)]


# Display the board
def show_board(board):
    print("\n-------------------------")

    for row in board:
        for number in row:
            if number == 0:
                print("|    ", end="")
            else:
                print("|", str(number).center(4), end="")

        print("|")
        print("-------------------------")


# Add a random 2 or 4
def add_number(board):
    empty = []

    for row in range(4):
        for column in range(4):
            if board[row][column] == 0:
                empty.append((row, column))

    if empty:
        row, column = random.choice(empty)

        # Mostly 2, sometimes 4
        board[row][column] = random.choice([2, 2, 2, 2, 4])


# Move one row to the left
def move_row_left(row):

    # Remove zeros
    numbers = []

    for number in row:
        if number != 0:
            numbers.append(number)

    # Merge same numbers
    new_row = []
    i = 0

    while i < len(numbers):

        if i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
            new_row.append(numbers[i] * 2)
            i += 2
        else:
            new_row.append(numbers[i])
            i += 1

    # Add zeros
    while len(new_row) < 4:
        new_row.append(0)

    return new_row


# Move left
def move_left(board):

    new_board = []

    for row in board:
        new_board.append(move_row_left(row))

    return new_board


# Move right
def move_right(board):

    new_board = []

    for row in board:

        row.reverse()

        new_row = move_row_left(row)

        new_row.reverse()

        new_board.append(new_row)

    return new_board


# Transpose the board
def transpose(board):

    new_board = []

    for column in range(4):

        new_row = []

        for row in range(4):
            new_row.append(board[row][column])

        new_board.append(new_row)

    return new_board


# Move up
def move_up(board):

    board = transpose(board)

    board = move_left(board)

    board = transpose(board)

    return board


# Move down
def move_down(board):

    board = transpose(board)

    board = move_right(board)

    board = transpose(board)

    return board


# Check if player reached 2048
def check_win(board):

    for row in board:
        if 2048 in row:
            return True

    return False


# Check if there are possible moves
def game_over(board):

    # Check for empty spaces
    for row in board:
        if 0 in row:
            return False

    # Check horizontal numbers
    for row in range(4):
        for column in range(3):
            if board[row][column] == board[row][column + 1]:
                return False

    # Check vertical numbers
    for row in range(3):
        for column in range(4):
            if board[row][column] == board[row + 1][column]:
                return False

    return True


# Main game
def play_2048():

    board = create_board()

    # Start with two numbers
    add_number(board)
    add_number(board)

    while True:

        show_board(board)

        if check_win(board):
            print("YOU WIN! You reached 2048!")
            break

        if game_over(board):
            print("GAME OVER!")
            break

        print("W = Up")
        print("S = Down")
        print("A = Left")
        print("D = Right")

        choice = input("Enter your move: ").lower()

        old_board = [row[:] for row in board]

        if choice == "a":
            board = move_left(board)

        elif choice == "d":
            board = move_right(board)

        elif choice == "w":
            board = move_up(board)

        elif choice == "s":
            board = move_down(board)

        else:
            print("Please enter W, A, S or D.")
            continue

        # Only add a number if board changed
        if board != old_board:
            add_number(board)


# Start game
play_2048()