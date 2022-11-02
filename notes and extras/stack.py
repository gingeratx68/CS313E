class Stack (object):
    def __init__(self):
        self.stack=[]
    #add item to top of the stack
    def push(self, item):
        self.stack.append(item)

    #remvoe and item for the top of the stack
    def pop(self):
        return self.stack.pop()

    #check the item on the top of the stack 
    def peek(self):
        return self.stack[-1]
    
    #helper functions
    #check if stack is empty
    def is_empty(self):
        return (len(self.stack)==0)
    #return the number of elements in the stack
    def size(size):
        return (len(self.stack))
