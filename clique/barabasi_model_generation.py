import networkx as nx
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------------------------------
# Get n and m and generate barabasi model

def generate_model(n, m):
    g = nx.barabasi_albert_graph(n, m)
    # nx.draw(g, with_labels=True)
    # plt.savefig("barabasi_graph_drawing.png")
    # plt.show()
    return g


# ---------------------------------------------------------------------------------------------------
# Get graph, run all over its nodes with degree and return the max one

def find_node_with_high_degree(g):
    max_degree = 0
    max_node = 0
    for node_num, degree_num in g.degree:
        if degree_num >= max_degree:
            max_degree = degree_num
            max_node = node_num
    return max_node, max_degree


# ---------------------------------------------------------------------------------------------------
def search_for_clique(g):
    x = 0
    # Option 1 :
    # clique_list = list(nx.enumerate_all_cliques(g))
    # print(clique_list)
    # Option 2 :
    # clique_list = list(nx.find_cliques(g))
    # print(clique_list)
    # Option 3 :
    # clique_list = list(nx.make_max_clique_graph((G[, create_using, name])))
    # Option 4 :
    # make_clique_bipartite(G[, fpos, ...])
    # Option 5 :
    # graph_clique_number(G[, cliques])
    # Option 6 :
    # graph_number_of_cliques(G[, cliques])
    # Option 7 :
    # node_clique_number(G[, nodes, cliques])
    # Option 8 :
    # number_of_cliques(G[, nodes, cliques])
    # Option 9 :
    # cliques_containing_node(G[, nodes, cliques])


# ---------------------------------------------------------------------------------------------------

def clique_high_degree(g, node, nodes_neighbors):
    clique_list = []
    clique_list.append(node)
    # num_of_neigh = len(list(nodes_neighbors))
    # Sort nodes_neighbors by degree : position 1 in the tuple
    nodes_sorted_by_deg = sorted(g.degree(nodes_neighbors), key=lambda x: x[1])
    print("nodes_sorted_by_deg :", nodes_sorted_by_deg)
    while len(nodes_sorted_by_deg) != 0:
        temp_node_num, _ = nodes_sorted_by_deg.pop()
        if is_connected_to_all_clique_nodes(g, clique_list, temp_node_num):
            clique_list.append(temp_node_num)
    return clique_list


# ---------------------------------------------------------------------------------------------------
# Get list of nodes and one node and check if the nodes connected to all the nodes in the group

def is_connected_to_all_clique_nodes(g, clique_list, temp_node_num):
    for node_ele_num in clique_list:
        if not g.has_edge(temp_node_num, node_ele_num) and not g.has_edge(node_ele_num, temp_node_num):
            return False
    return True


def check_if_clique(net, clique_list):
    for ele_1 in clique_list:
        for ele_2 in clique_list:
            if ele_1 != ele_2:
                if not net.is_at_edge_by_points(net.edges, ele_1, ele_2):
                    print("There is no clique")


def check_if_clique_nx(net, clique_list):
    for ele_1 in clique_list:
        for ele_2 in clique_list:
            if ele_1 != ele_2:
                if not net.has_edge(ele_1, ele_2):
                    print("There is no clique")


# ---------------------------------------------------------------------------------------------------

def barabasi_clique(g):
    # get node with highest degree
    max_node, max_degree = find_node_with_high_degree(g)
    print("g.degree :", g.degree)
    print("max_node :", max_node, "max_degree :", max_degree)
    print("neighbors of max node :", list(g.neighbors(max_node)))
    # search_for_clique(g)
    clique_list = clique_high_degree(g, max_node, g.neighbors(max_node))
    print("clique_list :", clique_list)
    print("max length of clique :", len(clique_list))
    pos = nx.spring_layout(g)
    nx.draw(g, pos=pos, with_labels=True)
    nx.draw_networkx_nodes(g, pos=pos, nodelist=clique_list, node_color='r')
    plt.savefig("clique_drawing.png")
    plt.show()
    check_if_clique_nx(g, clique_list)
    # Checking
    list_of_cliques = list(nx.enumerate_all_cliques(g))
    max_len = len(list_of_cliques[len(list_of_cliques) - 1])
    print("check length :", max_len)
    # For final report
    # if len(clique_list) == max_len:
    #     return clique_list, 1
    return clique_list

# ---------------------------------------------------------------------------------------------------

def main():
    n = 50
    m = 4
    # generate model
    g = generate_model(n, m)
    _ = barabasi_clique(g)


if __name__ == '__main__':
    main()
