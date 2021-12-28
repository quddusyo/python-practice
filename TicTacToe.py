#TIC-TAC-TOE GAME
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 22:41:10 2021
PROJECT: Tic-Tac-Toe, Functions Practice
@author: yousuf
"""


# ------- Global Variables ----------

# Game Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

# If Game Going
game_still_going = True

# Winner or Tie?
winner = None

# Player's Turn
current_player = "X"

# Display board
def display_board():
    print(board[0]+ " | " + board[1]+" | " + board[2]+ " | ")
    print(board[3]+ " | " + board[4]+" | " + board[5]+ " | ")
    print(board[6]+ " | " + board[7]+" | " + board[8]+ " | ")



def play_game():
    
    # Display initial board
    display_board()
    
    while game_still_going:
        # Handle a single turn
        handle_turn(current_player)
        
        # Check if the game has ended
        check_gameover()
        # Flip to other player
        flip_player()
        
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    else:
        print("Tie.")
    
# Function to handle a single turn of arbitrary player
def handle_turn(current_player):
    print(current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    # Check valid entry with while loop until valid entry given.
    # Invalid entry 1: overwritting 'O' or 'X'
    # Invalide entry 2: number not between 1-9
    valid = False
    while not valid: 
 
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        
        if board[position] == "-":
            valid = True
        else:
            print("Cannot do that! Go again. ")
    board[position] = current_player
    display_board()
    
    
# Function to check who won or tie
def check_gameover():
    check_winner()
    check_tie()


# Function to check win
def check_winner():
    #set up global variable
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


# Function to check row
def check_rows():
    #set up global variable
    global game_still_going
    #check if any of the rows have same value and not '-'
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    # if row has match, flag there is a win
    if row1 or row2 or row3:
        game_still_going = False
    # Return the winner (X or O)
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


# Function to check columns
def check_columns():
    #set up global variable
    global game_still_going
    #check if any of the columns have same value and not '-'
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    # if column has match, flag there is a win
    if col1 or col2 or col3:
        game_still_going = False
    # Return the winner (X or O)
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


# Function to check diagonals
def check_diagonals():
    #set up global variable
    global game_still_going
    #check if any of the diagonals have same value and not '-'
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    # if diagonal has match, flag there is a win
    if diagonal1 or diagonal2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return
    

# Function to check tie
def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # Set global variable
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return 



play_game()




#board
#display board
#play game
#check win
#handle turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player