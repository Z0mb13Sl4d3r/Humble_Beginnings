# e a module of utility functions called util.py for manipulating 2-dimensional arrays of size 4x4.
# Lehlogonolo Tshehla
# 05 May 2025


def create_grid(grid):
 """create a 4x4 array of zeroes within grid"""
 grid.clear()
 for i in range(4):
  r = []
  for rr in range(4):
   r.append(0)
  grid.append(r)

def print_grid (grid):
 """print out a 4x4 grid in 5-width columns within a box""" 
 print("+--------------------+")
 for  row in grid:
  print("|", end="")
  for val in row :
   print(f"{val<20}", end="")
  print("|")
 print("+--------------------+") 

def check_lost (grid):
 """return True if there are no 0 values and there are no
 adjacent values that are equal; otherwise False""" 
 zero = False
 equal = False
 for r in grid:
  for i in r:
   if i == 0:
    zero = True
   
   for i in range(4):
    for l in range(4):
     if l < 3:
      if grid[i][l] == grid[i][l+1]:
       equal = True
     if i< 3:
      if grid[i][l] == grid[i+1][l]:
       equal = True
 if zero == False and equal == False:
  return True
 else:
  return False

def check_won (grid):
 """return True if a value>=32 is found in the grid; otherwise 
 False""" 
 for r in grid:
  for v in r:
   if v >= 32:
    return True
 return False

def copy_grid (grid):
 """return a copy of the given grid"""
 arr = []
 for r in grid:
  row = []
  for n in r:
   row.append(n)
  arr.append(row)
 return arr

def grid_equal (grid1, grid2):
 """check if 2 grids are equal - return boolean value""" 
 for i in range(4):
  for l in range(4):
   if grid1[i][l] != grid2[i][l]:
    return False
 return True
 