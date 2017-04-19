class A:
    def __init__(self,a):
        self.a = a
        self.observers = []

    def subscribe(self,observer):
        self.observers.append(observer)

    def change_a(self, new_a):
        for observer in self.observers:
            observer.notify(self.a, new_a)

class Observer:
    def __init__(self):
        pass

    def notify(self, old_value, new_value):
        print("Value was changed from old value {} to new value {}"
              .format(old_value, new_value))

def main():
    a = A(10)
    obs1 = Observer()
    obs2 = Observer()

    a.subscribe(obs1)
    a.subscribe(obs2)

    a.change_a(20)

main()
