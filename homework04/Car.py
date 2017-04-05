class Car:
    def __init__(self, make, petrol_consumption):
        self.make = make
        self.petrol_consumption = petrol_consumption

    def petrol_calculation(self, price = 22.5):
        return self.petrol_consumption * price


ford = Car("ford", 10)

money = ford.petrol_calculation()
print(money)



