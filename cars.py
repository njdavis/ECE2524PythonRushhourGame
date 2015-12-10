#this documents containing functions relating to the movement of game pieces
#created by Noah Davis & Pia Banerjee

#this function translates user inputs into machine readable variables
def move(endpos, piece, pos, direction)

        distance = posDistance(piece, pos)
        endEndPos = endpos + distance
        #put old values into grid
        for i in range (0,35):
                if pos[i] == piece:
                        pos[i]= '  '

        #add new values into grid
        if direction == 'vertical':
                for i range (endpos, endEndPos, 6):
        elif direction == 'horizontal':
                for i range (endpos, endEndPos):
        else:
                print "Something is wrong"

        return pos

def readUser(ans):
    if ans == 'Aa':
        return 0
    elif ans == 'Ab':
        return 1
    elif ans == 'Ac':
        return 2
    elif ans == 'Ad':
        return 3
    elif ans == 'Ae':
        return 4
    elif ans == 'Af':
        return 5
    elif ans == 'Ba':
        return 6
    elif ans == 'Bb':
        return 7
    elif ans == 'Bc':
        return 8
    elif ans == 'Bd':
        return 9
    elif ans == 'Be':
        return 10
    elif ans == 'Bf':
        return 11
    elif ans == 'Ca':
        return 12
    elif ans == 'Cb':
        return 13
    elif ans == 'Cc':
        return 14
    elif ans == 'Cd':
        return 15
    elif ans == 'Ce':
        return 16
    elif ans == 'Cf':
        return 17
    elif ans == 'Da':
        return 18
    elif ans == 'Db':
        return 19
    elif ans == 'Dc':
        return 20
    elif ans == 'Dd':
        return 21
    elif ans == 'De':
        return 22
    elif ans == 'Df':
        return 23
    elif ans == 'Ea':
        return 24
    elif ans == 'Eb':
        return 25
    elif ans == 'Ec':
        return 26
    elif ans == 'Ed':
        return 27
    elif ans == 'Ee':
        return 28
    elif ans == 'Ef':
        return 29
    elif ans == 'Fa':
        return 30
    elif ans == 'Fb':
        return 31
    elif ans == 'Fc':
        return 32
    elif ans == 'Fd':
        return 33
    elif ans == 'Fe':
        return 34
    elif ans == 'Ff':
        return 35
    else: 
        print ("You enterd the wrong command")
        return -1

#this function finds the size of the cars
def posDistance(piece, pos):    
    isBegin = True
    
    #scans the list for car pieces of the same type
    for i in range(0, 35):
        if piece == pos[i]:
            #end is only tracked once
            if isBegin == True:
                isBegin = False
                begin = i
            end = i+1
    
    #finds the distance between the beginning of the car and end
    #finds how large the car is
    distance = end - begin
    
    return distance
    
#this function finds the direction of the cars
def carDirection(piece, pos):
    distance = posDistance(piece, pos)

    if distance < 6:
        return 'Horizontal'
    else :
        return 'Vertical'


#checking position for moving piece into 

def CorrectMove (endpos, piece, pos)
        move position = cars.readUser(endpos)

        for i in range (0,35):
                if piece == pos[i]:
                        startpos = i

        direction = board.direction (pos[startpos])

        if direction == 'horizontal':
                for i in range (startpos, endpos):
                        if (pos[i] != ' ') || (pos[i] != piece:
                                print "Can't move piece here!"
                        else:
                                output = move(endpos, piece, pos,direction)
        elif direction == 'vertical':
                for i in range (startpos, endpos,6):
                        if (pos[i] != ' ') || (pos[i] != piece:
                                print "Can't move piece here!"
                        else:
                                output= move(endpos, piece, pos, direction)
        return output


