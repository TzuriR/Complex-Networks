# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import point_gnc as Pnt
import edge_gnc as Edg
import random as rd
import math


class Network:
    # nodes = [pnt.Point]
    nodes = []  # points array
    # edges = [edg.Edge]
    edges = []  # edges array
    # adjacency_matrix = [] # num_of_nodes X num_of_nodes
    num_of_nodes: int = 0
    num_of_edges: int = 0
    c: float = 0

    # g = nx.Graph()  # in case of a random graph auto generated

    def __init__(self, c: float = 0):
        self.nodes = []
        self.edges = []
        self.num_of_nodes = 0
        self.num_of_edges = 0
        self.c = c

    # Get 2 points and return True if it meet the conditions to connection
    def do_vertices_meet_conditions(self, v_1: Pnt.Point, v_2: Pnt.Point):
        distance_torus_1_2 = self.node_distance(v_1, v_2)
        prob = min((self.c*(v_1.w_value*v_2.w_value)/distance_torus_1_2), 1)
        temp = rd.uniform(0, 1)
        if temp < prob:
            return True
        return False

    def add_vertex(self, v: Pnt.Point) -> int:  # returns number of the vertex assigned to the network
        if v in self.nodes:
            print("Node is already in")
            return -1
        self.nodes.append(v)
        self.num_of_nodes += 1
        return self.num_of_nodes

    def make_edges(self):
        for i in range(0, len(self.nodes)):
            for j in range(0, len(self.nodes)):
                if i == j:
                    continue
                if self.do_vertices_meet_conditions(self.nodes[i], self.nodes[j]):
                    self.add_edge_by_vtx(self.nodes[i], self.nodes[j])

    def add_edge_by_vtx(self, vtx1: Pnt.Point,
                        vtx2: Pnt.Point) -> int:  # returns number of the edge assigned to the network
        if vtx1 not in self.nodes or vtx2 not in self.nodes:
            print("Need to add these nodes first")
            return -1
        temp_edge = Edg.Edge(vtx1, vtx2, self.num_of_edges)
        self.edges.append(temp_edge)
        self.num_of_edges += 1
        # x0 = np.ones((m, 1))
        # x_normal = np.hstack((x0, x_normal))
        return self.num_of_edges

    # Utility function: get two nodes and return the distance between them in the torus
    def node_distance(self, vtx1: Pnt.Point, vtx2: Pnt.Point):
        x_pos_vtx1, y_pos_vtx1 = vtx1.x_value, vtx1.y_value
        x_pos_vtx2, y_pos_vtx2 = vtx2.x_value, vtx2.y_value
        x_abs = abs(x_pos_vtx2 - x_pos_vtx1)
        y_abs = abs(y_pos_vtx2 - y_pos_vtx1)
        delta_x = min(x_abs, 1 - x_abs)
        delta_y = min(y_abs, 1 - y_abs)
        # The distance between vtx1 and vtx2
        val = delta_x ** 2 + delta_y ** 2
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
