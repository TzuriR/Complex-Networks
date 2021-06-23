import networkx as nx
import maximal_clique_algorithm
import pandas as pd
import barabasi_model_generation

# =================================================
# maximal_clique_gnr

col_names = ['n', 'r', 'avg_clique_size']
exp_df = pd.DataFrame(columns=col_names)
# n_list = [20, 50, 70, 100, 150, 200]
# r_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
n_list = [20, 50, 70, 100]
r_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
for n in n_list:
    for r in r_list:
        n_r_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 5):
            net = maximal_clique_algorithm.generate_model(n, r)
            max_clique_group = maximal_clique_algorithm.deterministic_maximal_clique_algorithm(net)
            n_r_df_i = pd.DataFrame([[n, r, len(max_clique_group)]], columns=col_names)
            n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
        clique_len_mean = n_r_df['avg_clique_size'].mean()
        df_i = pd.DataFrame([[n, r, clique_len_mean]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_clique_gnr.csv')

# =================================================
'''
# barabasi_model_generation
col_names = ['n', 'm', 'avg_clique_size']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100, 150, 200]
m_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
for n in n_list:
    for m in m_list:
        n_m_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 10):
            g = barabasi_model_generation.generate_model(n, m)
            max_clique_group = barabasi_model_generation.barabasi_clique(g)
            n_m_df_i = pd.DataFrame([[n, m, len(max_clique_group)]], columns=col_names)
            n_m_df = n_m_df.append(n_m_df_i, ignore_index=True, sort=False)
        clique_len_mean = n_m_df['avg_clique_size'].mean()
        df_i = pd.DataFrame([[n, m, clique_len_mean]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_clique_barabasi.csv')'''

'''# barabasi_model_generation
col_names = ['n', 'm', 'avg_clique_size', 'avg_times_max_found']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100, 150, 200]
m_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
for n in n_list:
    for m in m_list:
        n_m_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 10):
            g = barabasi_model_generation.generate_model(n, m)
            max_clique_group, is_max_clique = barabasi_model_generation.barabasi_clique(g)
            n_m_df_i = pd.DataFrame([[n, m, len(max_clique_group), is_max_clique]], columns=col_names)
            n_m_df = n_m_df.append(n_m_df_i, ignore_index=True, sort=False)
        clique_len_mean = n_m_df['avg_clique_size'].mean()
        times_max_found_sum = n_m_df['avg_times_max_found'].sum()
        df_i = pd.DataFrame([[n, m, clique_len_mean, times_max_found_sum]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_clique_barabasi.csv')'''
