import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2) \
               + math.sqrt((point1.y - point2.y)**2)

class Circle(Point):
    def __init__(self, x, y, radius):
        Point.__init__(self, x, y)
        self.radius = radius
    def square(self):
        return 3.14 * self.radius**2

def main():
    p1 = Point(10,20)
    p2 = Point(20,40)
    d = distance(p1, p2)
    c1 = Circle(30,40,100)
    c2 = Circle(15,25,80)
    d1 = distance(c1, c2)
    print(d1)



main()