
# Description: Determine if a string of brackets is organized legally. 
# Student Name: Ginger Hudson
# Student UT EID: gsh628
# Course Name: CS 313E
# Unique Number: 52530


# Input: any valid string
# Output: the string "true" if it is valid, "false" if is not

import sys
def valid(s):
    # TODO: Implement me!
    #for every open bracket in the s there must be a close bracket for it to be true
    #if there is a close bracket with no open bracket then it is false
    #if there is an open bracket with no close bracket then it is false
    """
    count=0
    for i in range(len(s)):
        #print("yeet")
        if s[i] == "[":
            #iterate over s[i+1:] to find matching closing paranthesis
            for j in range(i+1,len(s)):
                #print(type(j))
                #print(j)
                if "]" in s[j]:
                    print("found2")
                    count+=0
                else:
                    count+=1
        
        if s[i] == "{":
            #print("yes")
            for j in range (i+1, len(s)):
                if "}" in s[j]:
                    print("found1")
                    count+=0
                else:
                    count+=1
            
        if s[i] == "(":
            for j in range (i+1, len(s)):
                if ")" in s[j]:
                    print("found")
                    count+=0
                else:
                    count+=1
    #temporary, change return when writing code

    print(count)
    if count==0:
        return "true"
    else:
        return "false"
    """
    brackets_left=0
    brackets_right=0
    paren_left=0
    paren_right=0
    squiggle_left=0
    squiggle_right=0
    for i in range(len(s)):
        if s[i]=="[":
            brackets_left+=1
        if s[i]=="]":
            brackets_right+=1
        if s[i]=="(":
            paren_left+=1
        if s[i]==")":
            paren_right+=1
        if s[i]=="{":
            squiggle_left+=1
        if s[i]=="}":
            squiggle_right+=1
    if brackets_left==brackets_right and paren_left==paren_right and squiggle_left==squiggle_right:
        return "true"
    else:
        return "false"

   
   
def main():
    #read the input file from stdin
    string = sys.stdin.readline().strip()
    #string="(((((((((())))))))))"
    print(valid(string)) 
    
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
