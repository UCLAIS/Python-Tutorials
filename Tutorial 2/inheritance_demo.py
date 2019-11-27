#!/usr/bin/env python


class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"

    def display_car(self):
        super().display_car()
        print("Also, this is an electric car.")


if __name__ == "__main__":
    my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
    my_car.display_car()
