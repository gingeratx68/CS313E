
#  File: DNA.py

#  Description: finding the longest common base sequence in two DNA strands

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628 

#  Partner Name: Chase Pham  

#  Partner UT EID: cjp3555

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 8/25/22

#  Date Last Modified:

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.



import sys
def longest_subsequence(s1,s2):
   a=len(s1)
   b=len(s2)
   #initialize counter array, array size is (b+1)*(a+1)
   countmatrix=[[0]*(b+1) for x in range(a+1)]
   #initialize 
   val=0
   empty=set()
   #traverse s2 by comparing the first char of s1
   for i in range(a):
      for j in range(b):
         if s1[i]==s2[j]:
           #if the string char 1st letter of s1 matches char in all of s2 increment counter by one!
            count=countmatrix[i][j]+1
            #reset the counter
            countmatrix[i+1][j+1]=count
            if count> val:
               empty=set()
               val=count
               empty.add(s1[i-count+1:i+1])
            elif count==val:
               empty.add(s1[i-count+1:i+1])
   return empty
   

   

def main():
   #st1="GAAGGTCGAA"
   #st2="CCTCGGGA"
   
   #read the number of pairs
   num_pairs= sys.stdin.readline()
    #strip of white space at beginning and end of input
   num_pairs=num_pairs.strip()
    #convert it to an integer
   
   num_pairs=int(num_pairs)
    #test if it was read correctly
   #print(num_pairs)
    
    #for each pair find the longest sequence
   for i in range (num_pairs):
      st1=sys.stdin.readline()
      st2=sys.stdin.readline()
        #strip whitespace
      st1=st1.strip()
      st2=st2.strip()
        #dont convert to int
        #convert to uppercase only
      st1=st1.upper()
      st2=st2.upper()

      #print(st1)
      #print(st2)
      
      long_sub=longest_subsequence(st1,st2)
      long_sub_l=list(long_sub)
      long_sub_l.sort()
      if len(long_sub_l)==0:
         print("No Common Sequence Found")
         print()
      else:
         for letter in long_sub_l:
            #print(type(letter))
            
            print(letter)
         print()
               
 
    #get the longest subsequences send a list
    #none return empty list"""

   #for v in long_sub:
      #print(v)
 
      
                    
if __name__=="__main__":
    #if function called main, run the function
    #now call main
    main()

