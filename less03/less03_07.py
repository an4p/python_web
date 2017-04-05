def g():
    print("1")
    k=yield 3
    print(k)
    l=yield 4
    print(l)

f=g()
k = next(f)
print(k)
k1=f.send(10)
print(k1)