# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import point as Pnt
import edge as Edg


# import random as rd


class Network:
    # nodes = [pnt.Point]??
    nodes = []  # points array
    # edges = [edg.Edge]??
    edges = []  # edges array
    # adjacency_matrix = [] # num_of_nodes X num_of_nodes
    num_of_nodes: int = 0
    num_of_edges: int = 0

    # g = nx.Graph()  # in case of a random graph auto generated

    # def __init__(self, model: str):
    #    self.model = model

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

    def add_edge_by_edg(self, edge: Edg.Edge) -> int:  # returns number of the edge assigned to the network
        self.edges.append(edge)
        self.num_of_edges += 1
        # x0 = np.ones((m, 1))
        # x_normal = np.hstack((x0, x_normal))
        return self.num_of_edges

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

    # Utility function: get indexes of points, return 1 if there is edge between them at the array and 0 if not
    def find_edge_between_vertices(self, ver1: Pnt.Point, ver2: Pnt.Point):
        for e in self.edges:
            if e.vtx_1.serial_number == ver1.serial_number and e.vtx_2.serial_number == ver2.serial_number:
                return e
            if e.vtx_1.serial_number == ver2.serial_number and e.vtx_2.serial_number == ver1.serial_number:
                return e
        return None

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
        '''print("Adjacency matrix:")
        self.print_mat(self.adjacency_matrix())'''
        print("Number of nodes:", self.num_of_nodes)
        print("Number of edges:", self.num_of_edges)

    def draw_network(self, title):
        """if self.model is not "":
            nx.draw(self.g, with_labels=True)
            plt.savefig("simple_path.png")
            plt.show()"""
        g = nx.Graph()
        for p in self.nodes:
            g.add_node(p.serial_number)
        for e in self.edges:
            g.add_edge(e.vtx_1.serial_number, e.vtx_2.serial_number)
        nx.draw(g, with_labels=True)
        # plt.savefig("erdos_renyi_net_drawing.png")
        plt.savefig("{}_drawing.png".format(title))
        plt.show()
