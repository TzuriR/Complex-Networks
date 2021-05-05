import random as rd
import numpy as np


class Point:
    w_value: float = 0.0
    x_value: float = 0
    y_value: float = 0
    serial_number: int = -1

    def __init__(self, num: int, w: float = None, x: float = None, y: float = None):
        self.serial_number = num
        # Generate location
        if x is None:
            self.x_value = rd.uniform(0, 1)
        if y is None:
            self.y_value = rd.uniform(0, 1)
        else:
            self.x_value = x
            self.y_value = y
        # Generate weight
        if w is None:
            x_v = rd.uniform(0, 1)
            self.w_value = np.sqrt(1/(1-x_v))
        else:
            self.w_value = w

    def print_point(self):
        print("Point", self.serial_number, ": x =", self.x_value, ",y =", self.y_value, ",w =", self.w_value)
