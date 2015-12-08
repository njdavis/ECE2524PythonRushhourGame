#board.py
#Created by: Noah Davis
#
#This file is meant to print out the gameboard.
#

def printBoard(pos):
    print ("    A  B  C  D  E  F")
    print ("   -------------------")
    print (" a |%s|%s|%s|%s|%s|%s|" % (pos[0],pos[1],pos[2],pos[3],pos[4],pos[5]) )
    print ("   -------------------")
    print (" b |%s|%s|%s|%s|%s|%s|" % (pos[6],pos[7],pos[8],pos[9],pos[10],pos[11]) )
    print ("   ----------------------")
    print (" c |%s|%s|%s|%s|%s|%s  Exit" % (pos[12],pos[13],pos[14],pos[15],pos[16],pos[17]) )
    print ("   ----------------------")
    print (" d |%s|%s|%s|%s|%s|%s|" % (pos[18],pos[19],pos[20],pos[21],pos[22],pos[23]) )
    print ("   -------------------")
    print (" e |%s|%s|%s|%s|%s|%s|" % (pos[24],pos[25],pos[26],pos[27],pos[28],pos[29]) )
    print ("   -------------------")
    print (" f |%s|%s|%s|%s|%s|%s|" % (pos[30],pos[32],pos[32],pos[33],pos[34],pos[35]) )
    print ("   -------------------")


#This function decides the difficulty of the game
def decideDiff():
    #Initialize the gameboard with blank spaces
    pos  = ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',' ','  ','  ','  ','  ','  ','  ','  ']

    print ("Do you wish to play easy, medium, or hard?")
    print ("Type 'easy', 'medium', or 'hard' and press enter")
    difficulty = input()
    
    print ( difficulty)
    
    if difficulty  == 'hard':
        #car 0
        pos[15] = '00'
        pos[16] = '00'
        
        #car 1
        pos[5] = '11'
        pos[11] = '11'
        pos[17] = '11'
        
        #car 2
        pos[28] = '22'
        pos[29] = '22'
        
        #car 3 
        pos[27] = '33'
        pos[33] = '33'
    elif difficulty == 'medium':
        #car 0
        pos[15] = '00'
        pos[16] = '00'
        
        #car 1
        pos[5] = '11'
        pos[11] = '11'
        pos[17] = '11'
        
        #car 2
        pos[28] = '22'
        pos[29] = '22'
        
        #car 3 
        pos[27] = '33'
        pos[33] = '33'
    else:
        #car 0
        pos[15] = '00'
        pos[16] = '00'
        
        #car 1
        pos[5] = '11'
        pos[11] = '11'
        pos[17] = '11'
        
        #car 2
        pos[28] = '22'
        pos[29] = '22'
        
        #car 3 
        pos[27] = '33'
        pos[33] = '33'

    return pos


def printJackieChan():
    print (''' 
    You Win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    `````````````````¶¶¶¶¶¶¶1```````¶¶¶¶¶````````
    `````1¶``1¶````¶¶¶¶¶¶¶¶¶¶¶¶1``1¶¶¶1`¶¶¶``````
    ````1¶¶¶¶¶11`1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶111`¶¶1`````
    ```111¶1`1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1```1¶1`¶`````
    ```¶1¶``¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111``¶11¶````
    ``¶¶``1¶1`1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶`11``¶`¶````
    `¶¶``¶1``¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶`1```11¶```
    1¶¶`¶```¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1```1¶``1¶¶```
    ¶¶`¶```¶¶¶¶1¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1``````¶¶``
    ¶`¶```¶¶¶``1¶¶¶``¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶``````¶¶`
    `````¶1``1¶¶¶111````¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶1``````¶1
    ````1```¶¶¶¶¶``1¶¶¶1`1¶1¶¶¶11¶`¶¶¶¶¶1¶``````¶
    ``````¶¶¶¶¶¶``11¶¶¶¶¶1`1`¶¶¶¶¶1`¶¶¶¶`¶1`````1
    `````1¶¶¶¶¶``1¶``1¶1111¶¶11¶¶11`¶¶¶¶`¶¶``````
    ````1¶¶¶¶¶¶``¶`¶¶¶¶¶111`¶1¶¶¶¶1`¶¶¶1``¶``````
    ````¶¶¶¶¶¶¶```````1111```1``````¶¶¶```11`````
    ```¶`¶¶¶¶¶````````1¶1````11`````¶¶¶````¶11```
    ```¶``¶¶¶¶1```````1``¶```¶¶`````¶¶```````¶¶``
    `1¶```¶¶`11````````¶¶11``¶¶¶````¶¶````````¶¶`
    ¶¶````1¶1¶`````````1¶¶¶1¶¶¶1````¶¶`````````¶1
    ```````¶1```````````1``````¶1``1¶1``````````¶
    ```````1¶¶¶````````¶`1¶1¶1``¶``¶¶```````````1
    ````````¶¶¶`````````1¶1¶¶¶¶````¶¶1```````````
    ````````1¶¶1`````````1111¶````¶1`¶¶````1`````
    ````````1¶1¶```````````11````¶¶```¶¶`¶¶¶¶¶111
    1``¶¶¶¶¶1¶`1¶¶````````¶¶¶¶``¶¶1````¶¶1```1¶¶¶
    ¶¶¶¶11``1¶```¶¶1```````````¶¶`1````¶`````````
    ``11````1¶`````¶¶¶¶¶¶1````¶1`1¶```¶¶`````1```
    `````````¶¶`````¶¶`11¶¶¶¶¶``1¶1¶¶1¶```````¶``
    ``````````¶¶````1¶``````11¶¶¶¶``¶¶¶¶``````¶``
    ```````````¶¶¶1``¶1¶¶¶¶1¶¶1`1¶`````¶``````¶¶`
    `````````````1¶¶¶¶``````````¶``````¶```````¶`
    `````````````````¶¶````````1¶`````1¶```````¶1
    ````````````````````````````1`````1`````````¶
    ''') 
