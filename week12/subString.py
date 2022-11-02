# File: Pattern.py

# Description:check if a string can be made into a palidrome by removing k characters

# Student Name: Ginger Hudson

# Student UT EID: gsh628

# Course Name: CS313E

# Unique Number: 52530

import sys

def proper_substring(s, k):
    if len(s)==0:
        return True
    if len(s)==k:
        return True
    else:
        check=remove_k(s, k)

    return check 
def remove_k(s, k):
    """
    i=0
    temp=s
    while k < len(s):
        word = s[:i] + s[i+1:]
        i+=1
        #print("jin")
        if is_palindrome(s) and i==k and len(s)==(len(temp)-k):
            print("works")
            return True 
        
    return False
    """
    if k==0:
        return is_palindrome(s)
    else:
        for i in range(len(s)):
            if remove_k(s[:i]+s[i+1:], k-1):
                return True
        return False
        
    return False
def is_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
    
# TAKE CAUTION TO EDIT BELOW THIS LINE
def main():
    s = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())
    #s= "ABCD"
    #k=1
    print(proper_substring(s, k))

if __name__ == "__main__":
    main()
