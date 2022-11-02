# File: CongoLine.py  
# Description: Conduct pair-wise swaps in a linked list

# Student Name: Ginger Hudson
# Student UT EID:  gsh628
# Course Name: CS 313E
# Unique Number: 52530

import sys

# DO NOT EDIT THE LINK CLASS DEFINITION BELOW

class Link(object):

    def __init__(self, name = "UNNAMED", next = None):
        self._name = name # _name is private - don't access or modify
        self.next = next
        
    def __str__(self):
        return self._name

 

 

# Input: the head Link of a linked list

# Output: returns the new head of the linked list after swapping

def swap(head):
    # TODO: fill in this function
    if head==None or head.next==None:
        return head
    head_ret = head.next
    tail = None
    while(head != None and  head.next != None):
        dance1 = head
        dance2 = head.next

        # Assign previous tail if any
        if tail != None:
            tail.next = dance1.next

        # Swap and send tail back around.
        head = dance2.next
        dance2.next = dance1
        tail = dance1
        dance1.next = None

        # Add last one if odd number.
        if tail != None and head != None and head.next == None:
           tail.next = head

    return head_ret

 
# ------- BE CAREFUL EDITING ANTYING BELOW THIS LINE --------

 

# Input: head of linked list
# Output: prints linked list to stdout
def printList(head):
    if (not head):
        print("__END__")
        return
    print(str(head))
    printList(head.next)

 

def main():
    # read input
    input = sys.stdin.readlines()
    #input = []

    # build linked list
    next = None
    for str in reversed(input[1::]): # ignores length
        next = Link(str.strip(), next)
    #print("START")

    #printList(next)
    #print("SWAP")

 
    # conduct swaps and print results
    printList(swap(next))

 

if __name__ == "__main__":

    main()
