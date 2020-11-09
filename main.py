import posaAlgorithm
import erdosRenyiModelGeneration
import geometricModelGeneration
import posaImprovementForGeometricModel

# Call function
n = 6
p = 0.8
r = 0.9
# g = erdosRenyiModelGeneration.gen_graph(n, p)
# rail_v_gnp, rail_e_gnp = posaAlgorithm.posa(g)
g = geometricModelGeneration.gen_graph(n, r)
rail_v_geo, rail_e_geo = posaAlgorithm.posa(g)

'''
g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4, 5, 6,7,8,9,10,11])
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
#rail_v = [1,2,3,4,5,6]
#rail_e = [(1,2),(2,3),(3,4),(4,5),(5,6)]
#rail_v, rail_e = posaImprovementForGeometricModel.absorb_vertices(g, rail_v, rail_e)
rail_v, rail_e = posaImprovementForGeometricModel.posa(g)
'''
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
