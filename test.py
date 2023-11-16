class Polygon():
    def __init__(self,side):
        self.side = side
    def perimeter(self):
        per = 4*self.side[0]
        return per
class Square(Polygon):
    def __init__(self,side):
        self.side = side
    def area(self):
        are = self.side[0]*self.side[0]
        return are

side = [int(input("Enter the side"))]
o1 = Square(side)
print("Perimeter is ",o1.perimeter())
print("Area is ",o1.area())