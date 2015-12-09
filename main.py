#Main file
#created by Noah and Pia
import cars
import board

youWin = False

pos = board.decideDiff() 
length = cars.posDistance('22',pos)
direction = cars.carDirection('22', pos)

print (length)
print (direction)

board.printBoard(pos) 

if youWin ==  True:
    board.printJackieChan()
