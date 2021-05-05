import point


class Edge:
    vtx_1: point  # a vertex
    vtx_2: point  # a vertex
    serial_number: int = -1

    def __init__(self, vtx1: point, vtx2: point, num: int):
        if vtx1 == vtx2:
            print("edges' points are the same one")
            return
        self.vtx_1 = vtx1
        self.vtx_2 = vtx2
        self.serial_number = num

    def print_edge(self):
        print("Edge", self.serial_number, "(", self.vtx_1.serial_number, ",", self.vtx_2.serial_number, ")")
