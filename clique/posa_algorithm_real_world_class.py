# This file include posa algorithm with the network class

# Changes to do : (1) Use the adj matrix from net (2) Make rail adj matrix (3) Use serial_number in is_at()

# Posa algorithm
def posa(net):
    # Step 1-------------------------------------------------------
    print("Start of step 1:")
    # n = len(net.nodes)
    rail_v = []
    rail_e = []
    # We are starting from the first node - insert it to the rail and call to utility function
    x = next(iter(net.nodes))
    rail_v.append(x)
    rail_v, rail_e = posa_loop(net, x, rail_v, rail_e)
    print("len of path :", len(rail_v))
    return rail_v, rail_e


# --------------------------------------------------------------------------------
# Utility function, get graph and node, and do the 3 steps of building an hamiltonian cycle

def posa_loop(net, x, rail_v, rail_e):
    # call utility function that create initial path
    rail_v, rail_e = insert_to_rail(net, x, rail_v, rail_e)
    print("rail_v:")
    net.print_point_arr(rail_v)
    print("rail_e:")
    net.print_edge_arr(rail_e)

    # Step 2-------------------------------------------------------
    print("Start of step 2:")
    # Check if the path is not hamiltonian
    if len(rail_v) < len(net.nodes):
        if len(rail_v) < 3:
            print("len of path :", len(rail_v))
            exit('algorithm failed to find a path!')  # algorithm failed
        # If the algorithm didn't fail - call utility function that make it hamiltonian
        rail_v, rail_e = rot_ext(net, rail_v, rail_e)
    print("rail_v:")
    net.print_point_arr(rail_v)
    print("rail_e:")
    net.print_point_arr(rail_e)
    return rail_v, rail_e


# --------------------------------------------------------------------------------
# Utility function, get rail and make it hamiltonian

def rot_ext(net, rail_v, rail_e):
    xt = rail_v[len(rail_v) - 1]
    # Run all over x's neighbors and insert them into arrays
    adj_x = []
    for e in net.edges:
        if e.vtx_1.serial_number == xt.serial_number:
            adj_x.append(e.vtx_2)
        if e.vtx_2.serial_number == xt.serial_number:
            adj_x.append(e.vtx_1)

    # Do the extension rotation
    if len(adj_x) <= 1:
        print("len of path :", len(rail_v))
        exit('algorithm failed to find a path!')  # algorithm failed
    flag = 0  # tell us if we did swap
    for xi in adj_x:
        if xi == rail_v[len(rail_v) - 2]:
            continue
        if is_at(rail_e, (xi, xt)) == 1:
            continue
        xi_plus_one = rail_v[rail_v.index(xi) + 1]
        adj_xi_plus_one = []
        for e in net.edges:
            if e.vtx_1.serial_number == xi_plus_one.serial_number:
                adj_xi_plus_one.append(e.vtx_2)
            if e.vtx_2.serial_number == xi_plus_one.serial_number:
                adj_xi_plus_one.append(e.vtx_1)
        for xk in adj_xi_plus_one:
            # if isAt(rail_e, (xi_plus_one, xk)) == 1 or isAt(rail_e, (xk, xi_plus_one)) == 1:
            if is_at(rail_v, xk) == 1:
                continue
            # Call utility function that to the swap - add the edge (xi+1, xk), (xi,xt) and delete the edge (xi+1, xk)
            rail_v, rail_e = swap_rail(net, xi, xi_plus_one, xk, xt, rail_v)
            flag = 1  # we back from swap
            break
        break
    if flag == 0:
        print("len of path :", len(rail_v))
        exit('algorithm failed to find a path!')  # algorithm failed
    return rail_v, rail_e


# --------------------------------------------------------------------------------
# Utility function: do the swap of the rotation extension

def swap_rail(net, xi, xi_plus_one, xk, xt, rail_v):
    temp_v = []
    temp_e = []
    index = 0
    while rail_v[index] != xi_plus_one:
        temp_v.append(rail_v[index])
        if index != 0:
            edge_temp = net.find_edge_between_vertices(rail_v[index - 1], rail_v[index])
            temp_e.append(edge_temp)
            # temp_e.append((rail_v[index - 1], rail_v[index]))
        index += 1
    temp_v.append(xt)
    edge_temp = net.find_edge_between_vertices(xi, xt)
    temp_e.append(edge_temp)
    # temp_e.append((xi, xt))
    # endIndex run on rail_v, index run on tempV
    index += 1
    end_index = len(rail_v) - 2
    while end_index >= rail_v.index(xi_plus_one):
        temp_v.append(rail_v[end_index])
        edge_temp = net.find_edge_between_vertices(rail_v[end_index + 1], rail_v[end_index])
        temp_e.append(edge_temp)
        # temp_e.append((rail_v[end_index + 1], rail_v[end_index]))  # How direct from rail_e?
        end_index -= 1
        index += 1
    temp_v.append(xk)
    edge_temp = net.find_edge_between_vertices(xi_plus_one, xk)
    temp_e.append(edge_temp)
    # temp_e.append((xi_plus_one, xk))
    rail_v = temp_v
    rail_e = temp_e
    return rail_v, rail_e


# --------------------------------------------------------------------------------
# Utility function: get node and rails, and insert the neighbors of the node into the rail

def insert_to_rail(net, x, rail_v, rail_e):
    # Run all over x's neighbors and insert them into array
    adj_x = []
    for e in net.edges:
        if e.vtx_1.serial_number == x.serial_number:
            adj_x.append(e.vtx_2)
        if e.vtx_2.serial_number == x.serial_number:
            adj_x.append(e.vtx_1)
    # Run all over x's neighbors, choose one that is not in the rail, insert it and call recursion
    for y in adj_x:
        if is_at(rail_v, y) == 0:
            rail_v.append(y)
            edge_temp = net.find_edge_between_vertices(x, y)
            rail_e.append(edge_temp)
            rail_v, rail_e = insert_to_rail(net, y, rail_v, rail_e)
            break
    return rail_v, rail_e


# Utility function: get element and arr, return 1 if the element is at the array and 0 if not
def is_at(arr, ele):
    for a in arr:
        if a == ele:
            return 1
    return 0
