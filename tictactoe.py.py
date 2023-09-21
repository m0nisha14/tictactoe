
from re import X

game_still_going=True
winner=None
current_player="X"


board=["-","-","-","-","-","-","-","-","-"]
def board_disp():
  
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3]+ "|" + board[4] + "|"+ board[5])
  print(board[6] + "|" + board[7] + "|"+ board[8])


def play_game():
  board_disp()
  while game_still_going:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  
  if(winner=="X" or winner=="O"):
    print(winner +" won")
  elif winner==None:
    print("Tie")
    

def handle_turn(player):
  print(player + "turn")
  position=input("Choose a position from 1 to 9:")
  valid=False
  while not valid:
    while position not in["1","2","3","4","5","6","7","8","9"]:
      position=input("Invalid input choose  a position from 1 to 9:")
    position=int(position)-1  
    if board[position] =="-":
      valid=True
    else:
      print("Try again")
      
  board[position] =player
  board_disp()
  
def check_if_game_over():
  check_if_win()
  check_if_tie()

def check_if_win():
  global game_still_going 
  if "-" not in board:
    game_still_going=False
    
  global winner
  row_winner=check_rows()
  col_winner=check_cols()
  diagonal_winner=check_diagonals()
  if row_winner:
    winner=row_winner
  elif col_winner:
    winner=col_winner
  elif diagonal_winner:
    winner=diagonal_winner
  else:
    winner=None
  return
  
def check_rows():
  global game_still_going
  row1= board[0]==board[1]==board[2] != "-"
  row2= board[3]==board[4]==board[5] != "-"
  row3= board[6]==board[7]==board[8] != "-"
  if row1 or row2 or row3:
    game_still_going=False
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6] 
  else:
    return None
  
def check_cols():
  global game_still_going
  col1= board[0]==board[3]==board[6] != "-"
  col2= board[1]==board[4]==board[7] != "-"
  col3= board[2]==board[5]==board[8] != "-"
  if col1 or col2 or col3:
    game_still_going=False
  if col1:
    return board[0]
  elif col2:
    return board[1]
  elif col3:
    return board[2]  
  else:
    return None
  
def check_diagonals():
  global game_still_going
  diagonal1= board[0]==board[4]==board[8] != "-"
  diagonal2= board[6]==board[4]==board[2] != "-"
  if diagonal1 or diagonal2:
    game_still_going=False
  if diagonal1:
    return board[0]
  elif diagonal2:
    return board[6]
  else:
    return None
  
def check_if_tie():
  return
def flip_player():
  global current_player
  if current_player =="X":
    current_player="O"
  elif current_player =="O":
    current_player="X"
  else:
    return None
  
play_game()
