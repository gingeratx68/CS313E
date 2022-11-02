#  File: Boxes.py

#  Description: with a list of boxes(length, width, heighth), determine max number of subsets that can be created
# by boxes fiting each other, and return max subsets and max length of subset

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628

#  Partner Name: Mehul Gupta

#  Partner UT EID: mdg3739

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/16/22

#  Date Last Modified: 10/18/22

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

  #return nested answer
  return big_boi_boxes_list

def all_combos (box_list, big_boi_boxes_list, trying_list, lower):
  #subset algorithm 
  high = len(box_list)
  #if at end of hi
  if lower == high:
    if(len(trying_list) >= 2):
        big_boi_boxes_list.append(trying_list)
        return big_boi_boxes_list

  else:
    #make copy of basket
    attempt = trying_list[:]
    trying_list.append(box_list[lower])
    #check, if it will nest and go to next element
    if fitcheck(trying_list):
        all_combos(box_list, big_boi_boxes_list, trying_list, lower+1)
    if fitcheck(attempt):
        all_combos(box_list, big_boi_boxes_list, attempt, lower+1)
    else:
        lower+=1

def fitcheck (try_list):
  #check if the boxes will nest on each other 
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
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  #print (box_list)
  #print()

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
  #print(max_boxes)


  if len(max_boxes)<2:
    print(1)
    print(len(box_list))
  else:
    maxLength = max(len(x) for x in max_boxes)
    val=maxLength
    sub_len=[]
    for i in max_boxes:
      if len(i)==val:
        sub_len.append(1)
    print(maxLength)
    print(len(sub_len))


  #print(sub_len)
  #maxNested=len(max_boxes)
 

  
    
  # print the number of sets of such boxes

if __name__ == "__main__":
  main()
