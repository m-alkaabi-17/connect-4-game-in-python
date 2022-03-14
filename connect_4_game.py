# number of columns and rows required
num_of_col = 7
num_of_row = 6

# the board that doing the operation
board = [ [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] 
        ]

# the board that apperes to the user
user_board = [[ "-" , "-" , "-" , "-" , "-" , "-" , "-" ] ,
              [ "-" , "-" , "-" , "-" , "-" , "-" , "-" ] ,
              [ "-" , "-" , "-" , "-" , "-" , "-" , "-" ] ,
              [ "-" , "-" , "-" , "-" , "-" , "-" , "-" ] ,
              [ "-" , "-" , "-" , "-" , "-" , "-" , "-" ] ,
              [ "-" , "-" , "-" , "-" , "-" , "-" , "-" ] 
            ]


# printing the board
def display_board () :
    for row in range ( 0 , num_of_row ) :
        for col in range ( 0 , num_of_col ) :
            print ( user_board [row] [col] , end = ' ' )
        print ( " " )


# choosing the column by player and put an "X or O" in the last empty cell of column
def finding_the_cell ( col , player ) :
    col = col-1
    for rows in range ( num_of_row - 1 , -1 , -1) :
        if board [rows] [col] == 0 :
            if(player == 'X'):
              board [rows] [col] = 1
              user_board [rows] [col] = 'X'
            else :
              board [rows] [col] = 2
              user_board [rows] [col] = 'O'
            break

# the probabilities of winning
def the_winning():
    if vertWin() or horizWin() or diagWin() :
        return True
    return False

# vertical winning probability
def vertWin ():
  for row in range (0,3):
    for col in range(0, num_of_col):
      if board[row][col] > 0:
        if board [row][col] == board [row+1] [col] == \
           board[row+2] [col] == board [row+3] [col]:
           print('Player', board [row] [col], 'won!')
           return True
  return False

# horizontal winning probability
def horizWin():
    for row in range(0, num_of_row) :
        for col in range(0, 4):
            if board [row][col] > 0:
                if board [row] [col] == board [row] [col+1] == \
                board [row][col+2] == board [row][col+3]:
                  print('Player', board [row][col], 'won!')
                  return True
    return False


# diagonal winning probabilities
def diagWin ():

# diagonal winning probability num1
# going up and to the right
    for row in range(3, num_of_row) :
        for col in range(0, 4):
            if board[row][col] > 0:  
                if board [row] [col] == board [row-1] [col+1] == \
                    board [row-2][col+2] == board [row-3][col+3]:
                    print('Player', board[row][col], 'won!')
                    return True

# diagonal winning probability num2
# going down and to the right
    for row in range(0, 3) :
        for col in range(0, 4):
            if board[row][col] > 0:
                if board [row] [col] == board [row+1] [col+1] == \
                    board [row+2][col+2] == board [row+3][col+3]:
                    print('Player', board [row][col], 'won!')
                    return True
    return False


# player1 == X
# player2 == O

player = 'X'

while not the_winning():
   col =int (input('Enter a column: '))
   finding_the_cell ( col , player )
   display_board()
   
   if player == 'X' :
      player =  'O'
   else:
      player = 'X'