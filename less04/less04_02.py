class Point:
    def f(self):
        self.x = 500


def main():
    p = Point()

    p.x = 100
    print(p.x)
    print(p.__dict__)
    p1 = Point()
    p1.f()
    print(p1.x)
    Point.f(p1)

main()