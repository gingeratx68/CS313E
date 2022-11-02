#  File: Triangle.py

#  Description: find the greatest sum from a path down in a triangle with four different algorithm methods 

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628 

#  Partner Name: Mehul Gupta 

#  Partner UT EID: mdg3739

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/9/22

#  Date Last Modified: 10/10/22

import sys

from timeit import timeit


    
    
# returns the greatest path sum using exhaustive search
    #sum all paths 16k+ sums 
 
def getpaths(row, col, path, rooted_paths, grid):
    # Cumulative solution list is 'rooted_paths'.
    if row < len(grid):
        entry = grid[row][col]
        for cc in [col, col + 1]:
            getpaths(row+1, cc, path + [entry], rooted_paths, grid)
        # Record result.
        if row == len(grid) - 1:
            rooted_paths.append(path + [entry])
            print("SOLN_LIST: %s :" % (path + [entry]))
    return rooted_paths


def brute_force (grid):
    all_paths = getpaths(0, 0, [], [], grid)
    max_value = 0
    for xx in all_paths:
        if sum(xx) > max_value:
            max_value = sum(xx)
    #print("BRUTE_FORCE: %s %s" % (len(all_paths), max_value))
    return max_value

 



# returns the greatest path sum using greedy approach
def greedy (grid):
    #look at local max so from 75 look at 95 and 64 
    i = 1
    j = 0
    sum = grid[0][0]
    while i<len(grid):
        row2 = grid[i]
        if row2[j] > row2[j+1]:
            sum+=row2[j]
        else:
            sum+=row2[j+1]
            j+=1
        i+=1

    return sum


def getpaths_div(row, col, path, max_value, grid):
    # Cumulative sum list is 'max_value'.
    if row < len(grid):
        entry = grid[row][col]
        for cc in [col, col + 1]:
            max_value = getpaths_div(row+1, cc, path + [entry], max_value, grid)
        # Record result.
        if row == len(grid) - 1:
            sum_temp = sum(path) + entry
            if sum_temp > max_value:
                max_value = sum_temp
            #print("SOLN_LIST: %s :%s ,%s" % (path + [entry],sum_temp,max_value))
    return max_value

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    max_valueX = getpaths_div(0, 0, [], 0, grid)
    #print("DIV_XXX: %s" % (max_valueX))
    return max_valueX

 

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    i = len(grid)-1
    sum = 0
    while i>0:
        j = 0
        #while j < len(grid[i-1]):
        while j < len(grid[i])-1:
            grid[i-1][j] = grid[i-1][j] + max(grid[i][j], grid[i][j+1])
            j+=1
        grid.pop(i)
        i-=1
    sum = grid[0][0]
    return sum

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print("The greatest path sum through exhaustive search is ")
  print(brute_force(grid))
  print("The time taken for exhaustive search in seconds is ")
  print(times)
  print("")
  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print("The greatest path sum through greedy search is ")
  print(greedy(grid))
  print("The time taken for greedy approach in seconds is ")
  print(times)
  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print("The greatest path sum through recursive search is ")
  print(divide_conquer(grid))
  print("The time taken for recursive search in seconds is ")
  print(times)
  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  print("The greatest path sum through dynamic programming is ")
  print(dynamic_prog(grid))
  print("The time taken for dynamic programming in seconds is ")
  print(times)
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()
