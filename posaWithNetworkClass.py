#This file include posa algoritm with the network class

# Posa algorithm
def posa(g):
    # Step 1-------------------------------------------------------
    print("Start of step 1:")
    n = len(g.nodes)
    rail_v = []
    rail_e = []
    # We are starting from the first node - insert it to the rail and call to utility function
    x = next(iter(g.nodes))
    rail_v.append(x)
    rail_v, rail_e = posa_loop(g, x, rail_v, rail_e)
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
            exit('algorithm failed to find a path!')  # algorithm failed
        # If the algorithm didn't fail - call utility function that make it hamiltonian
        rail_v, rail_e = rot_ext(g, rail_v, rail_e)
    print("rail_v:", rail_v)
    print("rail_e:", rail_e)

    # Step 3-------------------------------------------------------
    print("Start of step 3:")
    # Check if the path is hamiltonian
    if len(rail_v) == len(g.nodes):
        # Call utility function that will make it cycle
        rail_v, rail_e = make_cycle(g, rail_v, rail_e)
        print("rail_v:", rail_v)
        print("rail_e:", rail_e)
    # Check if the path is not hamiltonian - go back
    else:
        rail_v, rail_e = posa_loop(g, rail_v[len(rail_v) - 1], rail_v, rail_e)
    return rail_v, rail_e


# --------------------------------------------------------------------------------
# Utility function- get hamiltonian path and convert it to hamiltonian cycle
def make_cycle(g, rail_v, rail_e):
    # If there is (x0, xn) - add it to the rail and finish
    if (is_at(g.edges, (rail_v[0], rail_v[len(rail_v) - 1])) == 1) or (
            is_at(g.edges, (rail_v[len(rail_v) - 1], rail_v[0])) == 1):
        rail_e.append((rail_v[len(rail_v) - 1], rail_v[0]))
        return rail_v, rail_e
    i = 0
    flag = 0
    # Run all over the nodes - if there are edge (xi+1,x1), (xi,xn) which are not belongs to the rail - call swapCycle
    for v in rail_v:
        if i == len(rail_v) - 1:
            break
        x0 = rail_v[0]
        xi = v
        xi_plus_one = rail_v[i + 1]
        xn = rail_v[len(rail_v) - 1]
        if ((is_at(g.edges, (x0, xi_plus_one)) == 1) or (is_at(g.edges, (xi_plus_one, x0)) == 1)) and (
                (is_at(rail_v, (xi_plus_one, x0)) == 0) or (is_at(rail_v, (x0, xi_plus_one)) == 0)):
            if ((is_at(g.edges, (xi, xn)) == 1) or (is_at(g.edges, (xn, xi)) == 1)) and (
                    (is_at(rail_v, (xn, xi)) == 0) or (is_at(rail_v, (xi, xn)) == 0)):
                if is_at(rail_e, (xi, xi_plus_one)) == 1:
                    rail_v, rail_e = swap_cycle(x0, xi, xi_plus_one, xn, rail_v, rail_e)
                    flag = 1  # we back from swap
                    break
        i += 1
    if flag == 0:
        exit('algorithm failed to find a cycle!')  # algorithm failed
    return rail_v, rail_e


# --------------------------------------------------------------------------------
# Utility function: do the swap of the rotation extension
# This function add the edges (xi+1,x1), (xi,xn) and delete the edge (xi, xi+1)


def swap_cycle(x0, xi, xi_plus_one, xn, rail_v, rail_e):
    temp_v = []
    temp_e = []
    index = 0
    while rail_v[index] != xi_plus_one:
        temp_v.append(rail_v[index])
        if index != 0:
            temp_e.append((rail_v[index - 1], rail_v[index]))
        index += 1
    temp_v.append(xn)
    temp_e.append((xi, xn))
    # endIndex run on rail_v, index run on tempV
    index += 1
    end_index = len(rail_v) - 2
    while end_index >= rail_v.index(xi_plus_one):
        temp_v.append(rail_v[end_index])
        temp_e.append((rail_v[end_index + 1], rail_v[end_index]))  # How direct from rail_e?
        end_index -= 1
        index += 1
    temp_e.append((xi_plus_one, x0))
    rail_v = temp_v
    rail_e = temp_e
    return rail_v, rail_e


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
            rail_v, rail_e = swap_rail(xi, xi_plus_one, xk, xt, rail_v, rail_e)
            flag = 1  # we back from swap
            break
        break
    if flag == 0:
        exit('algorithm failed to find a path!')  # algorithm failed
    return rail_v, rail_e


# --------------------------------------------------------------------------------
# Utility function: do the swap of the rotation extension

def swap_rail(xi, xi_plus_one, xk, xt, rail_v, rail_e):
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
    return rail_v, rail_e


# Utility function: get element and arr, return 1 if the element is at the array and 0 if not
def is_at(arr, ele):
    for a in arr:
        if a == ele:
            return 1
    return 0
