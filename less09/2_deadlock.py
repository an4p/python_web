from threading import Thread, Condition
import time

class My_thread(Thread):
    def __init__(self, mutex1, mutex2):
        Thread.__init__(self)
        self.mutex1 = mutex1
        self.mutex2 = mutex2

    def run(self):
        self.mutex1.acquire()
        time.sleep(1)
        self.mutex2.acquire()
        self.mutex2.release()
        self.mutex1.release()

def main():
    mutex1 = Condition()
    mutex2 = Condition()
    m1 = My_thread(mutex1, mutex2)
    m2 = My_thread(mutex2, mutex1)
    m1.start()
    m2.start()


main()



