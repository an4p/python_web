class Square:
    def __init__(self, x):
        self.x = x

    def find_square(self):
        return self.x ** 2

s = Square(5)
print(s.x)
square = s.find_square()
print(square)
