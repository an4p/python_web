def f():
    a = 30
    def g():
        nonlocal a
        a=40
    g()
    return a
print(f())