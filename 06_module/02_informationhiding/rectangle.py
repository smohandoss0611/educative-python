class Rectangle:
    def __init__(self,length = None,breadth = None):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__breadth * self.__breadth

    def perimeter(self):
        return 2 * (self.__breadth + self.__length)
    
rectangleobj = Rectangle(10,20)
a  = rectangleobj.area()
print("Area",a)
p = rectangleobj.perimeter()
print("Perimeter",p)
