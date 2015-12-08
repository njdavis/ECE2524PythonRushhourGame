

import board

#carPositionListsitionList
pos  = ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']

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

board.printBoard(pos) 
