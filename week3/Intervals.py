
#  File: Interval.py

#  Description:
"""If we have two intervals like (7, 12) and (4, 9), they overlap.
We can collapse overlapping intervals into a single interval (4, 12).
But the following two intervals (-10, -2) and (1, 5) are non-intersecting
intervals and cannot be collapsed. Then with the merged intervals sort by size"""
#  Student Name: Ginger Hudson

#  Student UT EID: gsh628

#  Partner Name: fernando rodriquez

#  Partner UT EID: fr7376

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/6/22

#  Date Last Modified: 9/9/22


# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
import sys 
def merge_tuples (tuples_list):
    tuples_list_sorted = sorted(tuples_list, key=lambda x: x[0])
    #print(tuples_list_sorted)
    #return tuples_list_sorted
    
    #print(tuples_list)
    new_sorted=[]
    #set the start point
    x, y= tuples_list_sorted[0][0], tuples_list_sorted[0][1]
    #traverse the tuples list
    for i in tuples_list_sorted:
        #if the postion 0 in the tuple is greater than the starting position of y(starting at the first tuple)
        if i[0]>y:
            #theres no overlap so put that tuple into our new list
            
            new_sorted.append((x,y))
            #new_sorted.append([x,y])
            
            #then reset the x and y to the next iteration
            x,y=i[0], i[1]
            
        #check for overlap 
        else:
            #take the bigger value for overlapping and set it to y and then add it to the new list
            y=max(y, i[1])
            
    new_sorted.append((x,y))       
    #new_sorted.append([x,y])
            
    return new_sorted
    #print(new_sorted)       
# Input: tuples_list is a list of tuples denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

def sort_by_interval_size (tuples_list):
    #sort first
    #sort by interval size, y-x
    sorted_by_size=sorted(tuples_list, key=lambda a: a[1]- a[0])
    return sorted_by_size
    """
    my fails
    
    interval_size=0
    interval_dict={}
    #x, y= tuples_list[0][0], tuples_list[0][1]
    for i in tuples_list:
        x,y=i[0], i[1]
        interval_size=y-x
        interval_dict.update({interval_size: i})
        #x,y=i[0], i[1]
    sorted(interval_dict.items())
   
    return interval_dict
        """

          
        


    """
    for i in tuples_list:
        if new_sorted and i[0]<= new_sorted[-1][i]:
            #go to ending value of newsorted and change it max end and revise the newsorted
            new_sorted[-1][i]=max(new_sorted[-1][i], interval[1])
        else:
            new_sorted.append(i)
        
        if x[i+1][1]> y[0][i]:
            tuples_list.append(x[i+1][1], y[0][i+1])
        else:
            if y[0][i+1]>= y[0][i]:
                tuples_list[-1][1]=y[i+1][0]
                """
# Input: no input
# Output: a string denoting all test cases have passed
"""
def test_cases ():
    

    assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases
    assert merge_tuples([
    assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases

    return "all test cases passed"
  """  
def main():
  # open file intervals.in and read the data and create a list of tuples
    n=sys.stdin.readline()
    n=n.strip()
    #n=int(n)
    list_of_tups = []
    list_of_pairs = sys.stdin.readlines()
    #read the lines and take a position for the first and second number to add to new list of tups
    for line in list_of_pairs:
        pair_tuples= (int(line.split()[0]), int(line.split()[-1]))
        list_of_tups.append(pair_tuples)
    #print(list_of_tups)
  # merge the list of tuples
  
    #merge_tuples(list_of_tups)
    #print(merge_tuples(list_of_tups))
    print(merge_tuples(list_of_tups))
    answer=sort_by_interval_size(merge_tuples(list_of_tups))
    print(answer)
  # sort the list of tuples according to the size of the interval
    
  # run your test cases
  
  ##print (test_cases())

  # write the output list of tuples from the two functions

 #create new 
if __name__ == "__main__":
  main()
