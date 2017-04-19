import datetime
from threading import Thread
class Sum(Thread):
    def __init__(self, begin, end):
        Thread.__init__(self)
        self.begin = begin
        self.end = end
        self.result = 0

    def run(self):
        for i in range(self.begin,self.end):
            self.result += i

def main():
    s1 = Sum(1,5000000)
    s2 = Sum(5000000, 10000001)
    b = datetime.datetime.now()
    s1.start()
    s2.start()
    s1.join()
    s2.join()
    total = s1.result + s2.result
    e = datetime.datetime.now()
    print(e-b)
    print(total)



main()


