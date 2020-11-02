import posaAlgorithm
import erdosRenyiModelGeneration
import geometricModelGeneration

# Call function
n = 20
p = 0.5
r = 0.4
g = erdosRenyiModelGeneration.gen_graph(n, p)
rail_v_gnp, rail_e_gnp = posaAlgorithm.posa(g)
# print
g = geometricModelGeneration.gen_graph(n, r)
rail_v_geo, rail_e_geo = posaAlgorithm.posa(g)
# print
