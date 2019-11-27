#!/usr/bin/env python

import math


class Point(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):
    radius = 0

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return "A circle with a radius of " + str(self.radius) + " centimeters"

    def __str__(self):
        return repr(self)


if __name__ == "__main__":
    circle = Circle(5)
    print(circle.__repr__())
    print(
        "The area of the circle is "
        + str(round(circle.area(), 2))
        + " centimeters squared"
    )
