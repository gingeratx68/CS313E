#a set of things
#b basket
#idx index of where in set a
def sub_sets(a, b, idx):
    #size of a
    hi=len(a)
    #if at end of hi
    if (idx==hi):
        print(b)
        return
    else:
        #make copy of basket
        copy=b[:]
        b.append(a[idx])
        #go to next element
        sub_sets(a,b,idx+1)
        sub_sets(a,copy,idx+1)


def main():
    a=['A','B', 'C']
    b=[]
    #start at beginning index
    sub_sets(a,b,0)
main()
    
        
    
