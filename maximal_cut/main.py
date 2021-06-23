import maximal_cut_by_neighbors
import maximal_cut_by_eigenvectors
import pandas as pd

# =================================================
# maximal_cut_by_neighbors : G(n,r) based algorithm 1

'''col_names = ['n', 'r', 'avg_edges_num', 'avg_cut_size', 'avg_cut_ratio']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100]
r_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for n in n_list:
    for r in r_list:
        n_r_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 5):
            edges_num, len_of_cut, cut_ratio = maximal_cut_by_neighbors.max_cut_neighbors_gnr(n, r, 1)
            n_r_df_i = pd.DataFrame([[n, r, edges_num, len_of_cut, cut_ratio]], columns=col_names)
            n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
        edges_num_mean = n_r_df['avg_edges_num'].mean()
        cut_size_mean = n_r_df['avg_cut_size'].mean()
        cut_ratio_mean = n_r_df['avg_cut_ratio'].mean()
        df_i = pd.DataFrame([[n, r, edges_num_mean, cut_size_mean, cut_ratio_mean]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_cut_gnr_by_neighbors_based_alg1.csv')'''

# =================================================
'''# maximal_cut_by_neighbors : G(n,r) based bfs

col_names = ['n', 'r', 'avg_edges_num', 'avg_cut_size', 'avg_cut_ratio']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100]
r_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for n in n_list:
    for r in r_list:
        n_r_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 5):
            edges_num, len_of_cut, cut_ratio = maximal_cut_by_neighbors.max_cut_neighbors_gnr(n, r, 2)
            n_r_df_i = pd.DataFrame([[n, r, edges_num, len_of_cut, cut_ratio]], columns=col_names)
            n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
        edges_num_mean = n_r_df['avg_edges_num'].mean()
        cut_size_mean = n_r_df['avg_cut_size'].mean()
        cut_ratio_mean = n_r_df['avg_cut_ratio'].mean()
        df_i = pd.DataFrame([[n, r, edges_num_mean, cut_size_mean, cut_ratio_mean]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_cut_gnr_by_neighbors_based_bfs.csv')'''

# =================================================
'''# maximal_cut_by_neighbors : G(n,r) based degree

col_names = ['n', 'r', 'avg_edges_num', 'avg_cut_size', 'avg_cut_ratio']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100]
r_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for n in n_list:
    for r in r_list:
        n_r_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 5):
            edges_num, len_of_cut, cut_ratio = maximal_cut_by_neighbors.max_cut_neighbors_gnr(n, r, 3)
            n_r_df_i = pd.DataFrame([[n, r, edges_num, len_of_cut, cut_ratio]], columns=col_names)
            n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
        edges_num_mean = n_r_df['avg_edges_num'].mean()
        cut_size_mean = n_r_df['avg_cut_size'].mean()
        cut_ratio_mean = n_r_df['avg_cut_ratio'].mean()
        df_i = pd.DataFrame([[n, r, edges_num_mean, cut_size_mean, cut_ratio_mean]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_cut_gnr_by_neighbors_based_degree.csv')'''

# =================================================
'''# maximal_cut_by_neighbors : G(n,c) based algorithm 1

col_names = ['n', 'c', 'avg_edges_num', 'avg_cut_size', 'avg_cut_ratio']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100]
c_list = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4]
for n in n_list:
    for c in c_list:
        n_c_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 5):
            edges_num, len_of_cut, cut_ratio = maximal_cut_by_neighbors.max_cut_neighbors_gnc(n, c, 1)
            n_c_df_i = pd.DataFrame([[n, c, edges_num, len_of_cut, cut_ratio]], columns=col_names)
            n_c_df = n_c_df.append(n_c_df_i, ignore_index=True, sort=False)
        edges_num_mean = n_c_df['avg_edges_num'].mean()
        cut_size_mean = n_c_df['avg_cut_size'].mean()
        cut_ratio_mean = n_c_df['avg_cut_ratio'].mean()
        df_i = pd.DataFrame([[n, c, edges_num_mean, cut_size_mean, cut_ratio_mean]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_cut_gnc_by_neighbors_based_alg1.csv')'''

# =================================================
# maximal_cut_by_neighbors : G(n,c) based bfs

col_names = ['n', 'c', 'avg_edges_num', 'avg_cut_size', 'avg_cut_ratio']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100]
c_list = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4]
for n in n_list:
    for c in c_list:
        n_c_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 5):
            edges_num, len_of_cut, cut_ratio = maximal_cut_by_neighbors.max_cut_neighbors_gnc(n, c, 2)
            n_c_df_i = pd.DataFrame([[n, c, edges_num, len_of_cut, cut_ratio]], columns=col_names)
            n_c_df = n_c_df.append(n_c_df_i, ignore_index=True, sort=False)
        edges_num_mean = n_c_df['avg_edges_num'].mean()
        cut_size_mean = n_c_df['avg_cut_size'].mean()
        cut_ratio_mean = n_c_df['avg_cut_ratio'].mean()
        df_i = pd.DataFrame([[n, c, edges_num_mean, cut_size_mean, cut_ratio_mean]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_cut_gnc_by_neighbors_based_bfs.csv')

# =================================================
# maximal_cut_by_eigenvectors : G(n,r)

'''col_names = ['n', 'r', 'avg_edges_num', 'avg_cut_size', 'avg_cut_ratio']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100]
r_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for n in n_list:
    for r in r_list:
        n_r_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 5):
            edges_num, len_of_cut, cut_ratio = maximal_cut_by_eigenvectors.max_cut_eigenvectors_gnr(n, r)
            n_r_df_i = pd.DataFrame([[n, r, edges_num, len_of_cut, cut_ratio]], columns=col_names)
            n_r_df = n_r_df.append(n_r_df_i, ignore_index=True, sort=False)
        edges_num_mean = n_r_df['avg_edges_num'].mean()
        cut_size_mean = n_r_df['avg_cut_size'].mean()
        cut_ratio_mean = n_r_df['avg_cut_ratio'].mean()
        df_i = pd.DataFrame([[n, r, edges_num_mean, cut_size_mean, cut_ratio_mean]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_cut_gnr_by_eigenvectors.csv')'''

# =================================================
# maximal_cut_by_eigenvectors : G(n,c)

'''col_names = ['n', 'c', 'avg_edges_num', 'avg_cut_size', 'avg_cut_ratio']
exp_df = pd.DataFrame(columns=col_names)
n_list = [20, 50, 70, 100]
c_list = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4]
for n in n_list:
    for c in c_list:
        n_c_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 5):
            edges_num, len_of_cut, cut_ratio = maximal_cut_by_eigenvectors.max_cut_eigenvectors_gnc(n, c)
            n_c_df_i = pd.DataFrame([[n, c, edges_num, len_of_cut, cut_ratio]], columns=col_names)
            n_c_df = n_c_df.append(n_c_df_i, ignore_index=True, sort=False)
        edges_num_mean = n_c_df['avg_edges_num'].mean()
        cut_size_mean = n_c_df['avg_cut_size'].mean()
        cut_ratio_mean = n_c_df['avg_cut_ratio'].mean()
        df_i = pd.DataFrame([[n, c, edges_num_mean, cut_size_mean, cut_ratio_mean]], columns=col_names)
        exp_df = exp_df.append(df_i, ignore_index=True, sort=False)
exp_df.to_csv('maximal_cut_gnc_by_eigenvectors.csv')'''
