import random

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# Display current board state
def print_board(board):
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("------------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("------------")
    print(board[2][0], "|", board[2][1], "|", board[2][2])

# Place the current player's mark only if the selected position is empty
def make_move(board, user_choice, current_player):
    if user_choice == "1":
        if board[0][0] == " ":
            board[0][0] = current_player
            return True
        else:
            print("This position is already taken")
            return False

    elif user_choice == "2":
        if board[0][1] == " ":
            board[0][1] = current_player
            return True
        else:
            print("This position is already taken")
            return False

    elif user_choice == "3":
        if board[0][2] == " ":
            board[0][2] = current_player
            return True
        else:
            print("This position is already taken")
            return False

    elif user_choice == "4":
        if board[1][0] == " ":
            board[1][0] = current_player
            return True
        else:
            print("This position is already taken")
            return False

    elif user_choice == "5":
        if board[1][1] == " ":
            board[1][1] = current_player
            return True
        else:
            print("This position is already taken")
            return False

    elif user_choice == "6":
        if board[1][2] == " ":
            board[1][2] = current_player
            return True
        else:
            print("This position is already taken")
            return False

    elif user_choice == "7":
        if board[2][0] == " ":
            board[2][0] = current_player
            return True
        else:
            print("This position is already taken")
            return False

    elif user_choice == "8":
        if board[2][1] == " ":
            board[2][1] = current_player
            return True
        else:
            print("This position is already taken")
            return False

    elif user_choice == "9":
        if board[2][2] == " ":
            board[2][2] = current_player
            return True
        else:
            print("This position is already taken")
            return False

    else:
        print("Invalid choice")
        return False

# Check if the current move ended the game by win or draw
def check_game_over(board, current_player):
    # Check all possible winning combinations
    row1 = (board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ")
    row2 = (board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ")
    row3 = (board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ")

    col1 = (board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ")
    col2 = (board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ")
    col3 = (board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ")

    diag1 = (board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ")
    diag2 = (board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ")

    if row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2:
        print_board(board)
        print(f"{current_player} wins!")
        return True

    # If the board is full and no one won, the game is a draw
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print_board(board)
        print("It's a draw!")
        return True

    return False

# Switch turns between the human player and the computer
def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"

# Collect all empty positions so the computer only chooses valid moves
def get_available_moves(board):
    available_moves = []

    if board[0][0] == " ":
        available_moves.append(1)
    if board[0][1] == " ":
        available_moves.append(2)
    if board[0][2] == " ":
        available_moves.append(3)
    if board[1][0] == " ":
        available_moves.append(4)
    if board[1][1] == " ":
        available_moves.append(5)
    if board[1][2] == " ":
        available_moves.append(6)
    if board[2][0] == " ":
        available_moves.append(7)
    if board[2][1] == " ":
        available_moves.append(8)
    if board[2][2] == " ":
        available_moves.append(9)

    return available_moves

# Easy mode: computer chooses a random available move
def computer_move(board, current_player):
    moves = get_available_moves(board)
    choice = random.choice(moves)
    make_move(board, str(choice), current_player)

# Try each available move on a temporary board to see if it wins immediately
def find_winning_move(board, player):
    moves = get_available_moves(board)

    for move in moves:
        temp_board = [
            board[0][:],
            board[1][:],
            board[2][:],
        ]

        make_move(temp_board, str(move), player)

        if check_game_over(temp_board, player):
            return move

    return None

# Medium mode: win if possible, block the user if needed, otherwise move randomly
def medium_move(board, current_player):
    win_move = find_winning_move(board, current_player)
    if win_move:
        make_move(board, str(win_move), current_player)
        return

    block_move = find_winning_move(board, "X")
    if block_move:
        make_move(board, str(block_move), current_player)
        return

    computer_move(board, current_player)


# X starts first
current_player = "X"

difficulty = input("Choose difficulty: easy / medium: ")

while True:
    print_board(board)
    print(f"it's {current_player}'s turn")

    if current_player == "X":
        user_choice = input("Enter where u want to play(position with num)? ")
        move_made = make_move(board, user_choice, current_player)
    else:
        print("Computer is thinking...")

        if difficulty == "easy":
            computer_move(board, current_player)
            move_made = True
        elif difficulty == "medium":
            medium_move(board, current_player)
            move_made = True
        else:
            print("Your choice is not available")
            break

    # Only check the game result and switch turns after a valid move
    if move_made:
        checker = check_game_over(board, current_player)
        if checker:
            break

        current_player = switch_player(current_player)
