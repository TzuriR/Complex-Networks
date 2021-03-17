import pandas as pd
import geometric_network as geo_net
import point as pnt
import maximal_clique_algorithm
import barabasi_model_generation
import networkx as nx
import matplotlib.pyplot as plt


def generate_net_from_location_mat_class(file_name, file_type):
    # Read the data
    location_df = pd.read_csv('{}.{}'.format(file_name, file_type))
    # Drop non relevant columns
    location_df = location_df.drop(columns=['nb_flights', 'CO2'])
    # Create tuples of nodes
    location_df['dep'] = list(zip(location_df['dep_lat'], location_df['dep_lon']))
    location_df['arr'] = list(zip(location_df['arr_lat'], location_df['arr_lon']))
    print(location_df)
    # location_df.to_csv('location_df.csv')
    dep_lst_unique = location_df['dep'].unique()
    arr_lst_unique = location_df['arr'].unique()
    final_points_lst = list(set(dep_lst_unique) | set(arr_lst_unique))
    print("final_points_lst :", final_points_lst)
    print("len of final_points_lst :", len(final_points_lst))
    # Build network
    net = geo_net.Network()
    # Build nodes
    for i, data_tup in enumerate(final_points_lst):
        p = pnt.Point(i)
        p.x_value = data_tup[0]
        p.y_value = data_tup[1]
        net.add_vertex(p)
    # Build edges
    for i, row in location_df.iterrows():
        temp_point_dep = net.get_point_by_location_values(row['dep_lat'], row['dep_lon'])
        temp_point_arr = net.get_point_by_location_values(row['arr_lat'], row['arr_lon'])
        net.add_edge_by_vtx(temp_point_dep, temp_point_arr)
    net.print_network()
    net.draw_network("{}".format(file_name))
    return net


def generate_net_from_location_mat_nx(file_name, file_type):
    # Read the data
    location_df = pd.read_csv('{}.{}'.format(file_name, file_type))
    # Drop non relevant columns
    location_df = location_df.drop(columns=['nb_flights', 'CO2'])
    # Create tuples of nodes
    location_df['dep'] = list(zip(location_df['dep_lat'], location_df['dep_lon']))
    location_df['arr'] = list(zip(location_df['arr_lat'], location_df['arr_lon']))
    print(location_df)
    # location_df.to_csv('location_df.csv')
    dep_lst_unique = location_df['dep'].unique()
    arr_lst_unique = location_df['arr'].unique()
    final_points_lst = list(set(dep_lst_unique) | set(arr_lst_unique))
    print("final_points_lst :", final_points_lst)
    print("len of final_points_lst :", len(final_points_lst))
    # Build network
    g = nx.Graph()
    pos = {}
    # Build nodes
    for i, data_tup in enumerate(final_points_lst):
        pos[i] = data_tup
        g.add_node(i)
        g.nodes[i]['pos'] = data_tup
    # print("len(g.nodes) :", len(g.nodes))
    # Build edges
    for i, row in location_df.iterrows():
        temp_point_dep = get_point_by_location_values_nx(g, row['dep_lat'], row['dep_lon'])
        temp_point_arr = get_point_by_location_values_nx(g, row['arr_lat'], row['arr_lon'])
        g.add_edge(temp_point_dep, temp_point_arr)
    nx.draw(g, pos=pos, with_labels=True)
    plt.savefig("{}.png".format(file_name))
    plt.show()
    return g


def get_point_by_location_values_nx(g, x_val, y_val):
    for i in range(len(g.nodes)):
        if g.nodes[i]['pos'][0] == x_val and g.nodes[i]['pos'][1] == y_val:
            # print("g.nodes[i] :", g.nodes[i], "type :", type(g.nodes[i]))
            return i
    print("There is no node with those values")
    return None


def main():
    net = generate_net_from_location_mat_nx('flight_data', 'csv')
    barabasi_model_generation.barabasi_clique(net)
    # clique_group = maximal_clique_algorithm.deterministic_maximal_clique_algorithm(net)
    # maximal_clique_algorithm.check_if_clique(net, clique_group)


if __name__ == '__main__':
    main()

