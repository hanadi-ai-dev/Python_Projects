board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]

# Display current board state
def print_board(board):
    print(board[0][0], "|" ,board[0][1],"|",board[0][2])
    print("------------")
    print(board[1][0], "|" ,board[1][1],"|",board[1][2])
    print("------------")
    print(board[2][0], "|" ,board[2][1],"|",board[2][2])

def make_move(board,user_choice,current_player):
    # Place mark only if selected position is empty
    if user_choice == "1":
        if board[0][0] == " ":
            board[0][0] = current_player
            return True
        else:
            print("This position is already taken")
            return  False

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

def check_game_over(board,current_player):
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

    # If board is full and no winner -> draw
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print_board(board)
        print("It's a draw!")
        return True

    return False

def switch_player(current_player):
    # Switch turns
    if current_player == "X":
        return "O"
    else:
        return "X"

# X starts first
current_player = "X"

while True:

    print_board(board)
    print(f"it's {current_player}'s turn")

    user_choice = input("Enter where u want to play(position with num)? ")

    move_made = make_move(board,user_choice,current_player)


    # Continue only if a valid move was made
    if move_made:
        checker = check_game_over(board,current_player)
        if checker:
            break

        current_player = switch_player(current_player)
