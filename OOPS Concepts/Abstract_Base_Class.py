from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0
class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

square = Square(3)
rectangle = Rectangle(2,3)
def Area(Shape):
    print("Area is ",Shape.area())

Area(square)
Area(rectangle)
