import sys
"""notes on this assignment
-cannot rearrange letters
-how efficient you get to answer is most important
-recursive, hashing, double hashing 



"""
# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    #The constant is a prime number and smaller than the array size
    idx=0
    for i in range(len(s)):
        letter = ord(s[i]) - 96
        idx = const - (idx * 26 + letter) % const
    return(idx)       
    
# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    idx = hash_word (s, len(hash_table))
    if hash_table[idx] != "":
        check = False
        while check == False:
            idx += step_size(s, 11)
            if idx == "":
                check = True
                hash_table[idx] = s
    else:
        hash_table[idx] = s
        
    #print(hash_table)p
   
# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    hash1= hash_word(s, len(hash_table))
    if hash_table[hash1]==s:
        return True
    else:
        hash2=step_size(s, 11)
        i=0
        idx=hash1+i*hash2%len(hash_table)
        if hash_table[idx]==s:
            return True
        else:
            while hash_table[idx]!=s:
                i+=1
                if hash_table[idx]=="":
                    return False
            return True
        
                
                
            
# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
#def is_reducible (s, hash_table, hash_memo):

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
#def get_longest_words (string_list):
    
def main():
  # create an empty word_list
    word_list=[]
    word_list=["jiby", "jib", "cat", "meow"]
  # read words from words.txt and append to word_list
    """
    for line in sys.stdin:
        line = line.strip()
        word_list.append(line)
    """
  # find length of word_list
    len_wl=len(word_list)
    
  # determine prime number N that is greater than twice
  # the length of the word_list
    prime_c=(len_wl*2)+1
    while is_prime(prime_c) == False:
        prime_c += 1
        

        
  # create an empty hash_list
  # populate the hash_list with N blank strings
    hash_list=[]
    hash_list= ['' for i in range(prime_c)]
                
  # hash each word in word_list into hash_list
  # for collisions use double hashing
    
    for word in word_list:
        insert_word(word, hash_list)
    
    print(find_word('jibs', hash_list))
    
  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
    
    hash_memo=[]
    hash_memo=['' for i in range()]
  # populate the hash_memo with M blank strings

  # create an empty list reducible_words
    
    
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.

  # find the largest reducible words in reducible_words
    #largest=get_longest_words(
  # print the reducible words in alphabetical order
  # one word per line
    
if __name__ == "__main__":
  main()
