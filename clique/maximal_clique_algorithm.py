import point as pnt
import geometric_network as ge_net
from sympy import symbols, Eq, solve

# -----------------------------------------------------------------------------------------------------
# Definition of class represents line

class Line:
    a: int = 0
    b: int = 0

    def __init__(self, vtx1: pnt, vtx2: pnt):
        self.a = (vtx1.y_value - vtx2.y_value) / (vtx1.x_value - vtx2.x_value)
        self.b = vtx1.y_value - (self.a * vtx1.x_value)

    def calculate_relation_to_line(self, vtx: pnt):
        val = vtx.y_value - (self.a * vtx.x_value) - self.b
        return val

    def print_line(self):
        print("y =", self.a, "x +", self.b)

# -----------------------------------------------------------------------------------------------------
# Definition of class represents circle

class Circle:
    r: int = 0
    center_x: float = 0.0
    center_y: float = 0.0

    def __init__(self, rad: int, p: pnt):
        self.r = rad
        self.center_x = p.x_value
        self.center_y = p.y_value

    def calculate_relation_to_circle(self, vtx: pnt):
        val = (vtx.x_value - self.center_x) ** 2 + (vtx.y_value - self.center_y) ** 2 - self.r ** 2
        return val

    def print_line(self):
        print("(x -", self.center_x, ")² + (y -", self.center_y, ")² =", self.r**2)

# -----------------------------------------------------------------------------------------------------
# Function that generates random geometric model

def generate_model(n, r):
    net = ge_net.Network(r)
    for i in range(0, n):
        p = pnt.Point(i)
        net.add_vertex(p)
    net.make_edges()
    net.print_network()
    net.draw_network("main_network")
    return net


# -----------------------------------------------------------------------------------------------------
# Function that searches for two connected nodes with maximal distance

def nodes_with_maximal_distance(net):
    max_dist = 0.0
    max_node_1 = net.nodes[0]
    max_node_2 = net.nodes[0]
    for temp_edge in net.edges:
        temp_dist = net.node_distance(temp_edge.vtx_1, temp_edge.vtx_2)
        if temp_dist >= max_dist:
            max_node_1 = temp_edge.vtx_1
            max_node_2 = temp_edge.vtx_2
            max_dist = temp_dist
    print("max_node_1 :", max_node_1.serial_number, "max_node_2 :", max_node_2.serial_number)
    return max_node_1, max_node_2


# -----------------------------------------------------------------------------------------------------
# Gets two serial num of nodes and returns a group with the nodes which are in the intersection of the circles u and v
# create. The nodes which are in the intersection of the circles u and v create are the nodes that are connected
# to u and v. Therefore the function searches for these nodes and returns group of it

'''def intersection_group_u_v(adj_mat, u, v):
    intersection_group = []
    for i, row in enumerate(adj_mat):
        if i == u or i == v:
            continue
        if row[u] == 1 and row[v] == 1:
            intersection_group.append(i)
    return intersection_group'''


def intersection_group_u_v(net, u, v):
    '''intersection_group = []
    for temp_node in net.nodes:
        if temp_node.serial_number == u.serial_number or temp_node.serial_number == v.serial_number:
            continue
        if net.is_at_edge_by_points(net.edges, temp_node.serial_number, u.serial_number) and \
                net.is_at_edge_by_points(net.edges, temp_node.serial_number, v.serial_number):
            intersection_group.append(temp_node)
    print("intersection_group :")
    net.print_point_arr(intersection_group)
    return intersection_group'''
    d = net.node_distance(u, v)
    circle_u = Circle(d, u)
    circle_v = Circle(d, v)
    intersection_group = []
    for temp_node in net.nodes:
        if temp_node.serial_number == u.serial_number or temp_node.serial_number == v.serial_number:
            continue
        temp_relation_circle_u = circle_u.calculate_relation_to_circle(temp_node)
        temp_relation_circle_v = circle_v.calculate_relation_to_circle(temp_node)
        if temp_relation_circle_u <= 0 and temp_relation_circle_v <= 0:
            if net.is_at_edge_by_points(net.edges, temp_node.serial_number, u.serial_number) and \
                    net.is_at_edge_by_points(net.edges, temp_node.serial_number, v.serial_number):
                intersection_group.append(temp_node)
    print("intersection_group :")
    net.print_point_arr(intersection_group)
    return intersection_group


# -----------------------------------------------------------------------------------------------------
# This function get the intersection group and separate it to cliques by the line between the nodes

def separate_group_to_clique(net, u, v, intersection_group):
    line_u_v = Line(u, v)
    line_u_v.print_line()
    clique_pos = []
    clique_neg = []
    clique_line = []
    for temp_node in intersection_group:
        relation = line_u_v.calculate_relation_to_line(temp_node)
        if relation > 0:
            clique_pos.append(temp_node)
        elif relation < 0:
            clique_neg.append(temp_node)
        else:
            clique_line.append(temp_node)
    print("clique_pos :")
    net.print_point_arr(clique_pos)
    print("clique_neg :")
    net.print_point_arr(clique_neg)
    print("clique_line :")
    net.print_point_arr(clique_line)
    return clique_pos, clique_neg, clique_line


# -----------------------------------------------------------------------------------------------------
# Build complement graph of the intersection graph

def build_complement_graph(net, clique_pos, clique_neg):
    # Initialize the graph
    complement_graph = ge_net.Network(0)
    # Insert nodes to the graph
    for temp_node_pos in clique_pos:
        complement_graph.add_vertex(temp_node_pos)
    for temp_node_neg in clique_neg:
        complement_graph.add_vertex(temp_node_neg)
    # Insert edges to the graph
    for temp_node_pos in clique_pos:
        for temp_node_neg in clique_neg:
            if not net.is_at_edge_by_points(net.edges, temp_node_pos.serial_number, temp_node_neg.serial_number):
                complement_graph.add_edge_by_vtx(temp_node_pos, temp_node_neg)
    complement_graph.print_network()
    # complement_graph.draw_network("complement_network")
    return complement_graph


# -----------------------------------------------------------------------------------------------------
# Find maximal matching in given network, return list of the matching edges

def greedy_maximal_matching(net_graph):
    matching_edges = []
    matching_nodes = []
    for temp_edge in net_graph.edges:
        if not net_graph.is_at_point(matching_nodes, temp_edge.vtx_1.serial_number) and not net_graph.is_at_point(
                matching_nodes, temp_edge.vtx_2.serial_number):
            matching_edges.append(temp_edge)
            matching_nodes.append(temp_edge.vtx_1)
            matching_nodes.append(temp_edge.vtx_2)
    net_graph.print_point_arr(matching_nodes)
    net_graph.print_edge_arr(matching_edges)
    return matching_edges, matching_nodes


# -----------------------------------------------------------------------------------------------------

def build_clique(max_node_1, max_node_2, complement_graph, matching_edges, matching_nodes):
    clique_list = [max_node_1, max_node_2]
    for temp_node_complement in complement_graph.nodes:
        if not complement_graph.is_at_point(matching_nodes, temp_node_complement.serial_number):
            clique_list.append(temp_node_complement)
    complement_graph.print_point_arr(clique_list)
    for temp_edge_matching in matching_edges:
        vtx_1 = temp_edge_matching.vtx_1
        vtx_2 = temp_edge_matching.vtx_2
        flag_1 = 0
        flag_2 = 0
        for temp_node_clique in clique_list:
            if not complement_graph.is_at_edge_by_points(complement_graph.edges, vtx_1.serial_number,
                                                         temp_node_clique.serial_number):
                continue
            else:
                flag_1 = 1
            if not complement_graph.is_at_edge_by_points(complement_graph.edges, vtx_2.serial_number,
                                                         temp_node_clique.serial_number):
                continue
            else:
                flag_2 = 1
        if flag_1 == 0:
            clique_list.append(vtx_1)
        elif flag_2 == 0:
            clique_list.append(vtx_2)
    print("clique list :")
    complement_graph.print_point_arr(clique_list)
    return clique_list


def deterministic_maximal_clique_algorithm(net):
    # Take only the nodes with the maximal length
    max_clique_group = []
    index = 0
    max_index = 0
    for node_1 in net.nodes:
        for node_2 in net.nodes:
            print("***************************************************************************")
            print("index :", index)
            node_1.print_point()
            node_2.print_point()
            if node_1 == node_2:
                continue
            if not net.is_at_edge_by_points(net.edges, node_1.serial_number, node_2.serial_number):
                continue
            intersection_group = intersection_group_u_v(net, node_1, node_2)
            clique_pos, clique_neg, clique_line = separate_group_to_clique(net, node_1, node_2, intersection_group)
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("complement graph :")
            complement_graph = build_complement_graph(net, clique_pos, clique_neg)
            print("matching graph :")
            matching_edges, matching_nodes = greedy_maximal_matching(complement_graph)
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Building the clique :")
            clique_list = build_clique(node_1, node_2, complement_graph, matching_edges, matching_nodes)
            # print("len of maximal clique :", len(clique_list))
            # net.draw_network("clique_network", clique_list)
            print("len(max_clique_group) :", len(max_clique_group), "len(clique_list) :", len(clique_list))
            if len(max_clique_group) < len(clique_list):
                max_clique_group = clique_list
                max_index = index
            index += 1
    print("**************************************************************************")
    print("maximal clique :")
    net.print_point_arr(max_clique_group)
    print("len of maximal clique :", len(max_clique_group), "max index :", max_index)
    net.draw_network("clique_network", max_clique_group)
    return max_clique_group


def check_if_clique(net, clique_list):
    for ele_1 in clique_list:
        for ele_2 in clique_list:
            if ele_1 != ele_2:
                if not net.is_at_edge_by_points(net.edges, ele_1, ele_2):
                    print("There is no clique")



# -----------------------------------------------------------------------------------------------------

def main():
    n = 50
    r = 0.1
    net = generate_model(n, r)
    max_clique_group = deterministic_maximal_clique_algorithm(net)
    '''max_node_1, max_node_2 = nodes_with_maximal_distance(net)
    intersection_group = intersection_group_u_v(net, max_node_1, max_node_2)
    clique_pos, clique_neg, clique_line = separate_group_to_clique(net, max_node_1, max_node_2, intersection_group)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    complement_graph = build_complement_graph(net, clique_pos, clique_neg)
    matching_edges, matching_nodes = greedy_maximal_matching(complement_graph)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    clique_list = build_clique(max_node_1, max_node_2, complement_graph, matching_edges, matching_nodes)
    print("len of maximal clique :", len(clique_list))
    net.draw_network("clique_network", clique_list)'''



if __name__ == '__main__':
    main()
