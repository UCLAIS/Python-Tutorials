#!/usr/bin/env python


class Point3D(object):
    
    x = None
    y = None
    z = None
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print_point_info(self):
        print("(%d, %d, %d)" % (self.x, self.y, self.z))


if __name__ == "__main__":
    my_point = Point3D(1, 2, 3)
    my_point.print_point_info()
