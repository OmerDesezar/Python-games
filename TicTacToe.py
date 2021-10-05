# -----------------------------------------------------------------------------------------------------------------------
# tictactoe

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
game_still_going = True
current_player = "X"
winner = "none"


def play_tictactoe():
    while game_still_going:
        display_board()
        handle_turn()
        check_game_over()
        flip_player()
    results()
    suggest_rematch()


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn():
    position = int(input("choose a position from 1 to 9: ")) - 1
    while position < 0 or position > 8 or board[position] != "-":
        position = int(input("invalid position, choose another: ")) - 1
    board[position] = current_player


def check_game_over():
    check_row()
    check_column()
    check_diagonal()
    check_tie()


def check_row():
    if board[0] == board[1] == board[2] != "-" or board[3] == board[4] == board[5] != "-" or board[6] == board[7] == \
            board[8] != "-":
        end_game()


def check_column():
    if board[0] == board[3] == board[6] != "-" or board[1] == board[4] == board[7] != "-" or board[2] == board[5] == \
            board[8] != "-":
        end_game()


def check_diagonal():
    if board[0] == board[4] == board[8] != "-" or board[2] == board[4] == board[6] != "-":
        end_game()


def check_tie():
    for place in board:
        if place == "-":
            return
    global game_still_going
    game_still_going = False


def end_game():
    global winner
    global game_still_going
    winner = current_player
    game_still_going = False


def flip_player():
    global current_player
    if game_still_going:
        if current_player == "X":
            current_player = "O"
        elif current_player == "O":
            current_player = "X"


def results():
    display_board()
    if winner == "none":
        print("game ended in a tie")
    else:
        print("game winner is " + current_player)


def reset_parameters():
    global board
    global game_still_going
    global current_player
    global winner
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    game_still_going = True
    current_player = "X"
    winner = "none"


def suggest_rematch():
    rematch = input("rematch? 1 for yes: ")
    if rematch == "1":
        reset_parameters()
        play_tictactoe()


play_tictactoe()
# -----------------------------------------------------------------------------------------------------------------------





