import networkx as nx
import matplotlib.pyplot as plt
import posa_improvement_for_geometric_model
# import posa_algorithm

'''import posaWithNetworkClass
import erdosRenyiNetwork
import Point as Pnt
import random as rd
import Edge as Edg
import erdosRenyiModelGeneration
import geometricModelGeneration'''

'''
#Run posa on erdos renyi network
er_net = erdosRenyiNetwork.Network()
n = 20
for i in range(0, n):
    p = pnt.Point(i)
    er_net.add_vertex(p)
for i in range(0, n):
    num = round(rd.uniform(0, n))
    for j in range(0, num):
        if i != j:
            er_net.add_edge_by_vtx(er_net.nodes[i], er_net.nodes[j])
er_net.draw_network()
rail_v, rail_e = posaWithNetworkClass.posa(er_net)
'''

'''
# Call function
n = 50
p = 0.8
r = 0.6
# g = erdosRenyiModelGeneration.gen_graph(n, p)
# rail_v_gnp, rail_e_gnp = posaAlgorithm.posa(g)
g = geometricModelGeneration.gen_graph(n, r)
print("Posa improvement :")
rail_v_geo_i, rail_e_geo_i = posaImprovementForGeometricModel.posa(g)
print("Posa original :")
rail_v_geo, rail_e_geo = posaAlgorithm.posa(g)
'''

# I-M-P-O-R-T-A-N-T : case that Posa regular failed and Posa improve succeeds
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
'''nx.draw(g, with_labels=True)
plt.savefig("network_drawing.png")
plt.show()'''
# rail_v = [1,2,3,4,5,6]
# rail_e = [(1,2),(2,3),(3,4),(4,5),(5,6)]
# rail_v, rail_e = posaImprovementForGeometricModel.absorb_vertices(g, rail_v, rail_e)
# rail_v, rail_e = posa_algorithm.posa(g)
rail_v, rail_e = posa_improvement_for_geometric_model.posa(g)
pos = nx.spring_layout(g)
# nx.draw(g, with_labels=True)
nx.draw_networkx_nodes(g, pos, cmap=plt.get_cmap('jet'), node_size=500)
nx.draw_networkx_labels(g, pos)
nx.draw_networkx_edges(g, pos, edgelist=g.edges, edge_color='k', arrows=True)
nx.draw_networkx_edges(g, pos, edgelist=rail_e, edge_color='r', arrows=True)
plt.savefig("posa_path_improvement_drawing.png")
plt.show()

'''G = nx.random_geometric_graph(6, 0.5)
edge_x = []
edge_y = []
for edge in G.edges():
    print("edge[0]")
    print(edge[0])
    print("edge[1]")
    print(edge[1])
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    print("x0")
    print(x0)
    print("y0")
    print(y0)
    print("x1")
    print(x1)
    print("y1")
    print(y1)
nx.draw(G, with_labels=True)
plt.savefig("simple_path.png")
plt.show()'''
