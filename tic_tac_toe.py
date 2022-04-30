# Tic-Tac-Toe Game
# Caleb Barnhart

# Make the blank starting board
def make_board():
    blank_board = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return blank_board

# Display the board to the user
def display_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8], "\n")

# Determine who's turn it is
def is_x_turn(turn):
    if turn % 2 == 0:
        return True
    elif turn % 2 == 1:
        return False

# Play the game
def play_game(board, player):
    if player == True:
        location = input("X's turn to play, please choose between 1 - 9: ")
        board[int(location) - 1] = "X"
    elif player == False:
        location = input("O's turn to play, please choose between 1 - 9: ")
        board[int(location) - 1] = "O"

# Check to see if the game has a winner
def game_done(board):
    if (board[0] == board[1] == board[2] or board[3] == board[4] == board[5] 
    or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] 
    or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] 
    or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
        print("Good Game!")
        return True

# Main function to play game
def main():
    board = make_board()
    display_board(board)

    turn = 2
    x = 1

    while x < 10:
        player = is_x_turn(turn)
        play_game(board, player)
        display_board(board)

        if game_done(board) == True:
            return
        turn += 1
        x += 1

main()