import networkx as nx
import matplotlib.pyplot as plt
import random as rd
# Generate geometric graph
# how to make on R^d when d>2?
# draw [0,1]^2


# Generate graph
def gen_graph(n, r):
    # n = 100
    # r = 0.2
    dim = 2
    p = 2
    # g = nx.random_geometric_graph(n=n, radius=r)
    pos = {i: (rd.uniform(0, 1), rd.uniform(0, 1)) for i in range(n)}
    g = nx.random_geometric_graph(n=n, radius=r, dim=dim, pos=pos, p=p, seed=None)
    # The distance between a and b
    '''i = 0
    for v in g.nodes:
        print("v:", v)
        x, y = g.nodes[i]['pos']
        print("x, y:", x, y)
        i += 1'''
    nx.draw(g, with_labels=True)
    plt.savefig("simple_path.png")
    plt.show()
    return g
