from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx
import matplotlib.pyplot as plt


# Generate graph
def gen_graph(n, p):
    # Random------------------------
    g = erdos_renyi_graph(n, p)
    print("g.nodes:")
    print(g.nodes)
    print("g.edges:")
    print(g.edges)
    nx.draw(g, with_labels=True)
    plt.savefig("simple_path.png")
    plt.show()

    '''
    g.nodes:
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    g.edges:
    [(0, 1), (0, 2), (0, 5), (0, 7), (0, 8), (1, 3), (1, 5), (1, 6), (1, 8), (1, 9), (2, 3), (2, 4), (2, 5), (2, 6), 
    (2, 8), (3, 5), (3, 7), (3, 8), (3, 9), (4, 5), (4, 7), (5, 6), (5, 7), (5, 8), (6, 7), (6, 9), (7, 8)]
    
    # Example: do cycle with rotation - 10
    g = nx.Graph()
    g.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 8)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 4)
    g.add_edge(2, 8)
    g.add_edge(3, 4)
    g.add_edge(3, 6)
    g.add_edge(3, 7)
    g.add_edge(3, 8)
    g.add_edge(3, 9)
    g.add_edge(4, 5)
    g.add_edge(4, 7)
    g.add_edge(4, 9)
    g.add_edge(5, 8)
    g.add_edge(5, 9)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(7, 8)
    g.add_edge(7, 9)
    nx.draw(G, with_labels=True)
    plt.savefig("simple_path.png")
    plt.show()
    
    #Example: do cycle without rotation - 6
    g = nx.Graph()
    g.add_nodes_from([0, 1, 2, 3, 4, 5])
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    nx.draw(G, with_labels=True)
    plt.savefig("simple_path.png")
    plt.show()
    
    #Example: do cycle without rotation - 10
    g = nx.Graph()
    g.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    g.add_edge(0, 4)
    g.add_edge(0, 6)
    g.add_edge(0, 7)
    g.add_edge(0, 9)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 5)
    g.add_edge(1, 6)
    g.add_edge(1, 7)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(2, 7)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 7)
    g.add_edge(4, 6)
    g.add_edge(4, 7)
    g.add_edge(4, 8)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 9)
    g.add_edge(8, 9)
    nx.draw(G, with_labels=True)
    plt.savefig("simple_path.png")
    plt.show()
    return G
    '''

    return g
