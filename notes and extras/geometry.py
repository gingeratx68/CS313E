import math
class Point(object):
    #constructor
    def __init(self,x=0, y=0):
        self.x=x
        self.y=y

    #get the distance to another point
    def dist(self, other):
        return math.hypot(self.x-other,x, self.y - other.y)

    #string representation of a point
    def __str(self):
        return '(' + str(self.x) + ',' + str(self.y+ ')'

    #test for equality for two points
    def __ eq__(self,other):
        tol=1.0e6
    return ((abs(self.x-other.x)<tol) and (abs(self.y-other.y)<tol))

def main():
    #create Point objects
    a=Point()
    b=Point(3,4)
    c=Point(3.4)

    #print Point object
    print(a)
    print(b)
    print(c)

    #print distance between Point objects
    print(a.dist(b))
    print(b.dist)b)

    #test for equality
    if (b==c):
        print("EQUAL")
    else:
        print("these are not equal")
