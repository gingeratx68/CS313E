#  File: Radix.py

#  Description: sort a list of strings with letters and numbers in a queue by last char all the way to the first char

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628

#  Partner Name:

#  Partner UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/23/22

#  Date Last Modified: 10/24/22

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

  def debug(self):
    return self.queue
# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings

def radix_sort (a):
    val_dict = {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6' : 6,
              '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14,
              'f':15, 'g':16, 'h':17, 'i':18, 'j': 19, 'k': 20, 'l': 21, 'm': 22
              , 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r' : 27, 's': 28, 't': 29,
              'u': 30, 'v': 31, 'w' :32, 'x':33, 'y':34, 'z' :35, '*': 0}
  
    #find the max length which will be total num of passes 
    max_len=0
    for i in range(len(a)):
        if len(a[i])>max_len:
            max_len=len(a[i])
    #print(max_len)
    #padd strings in a with * to make them all the same length
    for i in range(len(a)):
        #print(len(i))
        while len(a[i])<max_len:
            a[i]=a[i]+'*'
            #print(a)

    #create a queue of the length of a
    queue_dict={}
    for i in val_dict.keys():
        queue_dict[i]=Queue()
    #print(queue_dict)

    for i in range(max_len-1, -1, -1):
        a=queue_sort(a, i, val_dict, queue_dict)
        #print("QUEUE %s %s" % (i,a))
    final=[]
    for chars in a:
        new_a=""
        for char in chars:
            if char != "*":
                new_a+=char
        final.append(new_a)
                
                

    return final



def queue_sort(a, idx, val_dict, queue_dict):
    for s in a:
        xx=list(s)[idx]
        #print("%s" % type(xx))
        yy=val_dict[xx]
        
        
        #print(val_dict)
        #look in dict for key, return object, enqueue object
        zz=queue_dict[xx].enqueue(s)
        #returns value at the key
        aa=queue_dict[xx].debug()
        #print(aa)
        
        #deq=queue_dict[xx].dequeue(s)
        #print('%s, %s, %s, %s' % (xx, s, yy,zz))

    #get value at key and sort by value
    abc=sorted(val_dict, key=val_dict.__getitem__)
    #print(abc)
    deq_list=[]
    hasdata=True
    #while(hasdata):
        #hasdata=False
    for key in abc:
        while (queue_dict[key].is_empty() == False):
            deq_list.append(queue_dict[key].dequeue())
                #hasdata=True
    return deq_list


    
    
        
    
    """  
    first_pass=[]
    #sort strings by 
    #sort by last character of string and add to queue
    for i in range(max_len):
        #sorted(a, key=lambda x: x[-1])
        for s in a:
            idx=val_dict[s[len(s)-i-1]]
            print(idx)
            (first_pass).Queue.enqueue(s)
            i+=1
            print(first_pass)
    #use dequeue_all to dequeue all values in queue
    sorted_list=dequeue_all(first_pass)
    return sorted_list
    """

    
    


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    
