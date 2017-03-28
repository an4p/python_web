a = 10

def func(b):
    global a
    a=30
    return a+b

print(func(10))
print(a)