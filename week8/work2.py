import time
import sys 
# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee

#extra function to count number of lines
def TotaL_No_of_Lines(v,k):
    sum_1=v
    x=1
    while v>k**x:
        sum_1+=v//k**x
        x+=1
    return sum_1


def linear_search(n: int, k: int) -> int:
  # use linear search here
  for v in range(1,n+1):
      if TotaL_No_of_Lines(v,k)>=n:
          return v
  return 0 # placeholder

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
  left=1
  right=n
  while (left<=right):
      Middle_term=(left+right)//2
      if TotaL_No_of_Lines(Middle_term,k)>=n and TotaL_No_of_Lines(Middle_term-1,k)<n:
          return Middle_term
      elif TotaL_No_of_Lines(Middle_term,k)>=n:
          right=Middle_term
      else:
          left=Middle_term


  return 0 

def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()
# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
