def main():
  # Read a Sudoku puzzle
  grid = readAPuzzle()

  if not isValidGrid(grid):
    print("Invalid input")
  elif search(grid):
    print("The solution is found:")
    printGrid(grid)
  else:
    print("No solution")

  return 0

# Read a Sudoku puzzle from the keyboard 
def readAPuzzle():  
  print("Enter a Sudoku puzzle:")
  grid = []
  for i in range(9):
    line = input().split()
    grid.append([eval(x) for x in line])
  return grid               

# Obtain a list of free cells from the puzzle 
def getFreeCellList(grid):
  freeCellList = []
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        freeCellList.append([i, j])

  return freeCellList

# Display the values in the grid 
def printGrid(grid):
  for i in range(9):
    for j in range(9):
      print(grid[i][j], end = " ")
    print()

# Search for a solution 
def search(grid):
  freeCellList = getFreeCellList(grid)
  numberOfFreeCells = len(freeCellList)
  if numberOfFreeCells == 0:
    return True # No free cells

  count = 0 # Multiple solutions: Count for 3 solutions
  k = 0 # Start from the first free cell
  done = False 
  while not done:
    i = freeCellList[k][0]
    j = freeCellList[k][1]
    if grid[i][j] == 0:
      grid[i][j] = 1 # Fill the free cell with number 1

    if isValid(i, j, grid):
        if k + 1 == numberOfFreeCells: # No more free cells
          # A solution is found
          count += 1
          if count < 3: # Display the first two solutions
            print("Sample solution " + str(count) + ":")
            printGrid(grid) # Multiple solutions: print a solution

          # Now search for the next possible solution
          if grid[i][j] < 9:
            grid[i][j] = grid[i][j] + 1 # Check the next possible value
          else: # grid[i][j] is 9, backtrack
            while grid[i][j] == 9:
              grid[i][j] = 0 # Reset to free cell
              if k == 0:
                done = True # No possible value any more, done!
                return count 

              k -= 1 # Backtrack
              i = freeCellList[k][0]
              j = freeCellList[k][1]

            grid[i][j] = grid[i][j] + 1 # Check the next possible value

        else: # Move to the next free cell
          k += 1

    elif grid[i][j] < 9:
      # Fill the free cell with the next possible value
      grid[i][j] = grid[i][j] + 1 
    else:
      # grid[i][j] is 9, backtrack
      while grid[i][j] == 9:
        grid[i][j] = 0 # Reset to free cell
        if k == 0:
            done = True # No possible value any more, done!
            return count
        k -= 1 # Backtrack to the preceding free cell
        i = freeCellList[k][0]
        j = freeCellList[k][1]

      # Fill the free cell with the next possible value, 
      # search continues from this free cell at k
      grid[i][j] = grid[i][j] + 1 

  return count # A solution is found

# Check whether grid[i][j] is valid in the grid 
def isValid(i, j, grid):
  # Check whether grid[i][j] is valid at the i's row
  for column in range(9):
    if column != j and grid[i][column] == grid[i][j]:
      return False

  # Check whether grid[i][j] is valid at the j's column
  for row in range(9):
    if row != i and grid[row][j] == grid[i][j]:
      return False

  # Check whether grid[i][j] is valid in the 3-by-3 box
  for row in range((i // 3) * 3, (i // 3) * 3 + 3):
    for col in range((j // 3) * 3, (j // 3) * 3 + 3):
      if row != i and col != j and grid[row][col] == grid[i][j]:
        return False

  return True # The current value at grid[i][j] is valid

# Check whether the fixed cells are valid in the grid 
def isValidGrid(grid): 
  for i in range(9):
    for j in range(9):
      if grid[i][j] < 0 or grid[i][j] > 9 or (grid[i][j] != 0 and not isValid(i, j, grid)): 
        return False

  return True # The fixed cells are valid

main()
