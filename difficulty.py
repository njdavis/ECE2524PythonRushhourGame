#This file decides the difficulty of the game
#Created by Noah Davis

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

