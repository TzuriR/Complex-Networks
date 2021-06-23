import point_gnc
import gnc_geometric_network
import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd


# -----------------------------------------------------------------------------------------------------
# Function that generates random geometric model

def generate_model(n, c):
    net = gnc_geometric_network.Network(c)
    for i in range(0, n):
        p = point_gnc.Point(i)
        net.add_vertex(p)
    net.make_edges()
    # net.print_network()
    # net.draw_network("main_network")
    return net


# -----------------------------------------------------------------------------------------------------
# Drawing distribution histogram

def draw_distribution_histogram(categories, counts, title):
    plt.bar(categories, counts, color='orange')
    plt.title('{} distribution'.format(title))
    plt.xlabel('degree')
    plt.ylabel('number of nodes')
    plt.savefig('{}_bar.png'.format(title), dpi=300)
    plt.show()


# -----------------------------------------------------------------------------------------------------

def gnc_experiments():
    col_names = ['n', 'c', 'degree', 'amount_of_nodes']
    distributions_df = pd.DataFrame(columns=col_names)
    c_list = [0.05, 0.1, 0.15, 0.2]
    n = 100
    for c in c_list:
        n_c_df = pd.DataFrame(columns=col_names)
        for run_counter in range(0, 100):
            net = generate_model(n, c)
            mat = net.adjacency_matrix()
            sum_arr = []
            for i in range(len(mat)):
                sum_i = 0
                for j in range(len(mat)):
                    sum_i += mat[i][j]
                sum_arr.append(sum_i)
            degree_count = [0] * len(sum_arr)
            for i in range(len(sum_arr)):
                degree_count[sum_arr[i]] += 1
            for i in range(len(degree_count)):
                n_c_df_i = pd.DataFrame([[n, c, i, degree_count[i]]], columns=col_names)
                n_c_df = n_c_df.append(n_c_df_i, ignore_index=True, sort=False)
        '''print("n_c_df :")
        print(n_c_df)'''
        for degree in range(0, n):
            true_false_degree = n_c_df['degree'] == degree
            means_node = n_c_df.loc[true_false_degree, 'amount_of_nodes'].mean()
            df_i = pd.DataFrame([[n, c, degree, means_node]], columns=col_names)
            distributions_df = distributions_df.append(df_i, ignore_index=True, sort=False)
    distributions_df.to_csv('distributions_gnc.csv')


# -----------------------------------------------------------------------------------------------------

def main():
    gnc_experiments()
    '''n = 50
    c = 0.4
    net = generate_model(n, c)
    mat = net.adjacency_matrix()
    sum_arr = []
    for i in range(len(mat)):
        sum = 0
        for j in range(len(mat)):
            sum += mat[i][j]
        sum_arr.append(sum)
    degree_count = [0] * len(sum_arr)
    for i in range(len(sum_arr)):
        degree_count[sum_arr[i]] += 1
    print("degree_count :")
    print(degree_count)
    # draw_distribution_histogram(list(np.arange(n)), degree_count, 'degree')
    # rail_v_geo, rail_e_geo = posa_improvement_for_geometric_model.posa(net)
    # max_clique_group = maximal_clique_algorithm.deterministic_maximal_clique_algorithm(net)
    # maximal_clique_algorithm.check_if_clique(net, max_clique_group)
'''


if __name__ == '__main__':
    main()
