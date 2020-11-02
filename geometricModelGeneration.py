
import networkx as nx
import matplotlib.pyplot as plt
# Generate geometric graph
# check on a large n!
# how to make on R^d when d>2?
# draw [0,1]^2


def gen_graph(n, r):
    # n = 30
    # radius = 0.4
    # dim = 2
    # p = 2
    # random_geometric_graph(n, radius, dim=2, pos=None, p=2, seed=None)
    # pos = {i: (random.gauss(0, 1), random.gauss(0, 1)) for i in range(n)}
    # G = nx.random_geometric_graph(n=n, radius=radius, dim=dim, pos=pos, p=p, seed=None)

    g = nx.random_geometric_graph(n=n, radius=r)
    nx.draw(g, with_labels=True)
    plt.savefig("simple_path.png")
    plt.show()
    return g
