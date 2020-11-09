import random as rd


class Point:
    x_value = 0
    y_value = 0
    serial_number: int = -1

    def __init__(self, num: int, x: float = None, y: float = None):
        self.serial_number = num
        if x is None:
            self.x_value = rd.uniform(0, 1)
            self.y_value = rd.uniform(0, 1)
        else:
            self.x_value = x
            self.y_value = y

    def print_point(self):
        print("Point", self.serial_number, "x:", self.x_value, "y:", self.y_value)
