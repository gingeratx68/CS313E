#memo can be list, array, dict, piece of memory
def fib_memo(n,memo):
    if (n==0) or (n==1):
        return n
    else:
        if (n>=len(memo)):
            f=fib_memo(n-1, memo)+ fib_memo(n-2, memo)
            memo.append(f)
            return f
        else:
            #its in the memo, so use it
            return memo[n]
def fib(n):
    if (n==0) or (n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)
def main():
    #first 50 terms
    memo=[0,1]
    for i in range(50):
        print(i,'', fib_memo(i,memo))
main()
    
