# Prints out the gameboard.
def print_gameboard(gameboard):

    def clear(): return os.system('clear')
    clear()

    print("     |     |     ")
    print("  {0}  |  {1}  |  {2}  ".format(gameboard[1], gameboard[2], gameboard[3]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {0}  |  {1}  |  {2}  ".format(gameboard[4], gameboard[5], gameboard[6]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {0}  |  {1}  |  {2}  ".format(gameboard[7], gameboard[8], gameboard[9]))
    print("     |     |     ")

# Prints out the game's start_page.


def start_page(names):

    print("Welcome to Tic-tac-toe!")
    print("     |     |     ")
    print(" \x1b[31;1m {0} \x1b[0m | \x1b[32;1m {1} \x1b[0m | \x1b[33;1m {2} \x1b[0m ".format("T", "I", "C"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[34;1m {0} \x1b[0m | \x1b[35;1m {1} \x1b[0m | \x1b[36;1m {2} \x1b[0m ".format("T", "A", "C"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[93;1m {0} \x1b[0m | \x1b[91;1m {1} \x1b[0m | \x1b[37;1m {2} \x1b[0m ".format("T", "O", "E"))
    print("     |     |     ")

    print("\n This how you can chose the place which you want to mark.")
    print("     |     |     ")
    print(" \x1b[31;1m {0} \x1b[0m | \x1b[32;1m {1} \x1b[0m | \x1b[33;1m {2} \x1b[0m ".format("1", "2", "3"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[34;1m {0} \x1b[0m | \x1b[35;1m {1} \x1b[0m | \x1b[36;1m {2} \x1b[0m ".format("4", "5", "6"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[93;1m {0} \x1b[0m | \x1b[91;1m {1} \x1b[0m | \x1b[37;1m {2} \x1b[0m ".format("7", "8", "9"))
    print("     |     |     ")

    while True:
        mode = input("Press 1 (two player) or 0 (computer) to start! ")
        if mode == "1":
            names.append(input("Enter your name: "))
            names.append(input("Enter your name: "))
            return False
        if mode == "0":
            names.append(input("Enter your name: "))
            names.append("A.I.")
            return True


# This function checks position is empty or not and also check is it a number between 1 and 9.
def read_choice():

    while True:
        input_str = input("Enter a number between [1-9] where you want to mark: ")
        try:
            number = int(input_str)
        except ValueError:
            print("I said number mate!")
            continue
        if (number < 1 or number > 9):
            print("Wrong number mate!")
            continue
        if (gameboard[number] != ' '):
            print("Sorry its already taken... Take another pick!")
            continue
        return number

# This function control the AI.


def read_ai():

    for i in range(1, 10):
        copy_gameboard = list(gameboard)
        if copy_gameboard[i] == ' ':
            copy_gameboard[i] = mark_o
            if win(copy_gameboard):
                return i

    for i in range(1, 10):
        copy_gameboard = list(gameboard)
        if copy_gameboard[i] == ' ':
            copy_gameboard[i] = mark_x
            if win(copy_gameboard):
                return i

    corner_positions = [1, 3, 7, 9]
    while len(corner_positions) > 0:
        corner_index = random.randint(0, len(corner_positions) - 1)
        position = corner_positions[corner_index]
        if gameboard[position] == ' ':
            return position

        else:
            list.remove(position)

    if gameboard[5] == ' ':
        return 5

    other_positions = [2, 4, 6, 8]
    while len(other_positions) > 0:
        other_index = random.randint(0, len(other_positions) - 1)
        position = other_positions[other_index]
        if gameboard[position] == ' ':
            return position

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


# Prints out "GAME OVER" if the game is ended.
def stop_page():

    print("     |     |     ")
    print(" \x1b[31;1m {0} \x1b[0m | \x1b[32;1m {1} \x1b[0m | \x1b[33;1m {2} \x1b[0m ".format("G", "A", "M"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[34;1m {0} \x1b[0m | \x1b[35;1m {1} \x1b[0m | \x1b[36;1m {2} \x1b[0m ".format("E", " ", "O"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[93;1m {0} \x1b[0m | \x1b[91;1m {1} \x1b[0m | \x1b[37;1m {2} \x1b[0m ".format("V", "E", "R"))
    print("     |     |     ")

# This function checks the winning and draw state, its return value stops or leaves running the game.


def win(gameboard):

    win = False
    marks = [mark_x, mark_o]

    for mark in marks:
        if gameboard[1] == mark and gameboard[2] == mark and gameboard[3] == mark:
            win = True
        elif gameboard[4] == mark and gameboard[5] == mark and gameboard[6] == mark:
            win = True
        elif gameboard[7] == mark and gameboard[8] == mark and gameboard[9] == mark:
            win = True
        elif gameboard[1] == mark and gameboard[4] == mark and gameboard[7] == mark:
            win = True
        elif gameboard[2] == mark and gameboard[5] == mark and gameboard[8] == mark:
            win = True
        elif gameboard[3] == mark and gameboard[6] == mark and gameboard[9] == mark:
            win = True
        elif gameboard[1] == mark and gameboard[5] == mark and gameboard[9] == mark:
            win = True
        elif gameboard[3] == mark and gameboard[5] == mark and gameboard[7] == mark:
            win = True
        elif (gameboard[1] != ' ' and gameboard[2] != ' ' and gameboard[3] != ' '
              and gameboard[4] != ' ' and gameboard[5] != ' ' and gameboard[6] != ' '
              and gameboard[7] != ' ' and gameboard[8] != ' ' and gameboard[9] != ' '):
            print("Game draw!")
            stop_page()
            return True

        if win:
            print_gameboard(gameboard)
            if mark == mark_x:
                print("{0} won!".format(names[0]))
            elif mark == mark_o:
                print("{0} won!".format(names[1]))
            stop_page()
            return True

    return False


import random
import os

# Makes a list with 9 space characters.
gameboard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# The variable 'gameover' starts with value False.
gameover = False
names = []
mark_x = '\x1b[34;1mX\x1b[0m'
mark_o = '\x1b[31;1mO\x1b[0m'


# The start_page function returns back whether we chose computer or two player mode.
computer_mode = start_page(names)

# The game starts with the first player.
who_is_next = 1

# The game is running until the value of 'gameover' is 'False'.
while gameover == False:
    if who_is_next == 1:
        print_gameboard(gameboard)
        print("{0}".format(names[0]))
        inp = read_choice()
        gameboard[inp] = mark_x
        gameover = win(gameboard)
        who_is_next = 2
    elif who_is_next == 2:
        if not computer_mode:
            print_gameboard(gameboard)
            print("{0}".format(names[1]))
            inp = read_choice()
            gameboard[inp] = mark_o
            gameover = win(gameboard)
            who_is_next = 1
        else:
            print_gameboard(gameboard)
            print("{0}".format(names[1]))
            inp = read_ai()
            gameboard[inp] = mark_o
            gameover = win(gameboard)
            who_is_next = 1
