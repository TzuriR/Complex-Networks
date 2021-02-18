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
