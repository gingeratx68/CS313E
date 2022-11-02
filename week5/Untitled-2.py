def test():
    for i in range(10):
        print(i)    
#find fifth line
a = test.__code__.co_firstlineno + 4
print(a)
test()
