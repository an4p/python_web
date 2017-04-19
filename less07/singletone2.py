# files shared from my missed lesson
class Singletone:
    instance = None

    def __new__(cls, *args, **kwargs):
        if Singletone.instance == None:
            Singletone.instance = object.__new__(cls)
        return Singletone.instance

    def __init__(self, a):
        self.a = a

a1 = Singletone(10)
a2 = Singletone(20)
print(a1.a)
print(a2.a)

print (a1 == a2)
