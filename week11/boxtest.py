#  File: Boxes.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
  big_boi_boxes_list = []
  trying_list = []
  answer = all_combos (box_list, big_boi_boxes_list, trying_list, 0)

  #return answer
  return big_boi_boxes_list

def all_combos (box_list, big_boi_boxes_list, trying_list, lower):
  
  high = len(box_list)
  if lower == high:
    if(len(trying_list) >= 4):
        big_boi_boxes_list.append(trying_list)
        return big_boi_boxes_list

  else:
    attempt = trying_list[:]
    trying_list.append(box_list[lower])
    if fitcheck(trying_list):
        all_combos(box_list, big_boi_boxes_list, trying_list, lower+1)
    if fitcheck(attempt):
        all_combos(box_list, big_boi_boxes_list, attempt, lower+1)
    else:
        lower+=1

def fitcheck (try_list):
  
  check = True
  for i in range(len(try_list)-1):
    check = does_fit(try_list[i], try_list[i+1])
    if (not check):
        return check
  return check

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  box_list = [[23,70,90],[48,56,99],[79,89,91],[70,74,91],[53,56,91],[22,39,56],[29,62,64],\
    [15,85,92],[23,61,78],[51,52,96],[49,67,95],[25,93,98],[57,82,94],[46,93,95],[32,38,50],\
    [27,50,89],[60,60,66],[37,43,66],[14,27,62],[16,40,90]]

  # print to make sure that the input was read in correctly
  #print (box_list)
  #print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  #print (box_list)
  #print()

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes = nesting_boxes (box_list)
  #print(max_boxes)
    
  # print the largest number of boxes that fit
  #print (max_boxes)
  #maxList = max((x) for x in max_boxes)
  maxLength = max(len(x) for x in max_boxes)
  maxNested=len(max_boxes)
  print(maxLength)
  print(maxNested)
  
    
  # print the number of sets of such boxes

if __name__ == "__main__":
  main()
