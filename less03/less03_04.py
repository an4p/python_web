# s = lambda x,y:x+3*y
# print(s(10,30))


def map(f,lis):
    return [f(elem) for elem in lis]
# def g(x):
#     return x+3
# new_lis=map(g,[10,20,30])

new_lis=map(lambda x:x+3, [10,20,30])




