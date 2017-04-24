from threading import Thread, Condition
from queue import Queue

class Producer(Thread):
    def __init__(self, queue, mutex, name):
        Thread.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire()
            while (self.queue.qsize() >= 5):
                self.mutex.wait()
            self.queue.put('element')
            print("The thread " + self.name + " put the element")
            self.mutex.notify()
            self.mutex.release()

class Consumer(Thread):
    def __init__(self, queue, mutex, name):
        Thread.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire()
            while (self.queue.qsize()== 0):
                self.mutex.wait()
            self.queue.get()
            print("The thread " + self.name + " get the element")
            self.mutex.notify()
            self.mutex.release()

def main():
    queue = Queue()
    mutex = Condition()
    p1 = Producer(queue, mutex, "P1")
    p2 = Producer(queue, mutex, "P2")
    p3 = Producer(queue, mutex, "P3")
    p4 = Producer(queue, mutex, "P4")

    c1 = Consumer(queue, mutex, "C1")
    c2 = Consumer(queue, mutex, "C2")

    p1.start()
    p2.start()
    p3.start()
    p4.start()



    c1.start()
    c2.start()

    p1.join()






main()



