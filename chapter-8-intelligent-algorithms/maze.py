import os
import sys
import time
# some constants
WALL = '#'
OPEN = ' '
FINISH = 'F'

def print_maze(maze):
  for r in range(len(maze)):
    for c in range(len(maze)):
      sys.stdout.write("| %c (%d, %d) " % (maze[r][c], r, c))
    print ""

  
def next_moves(maze, x, y):
  """
  find next possible moves from given cell
  """
  moves = []
  # can be moved in each direction by one step
  directions = {'W': lambda x, y: (x, y-1), 'S': lambda x, y: (x+1, y), 'E': lambda x, y: (x, y+1), 'N': lambda x, y: (x-1, y)}
  for d in directions.keys():
    x1, y1 = directions[d](x, y)

    if x1 < 0:
      continue

    if x1 > len(maze) - 1:
      continue

    if y1 < 0:
      continue

    if y1 > len(maze) - 1:
      continue

    moves.append((x1, y1))
                 
  return moves

def solve_maze(maze, x, y, path):
  # base case
  # (i) if current point is FINISH point, then maze has been solved
  if maze[x][y] == FINISH:
    return True

  # (ii) if it's a WALL, then no point exploring further
  if maze[x][y] == WALL:
    return False

  # (iii) if it's already visited
  if maze[x][y] == 'x':
    return False
  # recursive case
  else:
    # find possible moves from given point
    moves = next_moves(maze, x, y)
    if not moves:
      return False
  
    # mark this cell as visited
    maze[x][y] = 'x'
    found = False
    index = 0
    while not found and index < len(moves):
      move = moves[index]
      found = solve_maze(maze, move[0], move[1], path)
      index += 1
 
    # backtrack 
    if not found: maze[x][y] = OPEN
    else: path.append((x, y))

  return found


def get_maze():
  return [
          [WALL, FINISH, OPEN, OPEN, WALL], 
          [WALL,   WALL, WALL, OPEN, WALL], 
          [WALL,   WALL, OPEN, OPEN, WALL], 
          [OPEN,   WALL, WALL, OPEN, WALL], 
          [WALL,   OPEN, OPEN, OPEN, WALL]
          ]

def main():
  maze = get_maze()
  path = []
  solve_maze(maze, 4, 1, path)
  if not path:
    sys.exit("maze can't be solved")
  print_maze(maze)
  path.reverse()

  maze = get_maze()
  for cell in path:
    maze[cell[0]][cell[1]] = 'x'
    os.system('clear')
    print_maze(maze)
    time.sleep(1)

if __name__ == "__main__":
  main()
