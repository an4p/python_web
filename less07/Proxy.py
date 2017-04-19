# files shared from my missed lesson
class Operation:
    def operation(self, a, b):
        return a + b

class proxy_operation:
    def __init__(self):
        self.operation = Operation()
        self.cache = []

    def operation(self, a, b):
        for tup in self.cache:
            if tup[0] == a and tup[1] == b:
                return tup[2]
        res = self.operation.operation(a,b)
        self.cache.append((a,b,res))
        return res

