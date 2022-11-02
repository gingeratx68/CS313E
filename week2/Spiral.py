
#  File: Spiral.py

#  Description:
"""We will use our own input file to test your program. You must read the input in the format described above.
Once you read the first line from the input file you will create a 2-D list with the spiral of numbers. Then from the 2-D list you will obtain the sum of adjacent numbers
for a given number in the spiral and print it. The number of lines of input will be arbitrary and greater than 1."""

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 8/29/22

#  Date Last Modified:

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
import sys
import math

def create_spiral ( n ):
    #n=n.pop(0)
    #print(n)
    #matrix=[[0]* (n) for x in range(n)]
    matrix=[]
    level_list=[]
    for a in range(n):
        for a in range(n):
            level_list.append("")
        matrix.append(level_list)
        level_list=[]
    #print(matrix)
    #start at 2 in rotation of spiral 
    val=2
    #now start at middle point of 1
    row=int(n/2)
    col=int(n/2)
    #middle of zero matrix is 1
    matrix[row][col]=1
    for x in range(0,n):
        if (x%2==0):
            #if even
            for y in range(x):
                col-=1
                #revise left value to the matrix
                matrix[row][col]=val
                #add one to counter
                val+=1

            for y in range(x):
                row-=1
                #revise right value to the matrix
                matrix[row][col]=val
                #add one to counter
                val+=1

        else:
            #if odd
            for y in range(x):
                col+=1
                #revise 
                matrix[row][col]=val
                val+=1

            for y in range(x):
                row+=1
                
                matrix[row][col]=val
                val+=1
    for x in range(1,n):
        col+=1
        matrix[row][col]=val
        val+=1
    #print(matrix)
    return(matrix)
    
    

              
                    
           
def sum_adjacent_numbers (spiral, n):
    #print(spiral)
    #index given number
    index=0
    side_length=len(spiral)
    if n>(side_length**2):
        return 0
    for i in spiral:
        if n in i:
            spi_index=([index, i.index(n)])
        index+=1
    #print(spi_index)
    row =spi_index[0]
    #print(row)
    col=spi_index[1]
    #print(col)

    direction=[[0,1],[1,1],[1,-1],[-1,0],[1,0],[-1,1],[0,-1],[-1,-1]]

    sum_vals=0

    for x in direction:

        sur_row = x[0] + row

        sur_col = x[1] + col

 

        if 0<=sur_col<side_length and 0<=sur_row<side_length:
            #print("jiby: %s %s %s " %(sur_row,sur_col, spiral[sur_row][sur_col]))
            sum_vals += spiral[sur_row][sur_col]

 

    return sum_vals
def main():
    str1=sys.stdin.readline()
    str1=str1.strip()
    n=int(str1)
    #print(n)
    create_spiral(n)
    adjacents=sys.stdin.readlines()
    #print(adjacents)
    for line in adjacents:
        line=int(line.strip())
        #print(line)
                 
    #create_spiral(n)
        answer=sum_adjacent_numbers(create_spiral(n), line)
        print(answer)
   
  # create the spiral

  # add the adjacent numbers

  # print the result

if __name__ == "__main__":
  main()
