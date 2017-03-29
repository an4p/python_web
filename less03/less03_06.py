def myrange(begin,end):
    init = begin
    while(init<end):
        yield init
        init +=1

for i in myrange(0,20):
    print (i)