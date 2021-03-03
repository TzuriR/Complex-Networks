# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import point as Pnt
import edge as Edg
# import random as rd
import numpy as np
import math


class Network:
    # nodes = [pnt.Point]
    nodes = []  # points array
    # edges = [edg.Edge]
    edges = []  # edges array
    # adjacency_matrix = [] # num_of_nodes X num_of_nodes
    num_of_nodes: int = 0
    num_of_edges: int = 0
    r: float = 0

    # g = nx.Graph()  # in case of a random graph auto generated

    def __init__(self, r: float):
        self.r = r

    '''def random_generator(self, n: int, pr: int):
        if self.model == "ErdosRenyi":
            self.g = nx.generators.random_graphs.erdos_renyi_graph(n, pr)
        elif self.model == "Geometric":
            dim = 2
            p = 2
            pos = {i: (rd.uniform(0, 1), rd.uniform(0, 1)) for i in range(n)}  # problem!!
            self.g = nx.random_geometric_graph(n=n, radius=pr, dim=dim, pos=pos, p=p, seed=None)'''

    def add_vertex(self, v: Pnt.Point) -> int:  # returns number of the vertex assigned to the network
        if v in self.nodes:
            print("Node is already in")
            return -1
        self.nodes.append(v)  # ??
        self.num_of_nodes += 1
        return self.num_of_nodes

    def make_edges(self):
        for i in range(0, len(self.nodes)):
            for j in range(0, len(self.nodes)):
                if i == j:
                    continue
                if self.node_distance(self.nodes[i], self.nodes[j]) < self.r:
                    self.add_edge_by_vtx(self.nodes[i], self.nodes[j])

    def add_edge_by_vtx(self, vtx1: Pnt.Point,
                        vtx2: Pnt.Point) -> int:  # returns number of the edge assigned to the network
        if vtx1 not in self.nodes or vtx2 not in self.nodes:
            print("Need to add these nodes first")
            return -1
        temp_edge = Edg.Edge(vtx1, vtx2, self.num_of_edges)
        self.edges.append(temp_edge)  # ??
        self.num_of_edges += 1
        # x0 = np.ones((m, 1))
        # x_normal = np.hstack((x0, x_normal))
        return self.num_of_edges

    # Utility function: get two node and return the distance between

    def node_distance(self, vtx1: Pnt.Point, vtx2: Pnt.Point):
        x_pos_vtx1, y_pos_vtx1 = vtx1.x_value, vtx1.y_value
        x_pos_vtx2, y_pos_vtx2 = vtx2.x_value, vtx2.y_value
        # The distance between vtx1 and vtx2
        val = (x_pos_vtx1 - x_pos_vtx2) ** 2 + (y_pos_vtx1 - y_pos_vtx2) ** 2
        dist_vtx = math.sqrt(val)
        return dist_vtx

    # Utility function: get index of point, return 1 if the point is at the array and 0 if not

    def is_at_point(self, points_arr, index: int) -> bool:
        for p in points_arr:
            if p.serial_number == index:
                return True
        return False

    # Utility function: get index of edge, return 1 if the edge is at the array and 0 if not
    def is_at_edge_by_serial(self, edges_arr, index: int) -> bool:
        for e in edges_arr:
            if e.serial_number == index:
                return True
        return False

    # Utility function: get indexes of points, return 1 if there is edge between them at the array and 0 if not
    def is_at_edge_by_points(self, edges_arr, index1: int, index2: int) -> bool:
        for e in edges_arr:
            if e.vtx_1.serial_number == index1 and e.vtx_2.serial_number == index2:
                return True
            if e.vtx_1.serial_number == index2 and e.vtx_2.serial_number == index1:
                return True
        return False

    # Build adjacency matrix and return it

    def adjacency_matrix(self):
        adj_mat = [[0 for x in range(self.num_of_nodes)] for y in range(self.num_of_nodes)]
        for i in range(0, self.num_of_nodes):
            for j in range(0, self.num_of_nodes):
                if self.is_at_edge_by_points(self.edges, i, j):
                    adj_mat[i][j] = 1
                    adj_mat[j][i] = 1
        return adj_mat

    # Utility function: print as matrix
    def print_mat(self, mat):
        for i in range(0, len(mat)):
            print(mat[i])

    def print_point_arr(self, point_arr):
        print("[", end="")
        for i in range(0, len(point_arr)):
            if i != len(point_arr) - 1:
                print(point_arr[i].serial_number, end=", ")
            else:
                print(point_arr[i].serial_number, end="")
        print("]")

    def print_edge_arr(self, edge_arr):
        print("[", end="")
        for i in range(0, len(edge_arr)):
            print("(", end="")
            print(edge_arr[i].vtx_1.serial_number, ",", edge_arr[i].vtx_2.serial_number, end="")
            if i != len(edge_arr) - 1:
                print(")", end=", ")
            else:
                print(")", end="")
        print("]")

    def print_network(self):
        print("g.nodes:")
        self.print_point_arr(self.nodes)
        print("g.edges:")
        self.print_edge_arr(self.edges)
        print("Adjacency matrix:")
        self.print_mat(self.adjacency_matrix())
        print("Number of nodes:", self.num_of_nodes)
        print("Number of edges:", self.num_of_edges)

    def draw_network(self):
        g = nx.Graph()
        for p in self.nodes:
            g.add_node(p.serial_number)
        for e in self.edges:
            g.add_edge(e.vtx_1.serial_number, e.vtx_2.serial_number)
        pos_dict = {}
        for p in self.nodes:
            pos_dict[p.serial_number] = (p.x_value, p.y_value)
        fig, ax = plt.subplots()
        nx.draw_networkx(g, ax=ax, pos=pos_dict, with_labels=True)
        ax.set_xticks(np.arange(0, 1, self.r / 2))
        ax.set_yticks(np.arange(0, 1., self.r / 2))
        ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
        # plt.grid(True)
        plt.grid(b=True, which='major', color='red', linestyle='-')
        plt.savefig("geometric_net_drawing.png")
        plt.show()
