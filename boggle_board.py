import random

class BoggleBoard:
  
  def __init__(self):
    self.board = ['-  -  -  -'] * 4
    # self.print_board()

  def print_board(self):
    for row in self.board:
      print(row)
    print() 

  def shake(self):
    
    dice = [
      ['R ', 'I ', 'F ', 'O ', 'B ', 'X '],
      ['I ', 'F ', 'E ', 'H ', 'E ', 'Y '],
      ['D ', 'E ', 'N ', 'O ', 'W ', 'S '],
      ['U ', 'T ', 'O ', 'K ', 'N ', 'D '],
      ['H ', 'M ', 'S ', 'R ', 'A ', 'O '],
      ['L ', 'U ', 'P ', 'E ', 'T ', 'S '],
      ['A ', 'C ', 'I ', 'T ', 'O ', 'A '],
      ['Y ', 'L ', 'G ', 'K ', 'U ', 'E '],
      ['Qu', 'B ', 'M ', 'J ', 'O ', 'A '],
      ['E ', 'H ', 'I ', 'S ', 'P ', 'N '],
      ['V ', 'E ', 'T ', 'I ', 'G ', 'N '],
      ['B ', 'A ', 'L ', 'I ', 'Y ', 'T '],
      ['E ', 'Z ', 'A ', 'V ', 'N ', 'D '],
      ['R ', 'A ', 'L ', 'E ', 'S ', 'C '],
      ['U ', 'W ', 'I ', 'L ', 'R ', 'G '],
      ['P ', 'A ', 'C ', 'E ', 'M ', 'D ']
    ]
    # Setup
    # Randomly shuffles all dice.
    random.shuffle(dice)
    dice_on_board = {}
    # Puts dice on board.
    for i in range(16):
      dice_on_board.update({i: dice[i]})
    choose_from = []
    row = ''
    self.board = []
    # Looping through dice, and appending random letters from each die to the list, choose_from.
    for i in dice_on_board:
      # Rolling dice[i] - each die is 6 sided.
      choose_from.append(dice_on_board[i][random.randint(0,5)])
      # Adds 3 letters to the row.
      if i == 3 or i == 7 or i == 11 or i == 15:
        row += f'{choose_from[-1]}'
        self.board.append(row)
        row = ''
      else:  
        row += f'{choose_from[-1]} '
        
    game.print_board()

# Driver Code
game = BoggleBoard()
game.shake()