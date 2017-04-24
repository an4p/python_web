class Car:

    def __init__(self):
        self.state = Stop(self)
        self.transmission = "N"

    def start_moving(self):
        self.state.start_moving()

    def stop_moving(self):
        self.state.stop_moving()

    def switch_transmission(self, transmission):
        self.state.switch_transmission(transmission)

class State:
    def start_moving(self):
        print("Cannot start moving")

    def stop_moving(self):
        print("Cannot stop moving")

    def switch_transmission(self, transmission):
        print("Cannot switch transmission")

class Stop(State):
    def __init__(self, car):
        self.car = car

    def start_moving(self):
        self.car.state = Go(self.car)
        print("Starting the movement")


class Go(State):
    def __init__(self, car):
        self.car = car

    def stop_moving(self):
        self.car.state = Stop(self.car)
        print("Stopping the movement")

    def switch_transmission(self, transmission):
        self.car.transmission = transmission
        print("Changing transmission on {}".format(transmission))


def main():
    car = Car()
    car.stop_moving()
    car.switch_transmission("1")
    car.start_moving()
    car.switch_transmission("2")

main()




