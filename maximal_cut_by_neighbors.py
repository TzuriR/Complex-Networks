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
# Algorithm 1 : run over the nodes and insert into the sets with probability 0.5

def separate_to_sets_with_equal_probability(net, set_a, set_b):
    for temp_node in net.nodes:
        res = np.random.binomial(1, 0.5)
        if res == 1:
            set_a.append(temp_node)
        else:  # if res == 0:
            set_b.append(temp_node)
    # print("after separate :")
    # print("set_a :")
    # net.print_point_arr(set_a)
    # print("set_b :")
    # net.print_point_arr(set_b)
    return set_a, set_b


# -----------------------------------------------------------------------------------------------------
# Algorithm 3 : Run over each node and check if it has more neighbors in his set - exchange to the other set

def update_sets_by_neighbors(net, set_a, set_b):
    while True:
        flag = 0
        for temp_node_a in set_a:
            counter_a, counter_b = count_num_neighbors_for_each_set(net, set_a, temp_node_a)
            # print("temp_node_a :",temp_node_a.serial_number, "counter_a :", counter_a, "counter_b :", counter_b)
            if counter_b < counter_a:
                flag = 1
                set_b.append(temp_node_a)
                set_a.remove(temp_node_a)
        for temp_node_b in set_b:
            counter_a, counter_b = count_num_neighbors_for_each_set(net, set_a, temp_node_b)
            # print("temp_node_b :", temp_node_b.serial_number, "counter_a :", counter_a, "counter_b :", counter_b)
            if counter_a < counter_b:
                flag = 1
                set_a.append(temp_node_b)
                set_b.remove(temp_node_b)
        if flag == 0:
            break
    # print("after update :")
    # print("set_a :")
    # net.print_point_arr(set_a)
    # print("set_b :")
    # net.print_point_arr(set_b)
    return set_a, set_b


# -----------------------------------------------------------------------------------------------------

def count_num_neighbors_for_each_set(net, set_a, temp_node_set):
    counter_a = 0
    counter_b = 0
    for temp_node_net in net.nodes:
        if net.is_at_edge_by_points(net.edges, temp_node_net.serial_number, temp_node_set.serial_number):
            if temp_node_net in set_a:
                counter_a += 1
            else:  # if temp_node_net in set_b:
                counter_b += 1
    return counter_a, counter_b


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
    n = 10
    r = 0.6
    net = generate_model_gnr(n, r)
    '''# For G(n,c)
    n = 10
    c = 0.1
    net = generate_model_gnc(n, c)'''
    # net.print_edge_arr(net.edges)
    set_a = []
    set_b = []
    set_a, set_b = separate_to_sets_with_equal_probability(net, set_a, set_b)
    len_of_cut = cal_len_of_cut(net, set_a, set_b)
    # print("len of cut after separate:", len_of_cut)
    set_a, set_b = update_sets_by_neighbors(net, set_a, set_b)
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
    net.draw_network("maximal_cut_by_neighbors", nodes_list=set_a)


if __name__ == '__main__':
    main()
