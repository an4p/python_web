class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.__dict__["x"] = x1
        self.y = y1
def main():
    p = Point(3,4)
    print(p.x)
    print(p.__dict__["x"])
    print(p.y)
    print(p.__dict__)

    p1 = Point(5,6)

    p2 = Point.__new__(Point)
    Point.__init__(p2, 3, 4)
    print(p2.x)


main()