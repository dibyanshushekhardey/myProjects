# print print the tic tac toe layout

def printTicTacToe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


# function to check if any player has won
def check_win(player_pos, cur_player):
    # all possible combinations 
    sol = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
    # check if any winning combination is satisfied
    for x in sol:
        if all(y in player_pos[cur_player] for y in x):
            return True  # if there is any winning combination
    return False # if there is no combination as such is possible

# function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X'])+len(player_pos['O']) == 9:
        return True
    return False


# design the scoreboard
def printScoreboard(score_board):
    print("------------------------")
    print("-------SCOREBOARD-------")
    print("------------------------")

    players=list(score_board.keys())
    print("  ", players[0], "   ", score_board[players[0]])
    print("  ", players[1], "   ", score_board[players[1]])

    print("------------------------\n")


# for a single game of tic tac toe
def singleGame(cur_player):
    # representing tic tac toe
    values=[' ' for x in range(9)]
    # stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
    # ' ' a vacant cell
    # 'X' cell occupied by player X
    # 'O' cell occuied by player O

    # game for single game of tic tac tow 
    while True:
        printTicTacToe(values)

    # trying the exception block for move input
        try:
            print("Player", cur_player, " turn, which box?: ", end="")
            move=int(input())
        except ValueError:
            print("Wrong Input!!! Try again")
            continue
    
    # sanity check for move inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try again")
            continue
    #check if the box is not occupied currently
        if values[move-1] != ' ':
            print("Place is already occupied!!! Try again!")
            continue

        # update the game information 
        # updating the grid status
        values[move-1]=cur_player
        #updating player positions
        player_pos[cur_player].append(move)

        # function call to check win
        if check_win(player_pos, cur_player):
            printTicTacToe(values)
            print("Player ", cur_player, " has won the game!!!")
            print("\n")
            return cur_player

        # function call for checking draw game
        if check_draw(player_pos):
            printTicTacToe(values)
            print("Game is drawn!! Well done both player!!")
            print("\n")
            return 'D'

        # we have to switch the player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player='X'


if __name__=='__main__':
    print("Player 1")
    player1 = input("Enter the name: ")
    print("\n")

    print("Player 2")
    player2=input("Enter the name: ")
    print("\n")

    # stores the player who chooses X and O
    cur_player=player1
    #stores the choice of players
    player_choice={'X':"", "O":""}
    # stores the options
    options=['X', 'O']
    # stores the scoreboard
    score_board={player1:0, player2:0}


    # game loop for a series of tic tac toe
    # the loop runs until the players
    while True:
        # player choice menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit :(")
    
        # each iteration one has to handle and
        # store current player's choice
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input !! Try again\n")
            continue

        # conditioons for player choice
        if choice == 1:
            player_choice['X']= cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
        
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
        
        elif choice == 3:
            print("Final Scores!")
            printScoreboard(score_board)
            break
        else:
            print("Wrong Choice !!!Try Again!!!\n")

        # store the winner in a single game of TicTacToe
        winner=singleGame(options[choice-1])

        # update the scorecard according to the winner
        if winner != 'D':
            player_wom = player_choice[winner]
            score_board[player_wom] = score_board[player_wom+1]
        printScoreboard(score_board)

        # switch the choosing player
        if cur_player == player1:
            cur_player=player2
        else:
            cur_player=player1
