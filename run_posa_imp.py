import networkx as nx
import matplotlib.pyplot as plt
import posaImprovementForGeometricModel

# Case that Posa regular failed and Posa improve succeeds
g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(1, 7)
g.add_edge(2, 7)
g.add_edge(1, 8)
g.add_edge(2, 8)
g.add_edge(7, 11)
g.add_edge(8, 11)
g.add_edge(9, 11)
g.add_edge(10, 11)
g.add_edge(2, 11)
g.add_edge(4, 9)
g.add_edge(5, 9)
g.add_edge(5, 10)
g.add_edge(6, 10)

rail_v, rail_e = posaImprovementForGeometricModel.posa(g)
pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos, cmap=plt.get_cmap('jet'), node_size = 500)
nx.draw_networkx_labels(g, pos)
nx.draw_networkx_edges(g, pos, edgelist=g.edges, edge_color='k', arrows=True)
nx.draw_networkx_edges(g, pos, edgelist=rail_e, edge_color='r', arrows=True)
plt.savefig("posa_improvement_drawing.png")
plt.show()
