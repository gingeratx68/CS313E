#  File: Palindrome.py

#  Description: check if a palindrome, if not palindrome, start from end of string and append to the front in reversed order until it is a palindrome

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628

#  Partner Name: Mehul Gupta 

#  Partner UT EID:mdg3739  

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/2/22

#  Date Last Modified:10/3/22
import sys
# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string

def smallest_palindrome(str):
    #create new variable that is str backwards
    rev=str[::-1]
    #print(rev)
    #if empty string just return empty
    if len(str)==0:
        return ''
    #if len 1, return the string
    if len(str)==1:
        return str
    #if palindrome return the string
    if str==rev:
        return str
    #adjust to make palindrome
    else:
        #traverse len of string
        for i in range(len(str)):
            #print(i)
            #if the string starts with character i to the end 
            if str.startswith(rev[i:]):
                #new=str.startswith(rev[i:])
                #print(new)
                #then return the string with the reversed string of that character to the end of string and add to
                #BEGINNING of the string 
                return rev[:i]+str
    """
    notes from ta
    
    for i in len(str):
    set an end to len str-i
        return str[len(str)-1:end:-1]+str
    isPalindome(str[0:end+1}
    
    if isPalindrome(str):
        return str


    fail reels
    
    else:
        #while new_string is not a palindrome
        while not isPalindrome(str):
            new_string=str[counter:counter:-1]+str
            #print("jib")
            if isPalindrome(new_string):
                return new_string
            else:
                counter-=1
            
    return new_string
"""
"""          
    else:
        new_string=str
        counter=-1
        #add last character to the front of the string
        while new_string != new_string[::-1]:
            #if the last character to the front of the string added to the front of the string is a palindrome
            if new_string[counter] + new_string == new_string[counter] + new_string[::-1]:
                return new_string[counter] + new_string

            else:
                #add the reversed of counter and counter -1 to the front of the string
                new_string = new_string[counter] + new_string[counter-1] + new_string
                counter -= 1
                return new_string
        """ 

                
#Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
    # run your test cases
    '''
    print (test_cases())
    '''
    #read lines of file
    data=sys.stdin.readlines()
    #read each line as a different string
    for line in data:
        #remove whitespace
        line=line.strip()
        #check if string is a palindrome
        smallest_palindrome(line)
        #print smallest palindrome
        print(smallest_palindrome(line))
    # read the data
    
    # print the smallest palindromic string that can be made for each input
  
if __name__ == "__main__":
  main()
