import point as pnt
import geometric_network as ge_net
import numpy as np
import point_gnc
import gnc_geometric_network


# -----------------------------------------------------------------------------------------------------
# Function that generates random geometric model

def generate_model_gnr(n, r):
    net = ge_net.Network(r)
    for i in range(0, n):
        p = pnt.Point(i)
        net.add_vertex(p)
    net.make_edges()
    # net.print_network()
    # net.draw_network("main_network")
    return net


def generate_model_gnc(n, c):
    net = gnc_geometric_network.Network(c)
    for i in range(0, n):
        p = point_gnc.Point(i)
        net.add_vertex(p)
    net.make_edges()
    # net.print_network()
    # net.draw_network("main_network")
    return net


# -----------------------------------------------------------------------------------------------------
# Algorithm 5

def separate_to_sets_with_eigen_vector(net):
    n = len(net.nodes)
    set_a = []
    set_b = []
    # Calculate the eigen vectors and get the last one with the minimal eigen value
    eigen_values, eigen_vectors = np.linalg.eig(net.adjacency_matrix())
    # print("eigen_values :", eigen_values)
    # print("eigen_vectors :", eigen_vectors)
    v_n = eigen_vectors[n - 1]
    # print("v_n :", v_n)
    # Run over the elements in v_n, check its sign and insert to the relevant set
    for i in range(n):
        if v_n[i] > 0:
            set_a.append(net.nodes[i])
        else:
            set_b.append(net.nodes[i])
    # print("a :")
    # net.print_point_arr(set_a)
    # print("b :")
    # net.print_point_arr(set_b)
    return set_a, set_b


# -----------------------------------------------------------------------------------------------------
# Get network and sets of cut and calculate the length of the cut

def cal_len_of_cut(net, set_a, set_b):
    len_of_cut = 0
    for temp_node_a in set_a:
        for temp_node_b in set_b:
            if net.is_at_edge_by_points(net.edges, temp_node_a.serial_number, temp_node_b.serial_number):
                len_of_cut += 1
    return len_of_cut


# -----------------------------------------------------------------------------------------------------

def main():
    # For G(n,r)
    n = 100
    r = 0.8
    net = generate_model_gnr(n, r)
    '''# For G(n,c)
    n = 100
    c = 0.5
    net = generate_model_gnc(n, c)'''
    # net.print_edge_arr(net.edges)
    set_a, set_b = separate_to_sets_with_eigen_vector(net)
    len_of_cut = cal_len_of_cut(net, set_a, set_b)
    print("len of cut :", len_of_cut)
    print("len of a :", len(set_a))
    print("len of b :", len(set_b))
    print("len of a+b :", len(set_a) + len(set_b))
    # For G(n,r) : need to divide len of edges in 2
    print("len of edges :", len(net.edges) / 2)
    print("len of cut / num of edges :", 2 * len_of_cut / len(net.edges))
    '''# For G(n,c) : not need to divide len of edges in 2
    print("len of edges :", len(net.edges))
    print("len of cut / num of edges :", len_of_cut / len(net.edges))'''
    net.draw_network("maximal_cut_by_eigenvalues", nodes_list=set_a)


if __name__ == '__main__':
    main()
