# files shared from my missed lesson
class A:
    def __init__(self, a):
        self.a = a

# class B(A):
#     def __init__(self,a, b):
#         A.__init__(self, a)
#         self.b = b

class C:
    def __init__(self, c):
        self.c = c

class B(A, C):
    def __init__(self, a, b, c):
        super(B, self).__init__(a)
        super(A, self).__init__(c)
        self.b = b

pb = B(10, 20, 30)
print (pb.c)
