# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import Point as pnt
import Edge as edg
import random as rd


class Network:
    model: str = ""  # Geometric/ErdosRenyi
    # nodes = [pnt.Point]??
    nodes = []  # points array
    # edges = [edg.Edge]??
    edges = []  # edges array
    adjacency_matrix = [[]]  # num_of_nodes X num_of_nodes
    num_of_nodes: int = 0
    num_of_edges: int = 0
    g = nx.Graph()  # in case of a random graph auto generated

    def __init__(self, model: str):
        self.model = model

    def random_generator(self, n: int, pr: int):
        if self.model == "ErdosRenyi":
            self.g = nx.generators.random_graphs.erdos_renyi_graph(n, pr)
        elif self.model == "Geometric":
            dim = 2
            p = 2
            pos = {i: (rd.uniform(0, 1), rd.uniform(0, 1)) for i in range(n)}  # problem!!
            self.g = nx.random_geometric_graph(n=n, radius=pr, dim=dim, pos=pos, p=p, seed=None)

    def add_vertex(self, v: pnt.Point) -> int:  # returns number of the vertex assigned to the network
        if v in self.nodes:
            print("Node is already in")
            return -1
        self.nodes.append(v)  # ??
        self.num_of_nodes += 1
        return self.num_of_nodes

    def add_edge(self, vtx1: pnt.Point, vtx2: pnt.Point) -> int:  # returns number of the edge assigned to the network
        if vtx1 not in self.nodes or vtx1 not in self.nodes:
            print("Need to add these nodes first")
            return -1
        temp_edge = edg.Edge(vtx1, vtx2, self.num_of_edges)
        self.edges.append(temp_edge)  # ??
        self.num_of_edges += 1
        # x0 = np.ones((m, 1))
        # x_normal = np.hstack((x0, x_normal))
        return self.num_of_edges

    def build_adjacency_matrix(self):
        self.adjacency_matrix = [[0 for x in range(self.num_of_nodes)] for y in range(self.num_of_nodes)]
        for i in range(0, self.num_of_nodes):
            for j in range(0, self.num_of_nodes):
                # if self.edges
                self.adjacency_matrix[i][j] = 1
        print(self.adjacency_matrix)

    def print_network(self):
        print("Model:", self.model)
        print("g.nodes:", self.nodes)
        print("g.edges:", self.edges)
        print("Adjacency matrix:", self.adjacency_matrix)
        print("Number of nodes:", self.num_of_nodes)
        print("Number of edges:", self.num_of_edges)

    def show_drawing(self):
        if self.model is not "":
            nx.draw(self.g, with_labels=True)
            plt.savefig("simple_path.png")
            plt.show()
        else:
            x = 1  # how to print??
