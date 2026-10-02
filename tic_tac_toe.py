row1 = ["-", "-", "-",]
row2 = ["-", "-", "-",]
row3 = ["-", "-", "-",]
Board = [row1, row2, row3]
def print_board():
    '''This function prints the board.'''
    for i in range(len(Board)):
        print(Board[i])
        print()
 
def get_validint(prompt="Enter positive int") :
    '''This function checks to make sure that the player's input is an integer.'''
    user_input = input(prompt)  
    while user_input.isdigit() == False:
        print("Invalid.")
        user_input = input(prompt)  
    return int(user_input)
 
verticalsum_y = 0

def player_go(symbol): #maybe combine both player functions into 1?
    '''This function allows the player to enter the coordinates of where they would like to place a peice. It checks to make sure it is in range and there is not something already there.'''
    X_row = get_validint(f"{symbol} row (1-3): ")
    X_column = get_validint(f"{symbol} column(1-3): ")
    X_row = X_row- 1
    X_column = X_column - 1
    if X_row > 3 or X_column > 3:
        print("You went over ")
        X_row = get_validint(f"{symbol} row: ")
        X_column = get_validint(f"{symbol} column: ")
    if Board[X_row] [X_column] == "X" or Board[X_row] [X_column] == "O":
        print("Something is already there")
        X_row = get_validint(f"{symbol} row: ")
        X_column = get_validint(f"{symbol} column: ")
    Board[X_row] [X_column] = symbol
 
def check_diagonal():
    '''This function checks if there is a right up, left down diagonal.'''
    if Board[2][0] == Board[1][1]==  Board[0][2] and Board[0][2] != "-":
        return Board[2][0]

    else:
        return "No winner"
   
def find_result(player = "X"):
    '''This function finds if there is a row, collumn, or left up, down right diagnol full of one symbol.'''
    for row in range(len(Board)):
        if Board[row] == [player, player, player]: #check for win left - right
            return player
        for column in range(3):
            if Board[0][column] == player and Board[1][column] == player and Board[2][column] == player: #checks win going up-down
                return player
        lup_dright = 0
        for i in range(3):
            if Board[i][i] == player:
                lup_dright =+ 1
                if lup_dright == 3:
                    return player
        dleft_uright = check_diagonal()
        if dleft_uright == "X":
            return "X"
        elif dleft_uright == "O":
            return "O"
 
    return f"player {player} didnt"
def replay():
    '''This function resets the bpard after a round.'''
    for row in range(len(Board)):
        for col in range(len(Board)):
            Board[row][col] = "-"
active_player = "X"
while True:
    print_board()
    player_go(active_player)
    result = find_result(active_player)
    print(f"{result} win")
    if result == "X" or result == "O":
        reset = input("rematch? (y/n)")
        if reset == "y":
            replay()
        else:
            break
    active_player = "O" if active_player == "X" else "X"