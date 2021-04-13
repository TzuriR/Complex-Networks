# imports
import pandas as pd
import networkx as nx
# import matplotlib.pyplot as plt
import erdos_renyi_network as er_net
import point as pnt
import numpy as np
import posa_algorithm_real_world_nx
import posa_improvement_real_world_nx

def generate_net_from_adj_mat_file_class(file_name, file_type):
    """# Read the data
    adj_mat_df = pd.read_excel('{}.{}'.format(file_name, file_type))
    print(adj_mat_df)
    adj_mat_df = adj_mat_df.drop('Name', 1)
    print(adj_mat_df)
    adj_mat_np = np.asarray(adj_mat_df)
    print(adj_mat_df)
    net = er_net.Network()
    # build nodes
    for i, row in enumerate(adj_mat_np):
        if row.sum() == 0:
            print("No connections")
            continue
        p = pnt.Point(i)
        net.add_vertex(p)
    # add edges
    for i, row in enumerate(adj_mat_np):
        for j, col in enumerate(row):
            if adj_mat_np[i][j] == 1:
                net.add_edge_by_vtx(net.nodes[i], net.nodes[j])
    net.print_network()
    net.draw_network("{}_real_network".format(file_name))"""
    # Read the data
    adj_mat_df = pd.read_excel('{}.{}'.format(file_name, file_type))
    print(adj_mat_df)
    adj_mat_df = adj_mat_df.drop('Name', 1)
    print(adj_mat_df)
    net = er_net.Network()
    # build nodes
    for i, row in adj_mat_df.iterrows():
        if row.sum() == 0:
            print("No connections")
            continue
        p = pnt.Point(i)
        net.add_vertex(p)
    # add edges
    for i, row in adj_mat_df.iterrows():
        for j, col in enumerate(row):
            if adj_mat_df.iloc[i, j] == 1:
                net.add_edge_by_vtx(net.nodes[i], net.nodes[j])
    net.print_network()
    net.draw_network("{}_real_network".format(file_name))
    return net


def generate_net_from_adj_mat_file_nx(file_name, file_type, n):
    # Read the data
    adj_mat_df = pd.read_excel('{}.{}'.format(file_name, file_type))
    print(adj_mat_df)
    adj_mat_df = adj_mat_df.drop('Name', 1)
    # print(adj_mat_df)
    adj_mat_df = sort_df_by_sum(adj_mat_df, n)
    g = nx.Graph()
    # build nodes
    for i, row in adj_mat_df.iterrows():
        if row.sum() == 0:
            # print("No connections")
            continue
        g.add_node(i)
    # add edges
    for i, row in adj_mat_df.iterrows():
        # print("i :", i)
        for j, col in enumerate(row):
            # print("j :", j)
            if adj_mat_df.iloc[i, j] == 1:
                g.add_edge(i, j)
    # nx.draw(g, with_labels=True)
    # plt.savefig("{}_real_network.png".format(file_name))
    # plt.show()
    return g


# Get df and return df with n most connected nodes

def sort_df_by_sum(df, n):
    df.columns = np.arange(len(df.columns))
    # Sort by sum col
    df['sum'] = df.sum(axis=1)
    num_of_edges = (df['sum'].sum())/2
    print("num_of_edges :", num_of_edges)
    df = df.sort_values(by='sum', ascending=False)
    print("After sort :")
    print(df)
    # Get list with the minimum indexes
    df_min = df.tail(len(df) - n)
    min_index_list = list(df_min.index)
    # print("min_index_list :")
    # print(min_index_list)
    # print("len of min_index_list :", len(min_index_list))
    # Filter the df to the n max values
    df = df.head(n)
    # print("After n-filter :")
    df = df.drop(df.columns[min_index_list],axis=1)
    # drop sum column
    df = df.drop('sum', 1)
    # print("After col filter :")
    # print(df)
    df = df.sort_index()
    # print("After sort index :")
    # print(df)
    df.columns = np.arange(len(df.columns))
    for i, c in zip(df.index, df.columns):
        df = df.rename({i: c}, axis='index')
    # df.index.names = np.arange(len(df.columns))
    print("After change index :")
    print(df)
    return df

def count_tr(net):
    s = 0
    for i in range(0, len(net.nodes)):
        for j in range(0, i):
            for k in range(0, j):
                if net.has_edge(i, j) and net.has_edge(i, k) and net.has_edge(j, k):
                    s += 1
    print("s:", s)
    return s

def main():
    n = 1000
    # Run our class :
    '''# 250315 edges
    twitter_net = generate_net_from_adj_mat_file_class('Twitter_Data', 'xlsx')
    # 50153 edges
    # facebook_net = generate_net_from_adj_mat_file_class('Facebook_Data', 'xlsx')
    # 4933 edges
    # instagram_net = generate_net_from_adj_mat_file_class('Instagram_Data', 'xlsx')
    rail_v, rail_e = posa_algorithm_real_world_class.posa(twitter_net)'''
    # Run our nx :
    # --------------------------------------------------------------------------------------------
    # Twitter
    # 250315 edges
    # s: 20916815
    twitter_net = generate_net_from_adj_mat_file_nx('Twitter_Data', 'xlsx', n)
    # --------------------------------------------------------------------------------------------
    # Facebook
    # 50153 edges
    # s: 167964
    # facebook_net = generate_net_from_adj_mat_file_nx('Facebook_Data', 'xlsx', n)
    # --------------------------------------------------------------------------------------------
    # Instagram
    # 4933 edges
    # s: 136
    # instagram_net = generate_net_from_adj_mat_file_nx('Instagram_Data', 'xlsx', n)
    s = count_tr(twitter_net)
    # print("is connected :", nx.is_connected(instagram_net))
    # Run posa - hamiltonian cycle
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # print("Run posa :")
    # rail_v_posa, rail_e_posa = posa_algorithm_real_world_nx.posa(facebook_net)
    # Run posa improvement - hamiltonian path
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # print("Run posa improvement :")
    # rail_v_posa_imp, rail_e_posa_imp = posa_improvement_real_world_nx.posa(facebook_net)


if __name__ == '__main__':
    main()
