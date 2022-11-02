
def main():

    n = int(input())
    x = list(map(int, input().split()))

    # print n-1 lines
    # each line contains A/B in reduced form
    # format: "1/2"
   
    for i in x[1:]:
        #print(i)
        #print(x[0])
        frac=x[0]/i
        print(str(int(frac))+'/1')
if __name__ == "__main__":
    main()
