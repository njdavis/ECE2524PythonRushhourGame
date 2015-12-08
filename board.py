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
