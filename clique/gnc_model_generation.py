import point_gnc
import gnc_geometric_graph
import maximal_clique_algorithm

# -----------------------------------------------------------------------------------------------------
# Function that generates random geometric model

def generate_model(n, c):
    net = gnc_geometric_graph.Network(c)
    for i in range(0, n):
        p = point_gnc.Point(i)
        net.add_vertex(p)
    net.make_edges()
    net.print_network()
    net.draw_network("main_network")
    return net


# -----------------------------------------------------------------------------------------------------

def main():
    n = 50
    c = 0.01
    net = generate_model(n, c)
    max_clique_group = maximal_clique_algorithm.deterministic_maximal_clique_algorithm(net)
    # maximal_clique_algorithm.check_if_clique(net, max_clique_group)


if __name__ == '__main__':
    main()
