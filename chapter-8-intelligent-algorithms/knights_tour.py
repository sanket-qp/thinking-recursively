import sys
import time

def print_board(board):
  """
  prints the given board on the screen
  """
  for r in range(len(board)):
    for c in range(len(board[r])):
      sys.stdout.write("| %c (%d, %d) " % (board[r][c], r, c))
    print ""

def board_full(board):
  """
  checks if a given board is full or not
  """
  for r in range(len(board)):
    for c in range(len(board[r])):
      if board[r][c] != 'x':
        return False

  return True

def next_moves(board, x, y):
  """
  finds the next possible moves from given position (x, y)
  reutns a tuple of x and y coordinates (x, y)
  """
  moves = []
  # knight can moves 2 steps in each direction
  directions = {'W': lambda x, y, unit: (x, y - unit), 'S': lambda x, y, unit: (x + unit, y), 'E': lambda x, y, unit: (x, y + unit), 'N': lambda x, y, unit: (x - unit, y)}
  # and then it moves one step at 90 degree angle
  angles = {'W': ('N', 'S'), 'S' : ('E', 'W'), 'E': ('S', 'N'), 'N': ('E', 'W')}
  for d in directions.keys():
    # move two steps in this direction    
    steps = 2
    x1, y1 = directions[d](x, y, steps)
    for d1 in angles[d]:
      steps = 1
      x2, y2 = directions[d1](x1, y1, steps)
      if x2 < 0:
        continue
      if x2 > len(board) - 1:
        continue
      if y2 < 0:
        continue
      if y2 > len(board) - 1:
        continue
      moves.append((x2, y2))
  return moves

def knights_tour(board, x, y, path):
  """
  solves knight's tour
  path is populated as successful list of steps
  """

  # base cases
  # (i) if board is full, then we're done
  if board_full(board):
    return True

  # (ii) if given cell is visited, then not a valid path
  if board[x][y] == 'x':
    return False
  else:
    pass
    # find next moves
    moves = next_moves(board, x, y)
    if not moves and not board_full(board):
      return False
    else:
      # and keep looking while for a path recursively for each of the possible move until a good one found
      index = 0
      # visit the current cell
      board[x][y] = 'x'
      found = False
      move = moves[index]
      while not found and index < len(moves):
        move = moves[index]
        found = knights_tour(board, move[0], move[1], path)
        index += 1

      # if not found, then backtrack
      if not found: board[x][y] = ' '
      else:
        # store this cell as a successful step in path
        path.append((x, y))

      return found

def main():
  n = 5
  # create a board of n x n
  board = [[' ' for x in range(n)] for y in range(n)]
  # final path will be saved in following list
  path = []
  knights_tour(board, 4, 4, path)
  
  if not path:
    print "path from given cell doesn't exist"
    sys.exit(0)

  # reverse the path, because it'll need to backtracked to first successful step in the path
  path.reverse()
  blank_board = [[' ' for x in range(n)] for y in range(n)]
  for cell in path:
    print "(%d, %d)" % (cell[0], cell[1])
    blank_board[cell[0]][cell[1]] = 'x'
    print_board(blank_board)
    print "---------------------------"
    print ""
    time.sleep(1)

if __name__ == "__main__":
  main()
