import maximal_cut_gnr
import point as pnt
import geometric_network as ge_net
import numpy as np
import point_gnc
import gnc_geometric_network
# import maximal_cut_gnr


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
    print("len of a :", len(set_a))
    print("len of b :", len(set_b))
    print("sum of a+b :", len(set_a) + len(set_b))
    len_of_cut = cal_len_of_cut(net, set_a, set_b)
    print("len of cut :", len_of_cut)
    # For G(n,r) : need to divide len of edges in 2
    print("len of edges :", len(net.edges) / 2)
    print("len of cut / num of edges :", 2 * len_of_cut / len(net.edges))
    '''# For G(n,c) : not need to divide len of edges in 2
    print("len of edges :", len(net.edges))
    print("len of cut / num of edges :", len_of_cut / len(net.edges))'''
    return set_a, set_b, len_of_cut


# -----------------------------------------------------------------------------------------------------
# Bfs algorithm :

def maximal_cut_bfs_algorithm(net, set_a, set_b):
    # Initialize q and marked
    q = []
    marked = [0]*len(net.nodes)
    # While there is unmarked node
    while 0 in marked:
        # Heuristic start node
        # start_index = random.randint(0, len(net.nodes))
        start_index = marked.index(0)
        set_a.append(net.nodes[start_index])
        marked[start_index] = 1
        q.append(net.nodes[start_index])
        # While q is not empty
        while len(q) != 0:
            cur = q.pop(0)
            for temp_node in net.nodes:
                if not net.is_at_edge_by_points(net.edges, cur.serial_number, temp_node.serial_number):
                    continue
                # Run all over cur neighbors - if it is not marked - insert to the opposite group of cur
                if marked[temp_node.serial_number] == 0:
                    q.append(temp_node)
                    marked[temp_node.serial_number] = 1
                    if cur in set_a:
                        set_b.append(temp_node)
                    if cur in set_b:
                        set_a.append(temp_node)
    # print("set_a :")
    # net.print_point_arr(set_a)
    # print("set_b :")
    # net.print_point_arr(set_b)
    print("len of a :", len(set_a))
    print("len of b :", len(set_b))
    print("sum of a+b :", len(set_a) + len(set_b))
    len_of_cut = cal_len_of_cut(net, set_a, set_b)
    print("len of cut :", len_of_cut)
    '''# For G(n,r) : need to divide len of edges in 2
    print("len of edges :", len(net.edges) / 2)
    print("len of cut / num of edges :", 2 * len_of_cut / len(net.edges))'''
    # For G(n,c) : not need to divide len of edges in 2
    print("len of edges :", len(net.edges))
    print("len of cut / num of edges :", len_of_cut / len(net.edges))
    return set_a, set_b, len_of_cut


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
def max_cut_neighbors_gnr(n, r, flag):
    net = generate_model_gnr(n, r)
    set_a = []
    set_b = []

    # ***********************************************************************************
    # Heuristic starting points for algorithm 3

    # Call algorithm 1
    if flag == 1:
        set_a, set_b, len_of_cut = separate_to_sets_with_equal_probability(net, set_a, set_b)

    # Call maximal_cut_bfs algorithm
    if flag == 2:
        set_a, set_b, len_of_cut = maximal_cut_bfs_algorithm(net, set_a, set_b)

    # Call maximal_cut_gnr algorithm
    if flag == 3:
        set_a, set_b, len_of_cut = maximal_cut_gnr.maximal_cut_gnr_random_centers(net, set_a, set_b)


    # ***********************************************************************************

    # Call algorithm 3
    set_a, set_b = update_sets_by_neighbors(net, set_a, set_b)
    len_of_cut = cal_len_of_cut(net, set_a, set_b)
    # For G(n,r) : need to divide len of edges in 2
    # net.draw_network("maximal_cut_by_neighbors", nodes_list=set_a)
    return len(net.edges), len_of_cut, 2*len_of_cut / len(net.edges)


# -----------------------------------------------------------------------------------------------------
def max_cut_neighbors_gnc(n, c, flag):
    net = generate_model_gnc(n, c)
    # net.print_edge_arr(net.edges)
    set_a = []
    set_b = []

    # ***********************************************************************************
    # Heuristic starting points for algorithm 3

    # Call algorithm 1
    if flag == 1:
        set_a, set_b, len_of_cut = separate_to_sets_with_equal_probability(net, set_a, set_b)

    # Call maximal_cut_bfs algorithm
    if flag == 2:
        set_a, set_b, len_of_cut = maximal_cut_bfs_algorithm(net, set_a, set_b)

    # ***********************************************************************************

    # Call algorithm 3
    set_a, set_b = update_sets_by_neighbors(net, set_a, set_b)
    len_of_cut = cal_len_of_cut(net, set_a, set_b)
    # For G(n,c) : not need to divide len of edges in 2
    return len(net.edges), len_of_cut, len_of_cut / len(net.edges)

# -----------------------------------------------------------------------------------------------------

def main():
    """# For G(n,r)
    n = 100
    r = 0.8
    net = generate_model_gnr(n, r)"""
    # For G(n,c)
    n = 100
    c = 0.5
    net = generate_model_gnc(n, c)
    # net.print_edge_arr(net.edges)
    set_a = []
    set_b = []

    # ***********************************************************************************
    # Heuristic starting points for algorithm 3

    # Call algorithm 1
    # print("********************************************")
    # print("algorithm 1 :")
    # set_a, set_b, len_of_cut = separate_to_sets_with_equal_probability(net, set_a, set_b)

    # Call maximal_cut_gnr algorithm
    # print("********************************************")
    # print("maximal_cut_gnr algorithm :")
    # set_a, set_b, len_of_cut = maximal_cut_gnr.maximal_cut_gnr_random_centers(net, set_a, set_b)

    # Call maximal_cut_bfs algorithm
    print("********************************************")
    print("maximal_cut_bfs algorithm :")
    set_a, set_b, len_of_cut = maximal_cut_bfs_algorithm(net, set_a, set_b)
    # ***********************************************************************************

    # Call algorithm 3
    print("********************************************")
    print("algorithm 3 :")
    set_a, set_b = update_sets_by_neighbors(net, set_a, set_b)
    len_of_cut = cal_len_of_cut(net, set_a, set_b)
    print("len of a :", len(set_a))
    print("len of b :", len(set_b))
    print("len of a+b :", len(set_a) + len(set_b))
    print("len of cut :", len_of_cut)
    '''# For G(n,r) : need to divide len of edges in 2
    print("len of edges :", len(net.edges) / 2)
    print("len of cut / num of edges :", 2 * len_of_cut / len(net.edges))'''
    # For G(n,c) : not need to divide len of edges in 2
    print("len of edges :", len(net.edges))
    print("len of cut / num of edges :", len_of_cut / len(net.edges))
    # net.draw_network("maximal_cut_by_neighbors", nodes_list=set_a)


if __name__ == '__main__':
    main()
