# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name:

# Student UT EID:

# Course Name: CS 313E

# Unique Number:

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

class Triangle (object):
   # constructor
   # TODO: YOUR CODE HERE
  def __init__(self, a=0, b=0, c=0):
    self.a=a
    self.b=b
    self.c=c
    self.length_a=dist(self.a)
    self.length_b=dist(self.b)
    self.length_c=dist(self.c)
    
    # print string representation of Triangle
    # TODO: YOUR CODE HERE
  def __str__(self):
    return 'Point1: ' + str(self.a) + ', Point2: ' + str(self.b) + ', Point3: ' + str(self.c)
    
    # check if the triangle is similar to another triangle
    # TODO YOUR CODE HERE
    
    # check if triangle is obtuse or not
    # TODO: YOUR CODE HERE
  def is_obtuse(self):
    if self.length_a**2 + self.length_b**2< self.length_c**2:
      return True
    else:
      return False
    
    # check if triangle is scalene
    # TODO YOUR CODE HERE
  def is_scalene(self):
    eps=1e-8
    if abs(self.length_a-self.length_b)<eps and abs(self.length_a-self.length_c)<eps and abs(self.length_c-self.length_b)<eps:
      return True
    else:
      return False 

      

######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print('A', triangleA)
    print('B', triangleB)

    print('A obtuse', triangleA.is_obtuse())
    print('B obtuse', triangleB.is_obtuse())

    print('A scalene', triangleA.is_scalene())
    print('B scalene', triangleB.is_scalene())

    print('A equals b', triangleA == triangleB)

if __name__ == "__main__":
    main()
