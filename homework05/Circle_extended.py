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

    def square_circle(self):
        return 3.14 * self.radius**2

class Sector(Circle):
    def __init__(self, x, y, radius, angle):
        Circle.__init__(self, x, y, radius)
        self.angle = angle

    def square_sector(self):
        return Circle.square_circle(self) * self.angle / 360

def main():
    p1 = Point(10,20)
    p2 = Point(5,5)
    # print(p2.x, p2.y)
    dist = p1.distance(p2)
    #print(dist)
    c1 = Circle(10, 20, 20)
    # print(c1.x, c1.y, c1.radius)
    sq_circle = c1.square_circle()
    print(sq_circle)

    s1 = Sector(10,20, 20, 180)
    sq_sector = s1.square_sector()
    print(sq_sector)


main()