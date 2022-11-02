def permute(a, idx):
    hi= len(a)
    #if reached end of elements
    if (idx==hi):
        #print what is in a
        print(a)
    else:
        #swapping takes place
        for i in range(idx, hi):
            a[idx], a[i]= a[i], a[idx]
            #permute rest 
            permute(a, idx+1)
            #switch back 
            a[idx], a[i]= a[i], a[idx]
def main():
    a=['A', 'B', 'C', 'D']
    permute(a,0)
main()

            
