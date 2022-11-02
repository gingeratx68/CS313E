#  File: Tower.py

#  Description: tower of hanoi with 4 pegs instead of 3 

#  Student's Name: Ginger Hudson

#  Student's UT EID: gsh628

#  Partner's Name: Mehul Gupta

#  Partner's UT EID: mdg3739

#  Course Name: CS 313E 

#  Unique Number: 52530

#  Date Created: 10/12/22

#  Date Last Modified: 10/14/22


import sys, math 
"""
def towers(n, source, spare, dest):
    if (n==1):
        #move disc from source to destination
        print("move disk from", source, "to", dest)
    else:
        #move disc, from source to spare, using destination as spare
        towers(n-1, source, dest, spare)
        print("move disk from", source, "to", dest)
        towers(n-1, spare, source, dest)
def main():
    towers(3, 'A', 'B', 'C')

main()


notes from class on this assignment
-add another spare disk
-First move the topmost disks (say the top k disks) to one of the spare needles, say spare1.
-Then move n - k - 1 disks to spare2.
-Move the largest disk from source to destination.
-Move the n - k - 1 disks from spare2 to destination.
-Finally, move the top k disks from spare1 to destination.
"""
  




# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
    k=math.floor(n-(2*n+1)**.5+1)
    #print(k, "jib")
    #base cases 
    if n==0:
        return 0
    if n == 1:
        return 1
    else:
        #print((2*num_moves(k)), "jib")
        #print((2 **(n-k)-1), "cat")
        #implement formula of 2**(n)-1 for calculating moves and add recursive call to k(moves left needed to make)
        return (2 **(n-k)-1) + (2*num_moves(k))
          
        
def main():
  # read number of disks and print number of moves
  
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    
  #num_disks=28
    print (num_moves (num_disks))
    
    
if __name__ == "__main__":
  main()

