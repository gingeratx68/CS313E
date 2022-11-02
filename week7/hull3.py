#  File: Hull.py

#  Description:

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628

#  Partner Name: Mehul Gupta 

#  Partner UT EID: mdg3739  

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/25/2022

#  Date Last Modified: 9/26/2022

import sys
import math


class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)



def det(p, q, r):
    # determinant
  det = (p.x * q.y) + (q.x * r.y) + (r.x * p.y) - (p.y * q.x) - (q.y * r.x) - (r.y * p.x)

  if det == 0:
    return 'flat'
  elif det < 0:
    return 'right'
  elif det > 0:
    return 'left'


def area_poly(hull):
    
    return 


def convex_hull(sorted_points):
  #create empty upper hull
  #print(sorted_points)
  upper_hull=[]
  # Append the first two points p_1 and p_2 in order into the upper_hull.
  upper_hull = [sorted_points[0], sorted_points[1]]
  #For i going from 3 to n
  for i in range(2, len(sorted_points)):
    #Append p_i to upper_hull.
    upper_hull.append(sorted_points[i])
    #While upper_hull contains three or more points and the last three points in upper_hull do not make a right turn do
    while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-1], upper_hull[-2]) != "right":
      #Delete the middle of the last three points from upper_hull
      upper_hull.pop(-2)

  #create empty lower hull
  lower_hull=[]
  #Append the last two points p_n and p_n-1 (-2) in order into lower_hull with p_n(-1) as the first point.
  lower_hull = [sorted_points[-1], sorted_points[-2]]
  #For i going from n - 2 downto 1

  #print(len(sorted_points))
  for i in range(len(sorted_points) - 2, 0, -1):
    #print(i)
    #Append p_i to lower_hull
    lower_hull.append(sorted_points[i])
    # While lower_hull contains three or more points and the last three points in the lower_hull do not make a right turn do
    while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-1], lower_hull[-2]) != "right":
      #Delete the middle of the last three points from lower_hull
      lower_hull.pop(-2)

  #now combine the upper and lower hulls
  # Remove the first and last points for lower_hull to avoid duplication with points in the upper hull.
  lower_hull.pop(0)
  lower_hull.pop(-1)
  #extend adds elements of lower_hull to end of upper_hull
  upper_hull.extend(lower_hull)
  hull = [upper_hull.pop(0)]
  #print(hull)
  hull.extend(reversed(upper_hull))

  return hull


def main():
  # create an empty list of Point objects
  point_list = []
  # read number of points
  num_points = sys.stdin.readline()
  lines = sys.stdin.readlines()
  
  # read file and create new point for each line
  for line in lines:
    strip_line= line.strip("\n")
    split_line= strip_line.split()
    point_list.append(Point(int(split_line[0]), int(split_line[1])))

  #sort by x value 
  sorted_points = sorted(point_list)
  #print(sorted_points)
  #for zz in sorted_points:
    #print(zz.x, zz.y, zz)
  
  #call convex_hull which deals with upper/lower hull 
  hull = convex_hull(sorted_points)
  #print(hull)
  area=area_poly(hull)
  
  #output prints
  print('Convex Hull')
  for point in hull:
    print('(%s, %s)' % (point.x, point.y))
  print('')
  #print('Area of Convex Hull = %s' % (

if __name__ == "__main__":
    main()
