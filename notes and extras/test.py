def func ( n ):       

    if (n == 0) or (n == 1):            

      return n        

    else:            

      return 2 * func (n - 1) + func (n - 2)

print (func (5))
  
