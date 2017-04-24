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
    a1 = Sum(1, 10000000)
    time1_start = datetime.datetime.now()
    a1.start()
    a1.join()
    total = a1.result
    time1_end = datetime.datetime.now()
    time1 = time1_end - time1_start
    print("One thread:" + str(time1))
    print(total)

    time2_start = datetime.datetime.now()
    b1 = Sum(1, 5000000)
    b2 = Sum(5000000, 10000001)
    b1.start()
    b2.start()
    b1.join()
    b2.join()
    total = b1.result + b2.result
    time2_end = datetime.datetime.now()
    time2 = time2_end - time2_start
    print("Two threads: " + str(time2))
    print(total)

    time3_start = datetime.datetime.now()
    c1 = Sum(1, 10000000//3)
    c2 = Sum(10000000//3, 2*10000000//3)
    c3 = Sum(2*10000000//3, 10000001)
    c1.start()
    c2.start()
    c3.start()
    c1.join()
    c2.join()
    c3.join()
    total = c1.result + c2.result + c3.result
    time3_end = datetime.datetime.now()
    time3 = time3_end - time3_start
    print("Three threads: " + str(time3))
    print(total)

    time4_start = datetime.datetime.now()
    c1 = Sum(1, 10000000 // 4)
    c2 = Sum(10000000 // 4, 2 * 10000000 // 4)
    c3 = Sum(2 * 10000000 // 4, 3 * 10000000 // 4)
    c4 = Sum(3 * 10000000 // 4, 10000001)
    c1.start()
    c2.start()
    c3.start()
    c4.start()
    c1.join()
    c2.join()
    c3.join()
    c4.join()
    total = c1.result + c2.result + c3.result + c4.result
    time4_end = datetime.datetime.now()
    time4 = time4_end - time4_start
    print("Four threads: " + str(time4))
    print(total)


main()