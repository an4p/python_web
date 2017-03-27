def map(f, lis):
    # new_lis = []
    # for elem in lis:
    #     new_lis.append(f(elem))
    #
    # return new_lis
    return [f(elem) for elem in lis]

def func1(x):
    return x+2

def func2(x):
    return x+3

def reduce(g, init, lis):
    sum=init
    for i in lis:
        sum = g(sum,i)
    return sum

def plus(a,b):
    return a+b

l=[10,20,30]
# print(map(func, l))
#print(map(func1, map(func2,l)))
res=reduce(plus,0,map(func1,l))
print(res)