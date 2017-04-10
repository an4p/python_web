class A:
    def __init__(self, a):
        self.a = a

class B:
    def __init__(self, b):
        self.b = b

class C(A, B):
    def __init__(self, a, b):
        A.__init__(self,a)
        B.__init__(self,b)

def main():
    c = C(10,20)
    print(c.a, c.b)

main()

