#!/usr/bin/env python

import time


class Car(object):
    fuel = 23
    max_speed = 180
    speed = 0

    def __init__(self):
        pass

    def refuel(self):
        self.fuel = 23

        print("......Refuelling......")
        time.sleep(1)
        print("Refueled!")

    def getFuel(self):
        return self.fuel

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def drive(self):
        print("......Driving now......")
        time.sleep(1)
        while self.speed < self.max_speed:
            self.speed += 10
            time.sleep(0.5)
            print(str(self.speed) + " mph")
        print("Approached max speed!")


if __name__ == "__main__":
    Tesla = Car()
    Tesla.drive()
