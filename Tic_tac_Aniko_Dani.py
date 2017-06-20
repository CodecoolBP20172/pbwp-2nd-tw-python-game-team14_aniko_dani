# Prints out the gameboard.
def printgameboard(gameboard):
    print("     |     |     ")
    print("  %c  |  %c  |  %c  " % (gameboard[1], gameboard[2], gameboard[3]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  %c  |  %c  |  %c  " % (gameboard[4], gameboard[5], gameboard[6]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  %c  |  %c  |  %c  " % (gameboard[7], gameboard[8], gameboard[9]))
    print("     |     |     ")

# Prints out the game's startpage.


def startpage():
    startboard = [" ", "T", "I", "C", "T", "A", "C", "T", "O", "E"]
    printgameboard(startboard)
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
    endboard = [" ", "G", "A", "M", "E", " ", "O", "V", "E", "R"]
    printgameboard(endboard)

# This function checks the winning and draw state, its return value stops or leaves running the game.


def win(gameboard):
    mark = "X"
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

    mark = "O"
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


import random

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
        print("Player 1")
        printgameboard(gameboard)
        inp = readchoice()
        gameboard[inp] = "X"
        gameover = win(gameboard)
        whoisnext = 2

    elif whoisnext == 2:
        if not computermode:
            print("Player 2")
            printgameboard(gameboard)
            inp = readchoice()
            gameboard[inp] = "O"
            gameover = win(gameboard)
            whoisnext = 1
        else:
            print("Player 2 - A.I.")
            printgameboard(gameboard)
            inp = readAI()
            gameboard[inp] = "O"
            gameover = win(gameboard)
            whoisnext = 1
