import posa_algorithm
import erdos_renyi_model_generation
import networkx as nx
import matplotlib.pyplot as plt

# Call function
n = 40
p = 0.5
g = erdos_renyi_model_generation.gen_graph(n, p)
rail_v_gnp, rail_e_gnp = posa_algorithm.posa(g)

pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos, cmap=plt.get_cmap('jet'), node_size=500)
nx.draw_networkx_labels(g, pos)
nx.draw_networkx_edges(g, pos, edgelist=g.edges, edge_color='k', arrows=True)
nx.draw_networkx_edges(g, pos, edgelist=rail_e_gnp, edge_color='r', arrows=True)
plt.savefig("posa_path_drawing.png")
plt.show()
