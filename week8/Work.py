#  File: Work.py 

#  Description:  determine how many lines of code a programmer can write affected by cups of coffee and lowered productivity 

#  Student Name: Ginger Hudson 

#  Student UT EID: gsh628 

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/28/2022

#  Date Last Modified: 9/30/22

import sys, time
"""
v=lines of code
k=productivity factor
p=cups of coffee affecting productivity
n= number of lines of code to write
"""

#helper function to calc number of lines he can write after each coffee cup
def num_lines(v, k):
    #pre coffee number of lines
    #v=lines
    #k=productivity factor
    p=1
    total_lines=v
    #lines divided floor by k^count
    while v//k**p !=0:
        #total lines will decrease by n//k**p (track productivity with dif values of k and n )
        total_lines+=v//k**p
        p+=1
    return total_lines

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  # use linear search here
    for i in range(1, n+1):
        if num_lines(i, k)>=n:
            #return i which is the number of lines between 0-n that he must write
            return i
    return 0


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
    # use binary search here
    #set hi to n 
    hi = n
    #set low as the first number in n
    low = 1
    
    while low <= hi:
        #mid point between hi and low
        mid = (hi + low) // 2
        #number of lines from midpoint on
        lines = num_lines(mid, k)
        #if the lines is greater than n and mid -1 is not return middle value 
        if num_lines(mid,k)>=n and num_lines(mid-1,k)<n:
            return mid
        #if the lines is less than n, keep checking from low up 
        elif lines < n:
            low = mid + 1
        #if lines is greater check from hi down 
        elif lines > n:
            hi = mid - 1
        #if lines is = to n just return to the middle 
        else:
            return mid

    return 0



  


# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
