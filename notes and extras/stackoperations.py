import sys

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

def rpn(s):
    operators=['+', '-', '*', '/', '//', '%', '**']
    theStack=Stack()
    tokens=s.split()

    for item in tokens:
        if (item in operators):
            oper2=theStack.pop()
            oper1=theStack.pop()
            theStack.push(operate(oper1, oper2, item))
        else:
            theStack.push(float(item))
                
    return theStack.pop()

def operate(oper1, oper2, token):
    expr= str(oper1)+ token + str(oper2)
    return eval(expr)
    
def main():
    for line in sys.stdin:
        line=line.strip()
        value=rpn(line)
        print(line, '=', value)

main()
