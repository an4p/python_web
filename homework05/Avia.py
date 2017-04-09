class Employee:
    def __init__(self, title, name, salary):
        self.title = title
        self.name = name
        self.salary = salary

class Plane:
    def __init__(self, model, fuel_consumption, fuel_price, sits_count):
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price
        self.sits_count = sits_count
        self.personal = []

    def add_personal(self, employee):
        self.personal.append(employee)


class Flight:
    def __init__(self, name, distance, sit_price, plane):
        self.name = name
        self.distance = distance
        self.sit_price = sit_price
        self.plane = plane

    def income(self):
        sum = 0
        total_salary = 0
        for employee in self.plane.personal:
            total_salary += int(employee.salary)


        fuel_charge = self.distance/100 * self.plane.fuel_consumption * self.plane.fuel_price

        ticket_income = self.plane.sits_count * self.sit_price


        sum = ticket_income - total_salary - fuel_charge

        return sum



def main():
    pilot1 = Employee("First pilot", "Ivanov Ivan", "80000")
    pilot2 = Employee("Second pilot", "Petrov Petr", "70000")
    stewardess1 = Employee("Sr stewardess", "Olgova Olga", "30000")
    stewardess2 = Employee("Stewardess", "Tatianova Tatiana", "25000")
    stewardess3 = Employee("Stewardess", "Alinova Alina", "20000")

    plane = Plane("Boing-747", 100, 50, 526)
    plane.add_personal(pilot1)
    plane.add_personal(pilot2)
    plane.add_personal(stewardess1)
    plane.add_personal(stewardess2)
    plane.add_personal(stewardess3)

    flight = Flight("Kyiv-Shanghai", 7460, 10000, plane)

    income = flight.income()

    print(income)


main()