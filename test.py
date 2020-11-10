import Point as pnt
import Edge as edg
import random as rd
import networkx as nx
import matplotlib.pyplot as plt
import posaImprovementForGeometricModel

'''
random_point1 = pnt.Point(1)
random_point1.print_point()
random_point2 = pnt.Point(2)
random_point2.print_point()
first_edge = edg.Edge(random_point1, random_point2, 1)
first_edge.print_edge()
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
rail_v, rail_e = posaImprovementForGeometricModel.posa(g)
# The distance between a and b
'''
i = 0
for v in g.nodes:
    print("v:", v)
    x, y = g.nodes[i]['pos']
    print("x:", x, "y:", y)
    i += 1
'''

