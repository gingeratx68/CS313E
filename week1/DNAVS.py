
#  File: DNA.py

#  Description: finding the longest common base sequence in two DNA strands

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628 

#  Partner Name: 

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 8/25/22

#  Date Last Modified:

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

import sys
def longest_subsequence (s1, s2):
    #in the case string is too short or empty 
    temp=""
    longest=""
    s1=s1.casefold
    s2=s2.casefold
    if s1==[]:
        return ""
    if len(s1)==1:
        return 0
    if s2==[]:
        return ""
    if len(s2)==1:
        return 0
  
        

    #create empty list
    lst=[]
    #nested loop
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if [i==j]:
                append.lst()
                

                
            
def main():
  # read the data
    dnafile=open("dna.in.txt")
    
    #lines=dnafile.readlines()
    lines_all=int(sys.stdin.readline(dnafile))
    for char in range(lines_all):
        s1=sys.stdin.readline().strip()
        s2=sys.stdin.readline().strip()
        answer=longest_subsequence()
        print(results)
  # for each pair
    # call longest_subsequence
    
    # write out result(s)

	# insert blank line

if __name__ == "__main__":
  main()
