game_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

disp_board = {'1': '1', '2': '2', '3': '3',
              '4': '4', '5': '5', '6': '6',
              '7': '7', '8': '8', '9': '9'}


fill_board = []


# for i in the_board:
#     fill_board.append(i)

# Print or display the Tic-Tac-Toe board
def print_board(board):
    print(board["1"], " |", board["2"], "|", board["3"])
    print("-- + -- + --")
    print(board["4"], " |", board["5"], "|", board["6"])
    print("-- + -- + --")
    print(board["7"], " |", board["8"], "|", board["9"])


print_board(disp_board)
print("\n")


# Start of the main game function
def main_game():
    turn = "x"
    cnt = 0
    # move executor
    for i in range(1, 10):
        print_board(game_board)
        print("It's ", turn, " turn. Which place do you want to move?")

        # Move input taker
        move = input("Please enter your move: ")

        # Checks if the place on the board for particular place is empty
        if game_board[move] == ' ':
            game_board[move] = turn
            cnt += 1
        else:
            print(move, " place is already filled. Please try another place!")
            continue

        # Win checker
        if cnt >= 5:

            # Possibilities of win
            if game_board["7"] == game_board["8"] == game_board["9"]:
                print_board(game_board)
                print("Game over\n", turn, " has won the game")
                break

            elif game_board["4"] == game_board["5"] == game_board["6"]:
                print_board(game_board)
                print("Game over\n", turn, " has won the game")
                break

            elif game_board["1"] == game_board["2"] == game_board["3"]:
                print_board(game_board)
                print("Game over\n", turn, " has won the game")
                break

            elif game_board["1"] == game_board["5"] == game_board["9"]:
                print_board(game_board)
                print("Game over\n", turn, " has won the game")
                break

            elif game_board["7"] == game_board["5"] == game_board["3"]:
                print_board(game_board)
                print("Game over\n", turn, " has won the game")
                break

            elif game_board["7"] == game_board["4"] == game_board["1"]:
                print_board(game_board)
                print("Game over\n", turn, " has won the game")
                break

            elif game_board["8"] == game_board["5"] == game_board["2"]:
                print_board(game_board)
                print("Game over\n", turn, " has won the game")
                break

            elif game_board["9"] == game_board["6"] == game_board["3"]:
                print_board(game_board)
                print("Game over\n", turn, " has won the game")
                break
        if cnt == 9:
            print("Game over \n It's a Tie")

        # Turn switcher
        if turn == "x":
            turn = "o"
        else:
            turn = "x"

    print("Thanks for playing Quantum-Tricks Python Tic-Tac-Toe")
    new_game = input("Would you like to play again? Enter y to continue.... : ").lower()

    if new_game == "y":
        main_game()


main_game()
