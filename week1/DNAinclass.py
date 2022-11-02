import sys
def all_substrings(s):
    #produce all the substring
    
    result=[]
    ##define size of window
    wind=len(s)
    #generate all substrings
    while(wind>0):
        index=0
        while (index+wind)<=len(s):
            sub_str=s[index:index+wind]
            #store in result
            result.append(sub_str)
            #increment the index
            index+=1
        # decrease the size of the window
        wind=wind-1
    #return the result
    return result 
def longest_subsequence(s1,s2):
    #take two strings and return list
    
def test_cases():
    #test the function longest_subsequence
    assert longest_subsequence ("a", "a")==["a"]
    assert longest_subsequence ("abcd", "bc")==["bc"]
    assert longest_subsequence ("ginger", "insect")==["ine"]
    assert longest_subsequence ("abcd", "xyz")==[] #empty list

    #test the function all_substrings
    assert all_substrings("a")==["a"]
    assert all_substrings("abc")==["a","b","c","ab","bc", "abc"]

    #other test cases
    #return the result
    return "all test cases oassed"
def main():
    #call test_cases()
    print (test_case())
   
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

