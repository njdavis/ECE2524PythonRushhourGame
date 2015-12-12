#Main file
#created by Noah and Pia
import cars
import board

youWin = False

gameBoard = board.decideDiff() 

board.printBoard(gameBoard) 

while youWin == False:
    piece = input("Please enter the car you would like to move (ex: 11): ")
    endpos = input("Please enter the end position (of the top most piece or right most piece) piece of the car (ex: Aa): ")

    endpos = cars.readUser(endpos)
    direction = cars.carDirection(piece, gameBoard)

    gameBoard = cars.correctMove(endpos, piece, gameBoard)
    board.printBoard(gameBoard)

    if gameBoard[17] == '00':
        youWin = True

if youWin ==  True:
    board.printJackieChan()
