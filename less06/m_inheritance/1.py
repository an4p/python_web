class Quadrangle:
    def __init__(self, line1, line2, line3, angle1, angle2):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.angle1 = angle1
        self.angle2 = angle2

class Paralellogram(Quadrangle):
    def __init__(self, line1, line2, angle):
        Quadrangle.__init__(self, line1, line2, line1, angle, 180 - angle)

class Rectangle(Paralellogram):
    def __init__(self, line1, line2):
        Paralellogram.__init__(self, line1, line2, 90)

class Romb(Paralellogram):
    def __init__(self, line, angle):
        Paralellogram.__init__(self, line, line, angle)

class Square(Rectangle, Romb):
    def __init__(self, line):
        Rectangle.__init__(self, line, line)
        Romb.__init__(self, line, 90)

