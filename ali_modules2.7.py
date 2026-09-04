import random
import json
import os


SAVE_FILE = "2048_save.json"


# Create 4 x 4 board
def create_board():
    return [[0, 0, 0, 0] for i in range(4)]


# Display the board
def show_board(board, score):
    print("\nScore:", score)
    print("-------------------------")

    for row in board:
        for number in row:
            if number == 0:
                print("|    ", end="")
            else:
                print("|", str(number).center(4), end="")

        print("|")
        print("-------------------------")


# Add random 2 or 4
def add_number(board):
    empty = []

    for row in range(4):
        for column in range(4):
            if board[row][column] == 0:
                empty.append((row, column))

    if empty:
        row, column = random.choice(empty)
        board[row][column] = random.choice([2, 2, 2, 2, 4])


# Save current game
def save_game(board, score):

    game_data = {
        "board": board,
        "score": score
    }

    with open(SAVE_FILE, "w") as file:
        json.dump(game_data, file, indent=4)

    print("Game saved successfully!")


# Load previous game
def load_game():

    if os.path.exists(SAVE_FILE):

        with open(SAVE_FILE, "r") as file:
            game_data = json.load(file)

        print("Saved game loaded!")

        return game_data["board"], game_data["score"]

    return None, None


# Move one row left
def move_row_left(row):

    numbers = []

    for number in row:
        if number != 0:
            numbers.append(number)

    new_row = []
    score_added = 0
    i = 0

    while i < len(numbers):

        if i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:

            merged_number = numbers[i] * 2

            new_row.append(merged_number)

            score_added += merged_number

            i += 2

        else:
            new_row.append(numbers[i])
            i += 1

    while len(new_row) < 4:
        new_row.append(0)

    return new_row, score_added


# Move left
def move_left(board):

    new_board = []
    total_score = 0

    for row in board:

        new_row, score = move_row_left(row)

        new_board.append(new_row)

        total_score += score

    return new_board, total_score


# Move right
def move_right(board):

    new_board = []
    total_score = 0

    for row in board:

        reversed_row = row[::-1]

        new_row, score = move_row_left(reversed_row)

        new_row.reverse()

        new_board.append(new_row)

        total_score += score

    return new_board, total_score


# Transpose board
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

    board, score = move_left(board)

    board = transpose(board)

    return board, score


# Move down
def move_down(board):

    board = transpose(board)

    board, score = move_right(board)

    board = transpose(board)

    return board, score


# Check winner
def check_win(board):

    for row in board:
        if 2048 in row:
            return True

    return False


# Check game over
def game_over(board):

    # Check empty spaces
    for row in board:
        if 0 in row:
            return False

    # Check horizontal moves
    for row in range(4):
        for column in range(3):

            if board[row][column] == board[row][column + 1]:
                return False

    # Check vertical moves
    for row in range(3):
        for column in range(4):

            if board[row][column] == board[row + 1][column]:
                return False

    return True


# Main game
def play_2048():

    print("===================")
    print("      2048 GAME")
    print("===================")

    # Check if saved game exists
    if os.path.exists(SAVE_FILE):

        answer = input("Continue saved game? (Y/N): ").lower()

        if answer == "y":
            board, score = load_game()

        else:
            board = create_board()
            score = 0

            add_number(board)
            add_number(board)

    else:
        board = create_board()
        score = 0

        add_number(board)
        add_number(board)

    while True:

        show_board(board, score)

        if check_win(board):
            print("YOU WIN! You reached 2048!")
            break

        if game_over(board):
            print("GAME OVER!")
            break

        print("\nW = Up")
        print("S = Down")
        print("A = Left")
        print("D = Right")
        print("Q = Save and Quit")

        choice = input("\nEnter your move: ").lower()

        # Save and exit
        if choice == "q":

            save_game(board, score)

            print("See you later!")
            break

        old_board = [row[:] for row in board]

        score_added = 0

        if choice == "a":
            board, score_added = move_left(board)

        elif choice == "d":
            board, score_added = move_right(board)

        elif choice == "w":
            board, score_added = move_up(board)

        elif choice == "s":
            board, score_added = move_down(board)

        else:
            print("Please enter W, A, S, D or Q.")
            continue

        # Only add new number after valid move
        if board != old_board:

            score += score_added

            add_number(board)


# Start game
play_2048()