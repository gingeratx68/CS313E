#  File: Spiral.py

#  Description: encrypt text/string by rotating a 2d list clockwise, decrypt by rotating the text/string counter clockwise

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/11/22

#  Date Last Modified: 9/12/22

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string
import sys
import math

def encrypt ( strng ):
    #assign L
    L=len(strng)
    #find the closest square
    L_squared=math.sqrt(L)
    #print(L_squared)
    upper=math.ceil(L_squared)**2
    #print(upper)
    if L_squared==upper:
        M=upper
    if upper>L_squared:
        M=upper
    #print(M)
    #get size of 2d matrix or K
    K=math.sqrt(M)
    K=math.floor(K)
    
    #convert the string to a 2d matrix
    matrix=[[0]* (K) for x in range(K)]
    #print(matrix)
    
    #make the string with padding
    for char in range(M-L):
        strng += '*'
      
    #fill matrix with padded string   
    index=0
    for i in range(K):
        for j in range(K):
            matrix[i][j]=strng[index]
            index+=1
    
    #clockwise rotator
    #set a new list to catch the rotating string and a temp list for rotation process
    new_word=[]
    temp=[]
    for i in range(K // 2):
        for j in range(i, K - i - 1):
            #assign the temp 
            temp = matrix[i][j]
            matrix[i][j] = matrix[K - 1 - j][i]
            matrix[K - 1 - j][i] = matrix[K - 1 - i][K - 1 - j]
            matrix[K - 1 - i][K - 1 - j] = matrix[j][K - 1 - i]
            matrix[j][K - 1 - i] = temp
    #print(matrix)
    new_word=sum(matrix, [])
    #print(new_word)
    
    #merge new list to string, remove * and spaces
    for letter in new_word:
        if '*' in new_word:
            new_word.remove('*')
    
    #return (*new_word, sep='')
    answer=''.join(new_word)
    return(answer)

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
    #assign L
    L=len(strng)
    #find the closest square
    L_squared=math.sqrt(L)
    #print(L_squared)
    upper=math.ceil(L_squared)**2
    #print(upper)
    if L_squared==upper:
        M=upper
    if upper>L_squared:
        M=upper
    #print(M)
    #get size of 2d matrix or K
    K=math.sqrt(M)
    K=math.floor(K)
    
    #convert the string to a 2d matrix
    matrix=[[0] * (K) for x in range(K)]
    #print(matrix)
    
    #make the string with padding
    for char in range(M-L):
        strng += '*'
    #print(strng)
    
    #fill matrix with padded string   
    index=0
    for i in range(K):
        for j in range(K):
            matrix[i][j]=strng[index]
            index+=1
    #print(matrix)
            
    #counter clockwise rotator
    #set a new list to catch the rotating string and a temp list for rotation process
    new_word=[]
    temp=[]
    #rotate from the end of matrix  
    matrix=[i[::-1] for i in matrix]
    for i in range(K // 2):
        for j in range(i, K - i - 1):
            #assign the temp 
            temp = matrix[i][j]
            matrix[i][j] = matrix[K - 1 - j][i]
            matrix[K - 1 - j][i] = matrix[K - 1 - i][K - 1 - j]
            matrix[K - 1 - i][K - 1 - j] = matrix[j][K - 1 - i]
            matrix[j][K - 1 - i] = temp
    #print(matrix)
    #start from end again 
    matrix=[i[::-1] for i in matrix]
    new_word=sum(matrix, [])
    
    #merge new list to string, remove *(if there is extra padding) and spaces
    for letter in new_word:
        if '*' in new_word:
            new_word.remove('*')
    #print(new_word)
    #return(*new_word, sep='')
    answer=''.join(new_word)
    return(answer)
    
    """
    temp=[]
    for i in range(0, int(M/2)):
        for j in range(i,M-i-1):
            #assign tbe temp
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][M-1- i]
            matrix[j][M-1-i] = matrix[M-1- i][M- 1-j]
            matrix[M-1- i][M-1-j]= matrix[M-1-j][i]
            matrix[M-1 -j][i] = temp
    new_word=sum(matrix, [])
    
    new_word=[]
    for a in range(K):
        for b in range(K *(K*-1)):
            new_word+=matrix[b][a]
    """

    
def main():
  # read the two strings P and Q from standard imput
    lines=sys.stdin.readlines()
    line_counter=0
    for line in lines:
        if line_counter==0:
            P=str(line).strip()
        if line_counter==1:
            Q=str(line).strip()
            
        line_counter+=1
    #print(P)
    #print(Q)

    print(encrypt(P))
    print(decrypt(Q))
  # encrypt the string P

  # decrypt the string Q

  # print the encrypted string of P and the 
  # decrypted string of Q to standard out

if __name__ == "__main__":
  main()
