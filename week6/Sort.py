# File: Sort.py  
# Description: Sort a string by occurrences of the characters.

# Student Name: Ginger hudson
# Student UT EID: 628638
# Course Name: CS 313E
# Unique Number: 52530

# Input: any valid string
# Output: a string s in descending order based on the number of occurrences of the characters. Break ties of the same value by letting the character with the greater ASCII value come first 
import sys
def frequencySort(s):
    # TODO: Implement me!
    #turn to ascii char
    """temp=[]
    for element in s:
        temp.append(sum(ord(element))
    print(temp)"""
    #sort by descending order on the number of frequency of the characters
    #sort reverse=true, sort by ord value in s
    """
    dec_sort= sorted(s, key= lambda s: sum(ord(char) for char in s), reverse=True)
    #converts list to string with no spaces
    return ''.join(dec_sort)
    """
    """
    #sort by ascii
    dec_sort=sorted(s,key=s.count,reverse=True)
    print(dec_sort)
    #dec_sort=sorted(s,reverse=True)
    print(dec_sort)

  
    #sort by ascii value
    dec_sort = sorted(s, reverse=True)
    print(dec_sort)
    for i in range(len(dec_sort)-1):
        #if frequency is the same
        if dec_sort[i]==dec_sort[i+1]:
            #if ascii value is smaller, swap
            if ord(dec_sort[i])<ord(dec_sort[i+1]):
                #swap
                dec_sort[i],dec_sort[i+1]=dec_sort[i+1],dec_sort[i]
    #return the sorted string """
    
    
    dec_sort= sorted(s, key= lambda s: sum(ord(char) for char in s), reverse=False)
    for i in len(dec_sort):
        if i!=i+1:
            
            
            
    print(dec_sort)
    #return the sorted string """

   
def main():
    #read the input file from stdin
    string = sys.stdin.readline().strip()
    while(string != ''):
        print(frequencySort(string))
        string = sys.stdin.readline().strip()



# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()

