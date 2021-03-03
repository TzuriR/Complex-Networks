"""import point as Pnt
import edge as Edg
import random as rd
import networkx as nx
import matplotlib.pyplot as plt
import posa_improvement_for_geometricModel
import erdos_renyi_network as er_net"""
import point as Pnt
import geometric_network as Ge_net

# Run random graph :
'''net_example = er_net.Network()
p0 = pnt.Point(0)
net_example.add_vertex(p0)
p1 = pnt.Point(1)
net_example.add_vertex(p1)
p2 = pnt.Point(2)
net_example.add_vertex(p2)
p3 = pnt.Point(3)
net_example.add_vertex(p3)
p4 = pnt.Point(4)
net_example.add_vertex(p4)
p5 = pnt.Point(5)
net_example.add_vertex(p5)
edge0 = edg.Edge(p0, p1, 0)
net_example.add_edge_by_edg(edge0)
edge1 = edg.Edge(p1, p2, 1)
net_example.add_edge_by_edg(edge1)
edge2 = edg.Edge(p2, p3, 2)
net_example.add_edge_by_edg(edge2)
edge3 = edg.Edge(p3, p4, 3)
net_example.add_edge_by_edg(edge3)
edge4 = edg.Edge(p4, p5, 4)
net_example.add_edge_by_edg(edge4)
edge5 = edg.Edge(p5, p0, 5)
net_example.add_edge_by_edg(edge5)
net_example.print_network()
net_example.draw_network()'''

# Run geometric graph :
r = 0.4
net_example = Ge_net.Network(r)
n = 12
for i in range(0, n):
    p = Pnt.Point(i)
    net_example.add_vertex(p)
net_example.make_edges()
net_example.print_network()
net_example.draw_network()

'''
random_point1 = pnt.Point(1)
random_point1.print_point()
random_point2 = pnt.Point(2)
random_point2.print_point()
first_edge = edg.Edge(random_point1, random_point2, 1)
first_edge.print_edge()
'''
'''
n = 80
r = 0.3
dim = 2
p = 2
# g = nx.random_geometric_graph(n=n, radius=r)
pos = {i: (rd.uniform(0, 1), rd.uniform(0, 1)) for i in range(n)}
g = nx.random_geometric_graph(n=n, radius=r, dim=dim, pos=pos, p=p, seed=None)
nx.draw(g, with_labels=True)
plt.savefig("simple_path.png")
plt.show()
rail_v, rail_e = posaImprovementForGeometricModel.posa(g)'''
# The distance between a and b
'''
i = 0
for v in g.nodes:
    print("v:", v)
    x, y = g.nodes[i]['pos']
    print("x:", x, "y:", y)
    i += 1
'''
