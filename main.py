import posaAlgorithm
import erdosRenyiModelGeneration
import geometricModelGeneration

'''
#-----------------------------------------------------------
#Run random graph
n = 30
p = 0.2
g = erdosRenyiModelGeneration.GenGraph(n, p)
railV, railE = posaAlgorithm.Posa(g)

'''
#-----------------------------------------------------------
#Run geometric random graph
n = 100
r = 0.2
g = geometricModelGeneration.GenGraph(n, r)
print("g.nodes:")
print(g.nodes)
print("g.edges:")
print(g.edges)
railV, railE = posaAlgorithm.Posa(g)

