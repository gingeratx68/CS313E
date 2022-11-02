"""
def is isPowerOfTwo:
    if n==0:
        return False
    if n==1:
        return True
    if n%2!=0:
        return False
    return n%2==0 and isPowerOfTwo(n/2)
"""
class solution:
    def reverseList(self, head):
        if (not head) or (not head.next):
            return head
        reverse=self.reverseList(head.next)
        #move two places down the list and set next place to null 
        head.next.next=head
        head.next=None
        return reverse

def main():
    head=[1,2,3,4,5]
    print(solution.reverseList(self, head))
    
main()
