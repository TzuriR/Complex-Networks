import sys
import networkx as nx
# import matplotlib.pyplot as plt
import posa_improvement_for_geometric_model
import posa_algorithm
# import geometric_model_generation
import pandas as pd
import sharp_threshold_geometric

'''import posaWithNetworkClass
import erdosRenyiNetwork
import Point as Pnt
import random as rd
import Edge as Edg
import erdosRenyiModelGeneration
import geometricModelGeneration'''

'''
#Run posa on our erdos renyi network
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
# =================================================
'''
n = 20
r = 0.9
# g = erdosRenyiModelGeneration.gen_graph(n, p)
# rail_v_gnp, rail_e_gnp = posaAlgorithm.posa(g)
g = geometric_model_generation.gen_graph(n, r)
print("Posa improvement :")
rail_v_geo, rail_e_geo = posa_improvement_for_geometric_model.posa(g)
print("len of rail :", len(rail_v_geo))
if len(rail_e_geo) == n:
    print("Found hamiltonian cycle")
else:
    print("Didn't find hamiltonian cycle")
'''
# =================================================
'''# Run posa on gnp
col_names = ['n', 'p', 'avg_path_len', 'avg_times_cycle_found']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100, 150, 200]
p_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for n in n_list:
    for p in p_list:
        n_p_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 10):
            try:
                g = nx.erdos_renyi_graph(n, p)
                rail_v, rail_e = posa_algorithm.posa(g)
                # print("len of rail :", len(rail_v))
                if len(rail_e) == n:
                    # print("Found hamiltonian cycle")
                    n_p_df_i = pd.DataFrame([[n, p, len(rail_v), 1]], columns=col_names)
                    n_p_df = n_p_df.append(n_p_df_i, ignore_index=True, sort=False)
                else:
                    # print("Didn't find hamiltonian cycle")
                    n_p_df_i = pd.DataFrame([[n, p, len(rail_v), 0]], columns=col_names)
                    n_p_df = n_p_df.append(n_p_df_i, ignore_index=True, sort=False)
            except:
                # print("Didn't find hamiltonian cycle")
                len_of_rail = int(str(sys.exc_info()[1]))
                n_p_df_i = pd.DataFrame([[n, p, len_of_rail, 0]], columns=col_names)
                n_p_df = n_p_df.append(n_p_df_i, ignore_index=True, sort=False)
        path_len_mean = n_p_df['avg_path_len'].mean()
        times_cycle_found_sum = n_p_df['avg_times_cycle_found'].sum()
        df_i = pd.DataFrame([[n, p, path_len_mean, times_cycle_found_sum]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('posa_gnp.csv')'''
# =================================================
'''# Run posa on barabasi
col_names = ['n', 'm', 'avg_path_len', 'avg_times_cycle_found']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100, 150, 200]
m_list = [1,2,3,4,5,6,7,8,9]
for n in n_list:
    for m in m_list:
        n_m_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 10):
            try:
                g = nx.barabasi_albert_graph(n, m)
                rail_v, rail_e = posa_algorithm.posa(g)
                # print("len of rail :", len(rail_v))
                if len(rail_e) == n:
                    # print("Found hamiltonian cycle")
                    n_m_df_i = pd.DataFrame([[n, m, len(rail_v), 1]], columns=col_names)
                    n_m_df = n_m_df.append(n_m_df_i, ignore_index=True, sort=False)
                else:
                    # print("Didn't find hamiltonian cycle")
                    n_m_df_i = pd.DataFrame([[n, m, len(rail_v), 0]], columns=col_names)
                    n_m_df = n_m_df.append(n_m_df_i, ignore_index=True, sort=False)
            except:
                # print("Didn't find hamiltonian cycle")
                len_of_rail = int(str(sys.exc_info()[1]))
                n_m_df_i = pd.DataFrame([[n, m, len_of_rail, 0]], columns=col_names)
                n_m_df = n_m_df.append(n_m_df_i, ignore_index=True, sort=False)
        path_len_mean = n_m_df['avg_path_len'].mean()
        times_cycle_found_sum = n_m_df['avg_times_cycle_found'].sum()
        df_i = pd.DataFrame([[n, m, path_len_mean, times_cycle_found_sum]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('posa_barabasi.csv')'''
# =================================================
'''# Run posa on gnr
col_names = ['n', 'r', 'avg_path_len', 'avg_times_cycle_found']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100, 150, 200]
r_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for n in n_list:
    for r in r_list:
        n_r_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 10):
            try:
                g = nx.random_geometric_graph(n, r)
                rail_v, rail_e = posa_algorithm.posa(g)
                # print("len of rail :", len(rail_v))
                if len(rail_e) == n:
                    # print("Found hamiltonian cycle")
                    n_r_df_i = pd.DataFrame([[n, r, len(rail_v), 1]], columns=col_names)
                    n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
                else:
                    # print("Didn't find hamiltonian cycle")
                    n_r_df_i = pd.DataFrame([[n, r, len(rail_v), 0]], columns=col_names)
                    n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
            except:
                # print("Didn't find hamiltonian cycle")
                len_of_rail = int(str(sys.exc_info()[1]))
                n_r_df_i = pd.DataFrame([[n, r, len_of_rail, 0]], columns=col_names)
                n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
        path_len_mean = n_r_df['avg_path_len'].mean()
        times_cycle_found_sum = n_r_df['avg_times_cycle_found'].sum()
        df_i = pd.DataFrame([[n, r, path_len_mean, times_cycle_found_sum]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('posa_gnr.csv')'''
# =================================================
'''# Run posa imp on gnr
col_names = ['n', 'r', 'avg_path_len', 'avg_times_cycle_found']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100, 150, 200]
r_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for n in n_list:
    for r in r_list:
        n_r_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 10):
            try:
                g = nx.random_geometric_graph(n, r)
                rail_v, rail_e = posa_improvement_for_geometric_model.posa(g)
                # print("len of rail :", len(rail_v))
                if len(rail_e) == n:
                    # print("Found hamiltonian cycle")
                    n_r_df_i = pd.DataFrame([[n, r, len(rail_v), 1]], columns=col_names)
                    n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
                else:
                    # print("Didn't find hamiltonian cycle")
                    n_r_df_i = pd.DataFrame([[n, r, len(rail_v), 0]], columns=col_names)
                    n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
            except:
                # print("Didn't find hamiltonian cycle")
                len_of_rail = int(str(sys.exc_info()[1]))
                n_r_df_i = pd.DataFrame([[n, r, len_of_rail, 0]], columns=col_names)
                n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
        path_len_mean = n_r_df['avg_path_len'].mean()
        times_cycle_found_sum = n_r_df['avg_times_cycle_found'].sum()
        df_i = pd.DataFrame([[n, r, path_len_mean, times_cycle_found_sum]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('posa_improvement_gnr.csv')'''
# =================================================
# Run sharp threshold on gnr
col_names = ['n', 'r', 'avg_path_len', 'avg_times_cycle_found']
exp_df = pd.DataFrame(columns=col_names)
'''n_list = [50, 100, 150, 200]
r_list = [0.2, 0.4, 0.5]'''
n_list = [50]
r_list = [0.4]
for n in n_list:
    for r in r_list:
        n_r_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 2):
            path, is_cycle = sharp_threshold_geometric.run_sharp_threshold(n, r)
            n_r_df_i = pd.DataFrame([[n, r, len(path), is_cycle]], columns=col_names)
            n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
        path_len_mean = n_r_df['avg_path_len'].mean()
        times_cycle_found_sum = n_r_df['avg_times_cycle_found'].sum()
        df_i = pd.DataFrame([[n, r, path_len_mean, times_cycle_found_sum]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('sharp_threshold_gnr.csv')
# =================================================
'''# I-M-P-O-R-T-A-N-T : case that Posa regular failed and Posa improve succeeds
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
plt.show()'''

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
