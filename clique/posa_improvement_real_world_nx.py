import math


# Posa algorithm
def posa(g):
    # Step 1-------------------------------------------------------
    print("Start of step 1:")
    # n = len(g.nodes)
    rail_v = []
    rail_e = []
    # We are starting from the first node - insert it to the rail and call to utility function
    x = next(iter(g.nodes))
    rail_v.append(x)
    rail_v, rail_e = posa_loop(g, x, rail_v, rail_e)
    print("len of path :", len(rail_v))
    if len(rail_v) == len(g.nodes):
        print("Found a path :)")
    return rail_v, rail_e


# --------------------------------------------------------------------------------
# Utility function, get graph and node, and do the 3 steps of building an hamiltonian cycle

def posa_loop(g, x, rail_v, rail_e):
    # call utility function that create initial path
    rail_v, rail_e = insert_to_rail(g, x, rail_v, rail_e)
    print("rail_v:", rail_v)
    print("rail_e:", rail_e)

    # Step 2-------------------------------------------------------
    print("Start of step 2:")
    # Check if the path is not hamiltonian
    if len(rail_v) < len(g.nodes):
        if len(rail_v) < 3:
            print("len of path :", len(rail_v))
            exit('algorithm failed to find a path!')  # algorithm failed
        # If the algorithm didn't fail - call utility function that make it hamiltonian
        rail_v, rail_e = rot_ext(g, rail_v, rail_e)
    print("rail_v:", rail_v)
    print("rail_e:", rail_e)
    return rail_v, rail_e


# --------------------------------------------------------------------------------------------------------------------
# Utility function: get two node and return the distance between

def node_distance(g, a, b):
    x_pos_a, y_pos_a = g.nodes[a]['pos']
    x_pos_b, y_pos_b = g.nodes[b]['pos']
    # The distance between a and b
    val = (x_pos_a - x_pos_b) ** 2 + (y_pos_a - y_pos_b) ** 2
    dist_a_b = math.sqrt(val)
    # print("a:", a, "b:", b, "dist_a_b:", dist_a_b)
    return dist_a_b


# --------------------------------------------------------------------------------
# Utility function, get rail and make it hamiltonian

def rot_ext(g, rail_v, rail_e):
    xt = rail_v[len(rail_v) - 1]
    # Run all over x's neighbors and insert them into arrays
    adj_x = []
    for e in g.edges:
        if e[0] == xt:
            adj_x.append(e[1])
        if e[1] == xt:
            adj_x.append(e[0])
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
        for e in g.edges:
            if e[0] == xi_plus_one:
                adj_xi_plus_one.append(e[1])
            if e[1] == xi_plus_one:
                adj_xi_plus_one.append(e[0])
        for xk in adj_xi_plus_one:
            # if isAt(rail_e, (xi_plus_one, xk)) == 1 or isAt(rail_e, (xk, xi_plus_one)) == 1:
            if is_at(rail_v, xk) == 1:
                continue
            # Call utility function that to the swap - add the edge (xi+1, xk), (xi,xt) and delete the edge (xi+1, xk)
            rail_v, rail_e = swap_rail(xi, xi_plus_one, xk, xt, rail_v)
            flag = 1  # we back from swap
            break
        break
    if flag == 0:
        print("len of path :", len(rail_v))
        exit('algorithm failed to find a path!')  # algorithm failed
    return rail_v, rail_e


# --------------------------------------------------------------------------------
# Utility function: do the swap of the rotation extension

def swap_rail(xi, xi_plus_one, xk, xt, rail_v):
    temp_v = []
    temp_e = []
    index = 0
    while rail_v[index] != xi_plus_one:
        temp_v.append(rail_v[index])
        if index != 0:
            temp_e.append((rail_v[index - 1], rail_v[index]))
        index += 1
    temp_v.append(xt)
    temp_e.append((xi, xt))
    # endIndex run on rail_v, index run on tempV
    index += 1
    end_index = len(rail_v) - 2
    while end_index >= rail_v.index(xi_plus_one):
        temp_v.append(rail_v[end_index])
        temp_e.append((rail_v[end_index + 1], rail_v[end_index]))  # How direct from rail_e?
        end_index -= 1
        index += 1
    temp_v.append(xk)
    temp_e.append((xi_plus_one, xk))
    rail_v = temp_v
    rail_e = temp_e
    return rail_v, rail_e


# --------------------------------------------------------------------------------

# Utility function: get node and rails, and insert the neighbors of the node into the rail
def insert_to_rail(g, x, rail_v, rail_e):
    # Run all over x's neighbors and insert them into array
    adj_x = []
    for e in g.edges:
        if e[0] == x:
            adj_x.append(e[1])
        if e[1] == x:
            adj_x.append(e[0])
    # Run all over x's neighbors, choose one that is not in the rail, insert it and call recursion
    for y in adj_x:
        if is_at(rail_v, y) == 0:
            rail_v.append(y)
            rail_e.append((x, y))
            rail_v, rail_e = insert_to_rail(g, y, rail_v, rail_e)
            break
    rail_v, rail_e = absorb_vertices(g, rail_v, rail_e)
    return rail_v, rail_e


def absorb_vertices(g, rail_v, rail_e):
    # do for every vertex possible
    # for every two vertices that are next to each other on the rail
    """
    # all neighbors in rail
    adj_v = []
    for v in g.nodes:# O(n^2)
        for e in g.edges:
            if e[0] == v and e[0] in rail_v:
                adj_v.append(e[1])
            if e[1] == v and e[1] in rail_v:
                adj_v.append(e[0])
    for v1 in g.nodes:  # O(n^2)
        for v2 in rail_v:
            if (v1,v2) in rail_e or (v2,v1) in rail_e:
                adj_v.append(v2)
    """
    # first neighbor and second neighbor found - greedy
    # absorb
    # return railV and railV
    if len(rail_v) <= 1:
        return rail_v, rail_e
    # Run all over V and check every node that is not in rail_v
    for v in g.nodes:
        if is_at(rail_v, v) == 1:
            continue
        # adj_v - v's neighbors that already in rail_v
        adj_v = []
        for e in g.edges:
            if e[0] == v and is_at(rail_v, e[1]) == 1:
                adj_v.append(e[1])
            if e[1] == v and is_at(rail_v, e[0]) == 1:
                adj_v.append(e[0])
        # Check for two following neighbors in rail_v that have neighbors which is not in rail_v
        for xi in rail_v:
            if xi == rail_v[len(rail_v) - 1]:
                continue
            if is_at(adj_v, xi) == 0:
                continue
            xi_plus_one = rail_v[rail_v.index(xi) + 1]
            if is_at(adj_v, xi_plus_one) == 0:
                continue
            rail_v, rail_e = apply_absorption(rail_v, v, xi, xi_plus_one)
            break
    return rail_v, rail_e


# --------------------------------------------------------------------------------------------------------------------
# Utility function: insert v to the rail between xi and xi_plus_one

def apply_absorption(rail_v, v, xi, xi_plus_one):
    temp_v = []
    temp_e = []
    index = 0
    # Insert all the nodes until xi
    while rail_v[index] != xi_plus_one:
        temp_v.append(rail_v[index])
        if index != 0:
            temp_e.append((rail_v[index - 1], rail_v[index]))
            # temp_e.append(rail_e[index-1])
        index += 1
    # Insert all v and xi_plus_one
    temp_v.append(v)
    temp_e.append((xi, v))
    temp_v.append(xi_plus_one)
    temp_e.append((v, xi_plus_one))
    index += 1
    # Insert all the nodes until the end
    while index < len(rail_v):
        temp_v.append(rail_v[index])
        # if index != len(rail_v)-1:
        temp_e.append((rail_v[index - 1], rail_v[index]))
        index += 1
    return temp_v, temp_e


# --------------------------------------------------------------------------------------------------------------------
# Utility function: get element and arr, return 1 if the element is at the array and 0 if not

def is_at(arr, ele):
    for a in arr:
        if a == ele:
            return 1
    return 0
