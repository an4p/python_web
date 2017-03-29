def myfunc():
    print("1")
    yield 11
    print("2")
    yield 22

f=myfunc()
res = next(f)
print(res)

res1 = next(f)
print(res1)

next(f)