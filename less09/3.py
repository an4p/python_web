from threading import Thread, Condition
from queue import Queue
import time

class Violinist(Thread):
    def __init__(self, queue_violins, queue_bow, mutex_violin, mutex_bow, name):
        Thread.__init__(self)
        self.queue_violins = queue_violins
        self.queue_bow = queue_bow
        self.mutex_violin = mutex_violin
        self.mutex_bow = mutex_bow
        self.name = name

    def run(self):
        while True:
            self.mutex_violin.acquire()
            while self.queue_violins.qsize() == 0:
                self.mutex_violin.wait()
            self.queue_violins.get()
            print("Violinist " + self.name + " take the violin")
            self.mutex_violin.release()

            self.mutex_bow.acquire()
            while self.queue_bow.qsize() == 0:
                self.mutex_bow.wait()
            self.queue_bow.get()
            print("Violinist " + self.name + " take the bow")
            self.mutex_bow.release()

            print("Violinist " + self.name + " is playing")
            time.sleep(1)

            self.mutex_violin.acquire()
            self.queue_violins.put("violin")
            print("Violinist " + self.name + " put the violin")
            self.mutex_violin.notify()
            self.mutex_violin.release()

            self.mutex_bow.acquire()
            self.queue_bow.put("bow")
            print("Violinist " + self.name + " put the bow")
            self.mutex_bow.notify()
            self.mutex_bow.release()

def main():
    mutex_violins = Condition()
    mutex_bow = Condition()
    queue_violins = Queue()
    queue_violins.put("violin")
    queue_violins.put("violin")
    queue_bows = Queue()
    queue_bows.put("bow")
    queue_bows.put("bow")

    v1 = Violinist(queue_violins, queue_bows, mutex_violins, mutex_bow, "V1")
    v2 = Violinist(queue_violins, queue_bows, mutex_violins, mutex_bow, "V2")
    v3 = Violinist(queue_violins, queue_bows, mutex_violins, mutex_bow, "V3")
    v4 = Violinist(queue_violins, queue_bows, mutex_violins, mutex_bow, "V4")

    v1.start()
    v2.start()
    v3.start()
    v4.start()




main()





