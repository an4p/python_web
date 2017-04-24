from multiprocessing import Process, Queue

def sum(begin, end, queue):
    result = 0
    for i in range(begin, end):
        result += i
    queue.put(result)

def main():
    queue1 = Queue()
    queue2 = Queue()

    p1 = Process(target=sum, args=(0,50000000, queue1))
    p2 = Process(target=sum, args=(50000000, 100000001, queue2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    total = queue1.get() + queue2.get()
    print(total)

if __name__ == "__main__":
    main()
