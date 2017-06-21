# Prints out the gameboard.
def printgameboard(gameboard):
    clear = lambda: os.system('clear')
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

# Prints out the game's startpage.



def startpage():

    print("     |     |     ")
    print(" \x1b[31;1m {0} \x1b[0m | \x1b[32;1m {1} \x1b[0m | \x1b[33;1m {2} \x1b[0m ".format("T", "I", "C"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[34;1m {0} \x1b[0m | \x1b[35;1m {1} \x1b[0m | \x1b[36;1m {2} \x1b[0m ".format("T", "A", "C"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[93;1m {0} \x1b[0m | \x1b[91;1m {1} \x1b[0m | \x1b[37;1m {2} \x1b[0m ".format("T", "O", "E"))
    print("     |     |     ")

   
    while True:
        mode = input("Press 1 (two player) or 0 (computer) to start! ")
        if mode == "1":
            return False
        if mode == "0":
            return True

# This function checks position is empty or not and also check is it a number between 1 and 9.


def readchoice():
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

# This function checks empty position in computer mode.


def readAI():
    while True:
        number = random.randint(1, 9)
        if (gameboard[number] != ' '):
            continue
        return number

# Prints out "GAME OVER" if the game is ended.


def stoppage():
    print("     |     |     ")
    print(" \x1b[31;1m {0} \x1b[0m | \x1b[32;1m {1} \x1b[0m | \x1b[33;1m {2} \x1b[0m ".format("G", "A", "M"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[34;1m {0} \x1b[0m | \x1b[35;1m {1} \x1b[0m | \x1b[36;1m {2} \x1b[0m ".format("M", "E", "O"))
    print("_____|_____|_____")
    print("     |     |     ")
    print(" \x1b[93;1m {0} \x1b[0m | \x1b[91;1m {1} \x1b[0m | \x1b[37;1m {2} \x1b[0m ".format("V", "E", "R"))
    print("     |     |     ")

# This function checks the winning and draw state, its return value stops or leaves running the game.


def win(gameboard):
    mark = mark_x
    if gameboard[1] == mark and gameboard[2] == mark and gameboard[3] == mark:
        printgameboard(gameboard)
        print("Player 1 won!")
        stoppage()
        return True
    if gameboard[4] == mark and gameboard[5] == mark and gameboard[6] == mark:
        printgameboard(gameboard)
        print("Player 1 won!")
        stoppage()
        return True
    if gameboard[7] == mark and gameboard[8] == mark and gameboard[9] == mark:
        printgameboard(gameboard)
        print("Player 1 won!")
        stoppage()
        return True
    if gameboard[1] == mark and gameboard[4] == mark and gameboard[7] == mark:
        printgameboard(gameboard)
        print("Player 1 won!")
        stoppage()
        return True
    if gameboard[2] == mark and gameboard[5] == mark and gameboard[8] == mark:
        printgameboard(gameboard)
        print("Player 1 won!")
        stoppage()
        return True
    if gameboard[3] == mark and gameboard[6] == mark and gameboard[9] == mark:
        printgameboard(gameboard)
        print("Player 1 won!")
        stoppage()
        return True
    if gameboard[1] == mark and gameboard[5] == mark and gameboard[9] == mark:
        printgameboard(gameboard)
        print("Player 1 won!")
        stoppage()
        return True
    if gameboard[3] == mark and gameboard[5] == mark and gameboard[7] == mark:
        printgameboard(gameboard)
        print("Player 1 won!")
        stoppage()
        return True
    if gameboard[1] != ' ' and gameboard[2] != ' ' and gameboard[3] != ' ' and gameboard[4] != ' ' and gameboard[
            5] != ' ' and gameboard[6] != ' ' and gameboard[7] != ' ' and gameboard[8] != ' ' and gameboard[9] != ' ':
        print("Game Draw!")
        stoppage()
        return True

    mark = mark_o
    if gameboard[1] == mark and gameboard[2] == mark and gameboard[3] == mark:
        printgameboard(gameboard)
        print("Player 2 won!")
        stoppage()
        return True
    if gameboard[4] == mark and gameboard[5] == mark and gameboard[6] == mark:
        printgameboard(gameboard)
        print("Player 2 won!")
        stoppage()
        return True
    if gameboard[7] == mark and gameboard[8] == mark and gameboard[9] == mark:
        printgameboard(gameboard)
        print("Player 2 won!")
        stoppage()
        return True
    if gameboard[1] == mark and gameboard[4] == mark and gameboard[7] == mark:
        printgameboard(gameboard)
        print("Player 2 won!") 
        stoppage()
        return True
    if gameboard[2] == mark and gameboard[5] == mark and gameboard[8] == mark:
        printgameboard(gameboard)
        print("Player 2 won!")
        stoppage()
        return True
    if gameboard[3] == mark and gameboard[6] == mark and gameboard[9] == mark:
        printgameboard(gameboard)
        print("Player 2 won!")
        stoppage()
        return True
    if gameboard[1] == mark and gameboard[5] == mark and gameboard[9] == mark:
        printgameboard(gameboard)
        print("Player 2 won!")
        stoppage()
        return True
    if gameboard[3] == mark and gameboard[5] == mark and gameboard[7] == mark:
        printgameboard(gameboard)
        print("Player 2 won!")
        stoppage()
        return True
    if gameboard[1] != ' ' and gameboard[2] != ' ' and gameboard[3] != ' ' and gameboard[4] != ' ' and gameboard[
            5] != ' ' and gameboard[6] != ' ' and gameboard[7] != ' ' and gameboard[8] != ' ' and gameboard[9] != ' ':
        print("Game Draw!")
        stoppage()
        return True

    return False



mark_x = '\x1b[34;1mX\x1b[0m'
mark_o = '\x1b[31;1mO\x1b[0m' 

import random
import os

# Makes a list with 9 space characters.
gameboard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# The variable 'gameover' starts with value False.
gameover = False

# The startpage function returns back whether we chose computer or two player mode.
computermode = startpage()

# The game starts with the first player.
whoisnext = 1

# The game is running until the value of 'gameover' is 'False'.
while gameover == False:
    if whoisnext == 1:
        printgameboard(gameboard)
        print("Player 1")
        inp = readchoice()
        gameboard[inp] = mark_x
        gameover = win(gameboard)
        whoisnext = 2

    elif whoisnext == 2:
        if not computermode:
            printgameboard(gameboard)
            print("Player 2")
            inp = readchoice()
            gameboard[inp] = mark_o
            gameover = win(gameboard)
            whoisnext = 1
        else:
            printgameboard(gameboard)
            print("Player 2 - A.I.")
            inp = readAI()
            gameboard[inp] = mark_o
            gameover = win(gameboard)
            whoisnext = 1
