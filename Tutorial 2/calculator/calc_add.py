#!/usr/bin/env python

from calc_operator import Operator


class Add(Operator):
    def __init__(self, x, y):
        super().__init__(x, y)

    def eval(self):
        return self.x + self.y
