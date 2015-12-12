#!usr/bin/python

#checking position for moving piece 

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


def move (endpos, piece, pos, direction)
	
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
