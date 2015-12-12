#Main file
#created by Noah and Pia
import cars
import board

youWin = False

#START OF GAME

#Display of gameboard 
gameBoard = board.decideDiff() 

board.printBoard(gameBoard) 


while youWin == False:
    piece = input("Please enter the car you would like to move (ex: 11): ")
    endpos = input("Please enter the end position (of the top most piece or left most piece) piece of the car (ex: Aa): ")

    #Placing appropriate variables into pre-defined functions
    endpos = cars.readUser(endpos)
    direction = cars.carDirection(piece, gameBoard)

    gameBoard = cars.correctMove(endpos, piece, gameBoard)
    board.printBoard(gameBoard)

#win condition
    if gameBoard[17] == '00':
        youWin = True
#Jackie Chan display when win
if youWin ==  True:
    board.printJackieChan()
