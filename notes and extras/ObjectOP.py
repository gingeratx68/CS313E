class Shape:
    description="Simple quadrilaterals"
    author="Ginger Hudson"

    def __init__(self, length, height):
        #when creating rectangle object assign it l and h
        self.x=length
        self.y=height 
        
    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2*self.x +2*self.y
def main():
    myRectangle=Shape(10,20)
    print(myRectangle.description)
    print(myRectangle.author)
    print(myRectangle.x)
    print(myRectangle.y)
    print(myRectangle.area())
    print(myRectangle.perimeter())
    
    myRectangle2=Shape(50,25)
    print(myRectangle.description)
    print(myRectangle.author)
    print(myRectangle2.x)
    print(myRectangle2.y)
    print(myRectangle2.area())
    print(myRectangle2.perimeter())
main()
    
