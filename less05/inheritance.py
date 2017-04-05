import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2) \
               + math.sqrt((self.y - other.y)**2)

class Circle(Point):
    def __init__(self, x, y, radius):
        Point.__init__(self, x, y)
        self.radius = radius
    def square(self):
        return 3.14 * self.radius**2
def main():
    circle = Circle(10,20,100)
    print(circle.radius, circle.x, circle.y)
    print(circle.__dict__)
    print(circle.square())
    circle2 = Circle(5,6,80)
    print(circle2.distance(circle))

main()

