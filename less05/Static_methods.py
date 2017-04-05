class A:
    field = 10
    def __init__(self, a):
        self.a = a

    def f(self):
        return self.a

    @staticmethod
    def g():
        return A.field
