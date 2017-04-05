class Coffee:
    def __init__(self, type, price):
        self.type = type
        self.price = price

class Box:
    def __init__(self, volume, coffee):
        self.volume = volume
        self.coffee = coffee

class Lorry:
    def __init__(self):
        self.boxes = []
    def add_box(self,box):
        self.boxes.append(box)
    def total(self):
        sum = 0
        for box in self.boxes:
            sum += box.volume * box.coffee.price
        return sum

def main():
    coffee_arabica = Coffee("arabica", 200)
    coffee_robusta = Coffee("robusta", 180)
    box1 = Box(40, coffee_arabica)
    box2 = Box(50, coffee_robusta)
    box3 = Box(10, coffee_robusta)
    box4 = Box(30, coffee_arabica)

    lorry = Lorry()
    lorry.add_box(box1)
    lorry.add_box(box2)
    lorry.add_box(box3)
    lorry.add_box(box4)

    print(lorry.total())

main()