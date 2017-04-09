class A:
    def __init__(self):
        self.f()

    def f(self):
        print("A")

class B(A):
    def __init__(self):
        A.__init__(self)

    def f(self):
         print("B")

def main():
    b = B()

main()