def func():
    def g(x):
        return x+10
    return g

res = func()
print(res)
print(res(50))