class Square:
    def __init__(self,side):
        self.side = side

    def perimeter(self):
        return self.side *4

    def __add__(squareOne, squareTwo):
        print(squareOne.side)
        return(4*squareOne.side + 4*squareTwo.side)
squareone = Square(5)
squaretwo = Square(10)
per = squareone.perimeter()
print(squareone + squaretwo)
print(squaretwo.side + squareone.side)
