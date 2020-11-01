#Posa algorithm
def Posa(g):
    # Step 1-------------------------------------------------------

    print("Start of step 1:")
    n = len(g.nodes)
    railV = []
    railE = []
    #We are starting from the first node - insert it to the rail and call to utility function
    x = 0
    railV.append(x)
    PosaLoop(g, x, railV, railE)
    return railV, railE


# -----------------------------------------------------------------
# Utility functions:

# --------------------------------------------------------------------------------
# Utility function, get graph and node, and do the 3 steps of building an hamiltonian cycle

def PosaLoop(g, x, railV, railE):
    # call utility function that create initial path
    insertToRail(g, x, railV, railE)
    print("railV:")
    print(railV)
    print("railE:")
    print(railE)

    # Step 2-------------------------------------------------------

    print("Start of step 2:")
    # Check if the path is not hamiltonian
    if len(railV) < len(g.nodes):
        if len(railV) < 3:
            exit('algorithm failed to find a path!')  # algorithm failed
        # If the algorithm didnt fail - call utility function that make it hamiltonian
        railV, railE = rotExt(g, railV, railE)
    print("railV:")
    print(railV)
    print("railE:")
    print(railE)

    # Step 3-------------------------------------------------------
    print("Start of step 3:")
    # Check if the path is hamiltonian
    if len(railV) == len(g.nodes):
        # Call utility function that will make it cycle
        railV, railE = makeCycle(g, railV, railE)
        print("railV:")
        print(railV)
        print("railE:")
        print(railE)
    # Check if the path is not hamiltonian - go back
    else:
        PosaLoop(g, railV[len(railV)-1], railV, railE)

    return railV, railE

# --------------------------------------------------------------------------------
# Utility function- get hamitonian path and convert it to hamiltonian cycle

def makeCycle(g, railV, railE):
    #If there is (x0, xn) - add it to the rail and finish
    if (isAt(g.edges, (railV[0], railV[len(railV) - 1])) == 1) or (
            isAt(g.edges, (railV[len(railV) - 1], railV[0])) == 1):
        railE.append((railV[len(railV) - 1], railV[0]))
        return railV, railE
    i = 0
    flag = 0
    #Run all over the nodes - if there are edge (xi+1,x1), (xi,xn) which are not belongs to the rail - call utility function swapCycle
    for v in railV:
        if i == len(railV) - 1:
            break
        x0 = railV[0]
        xi = v
        xiplusone = railV[i + 1]
        xn = railV[len(railV) - 1]
        if ((isAt(g.edges, (x0, xiplusone)) == 1) or (isAt(g.edges, (xiplusone, x0)) == 1)) and (
                (isAt(railV, (xiplusone, x0)) == 0) or (isAt(railV, (x0, xiplusone)) == 0)):
            if ((isAt(g.edges, (xi, xn)) == 1) or (isAt(g.edges, (xn, xi)) == 1)) and (
                    (isAt(railV, (xn, xi)) == 0) or (isAt(railV, (xi, xn)) == 0)):
                if isAt(railE, (xi, xiplusone)) == 1:
                    railV, railE = swapCycle(x0, xi, xiplusone, xn, railV, railE)
                    flag = 1  # we back from swap
                    break
        i += 1
    if flag == 0:
        exit('algorithm failed to find a cycle!')  # algorithm failed
    return railV, railE

# --------------------------------------------------------------------------------
# Utility function: do the swap of the rotation extenstion
# This function add the edges (xi+1,x1), (xi,xn) and delete the edge (xi, xi+1)

def swapCycle(x0, xi, xiplusone, xn, railV, railE):
    tempV = []
    tempE = []
    index = 0
    while railV[index] != xiplusone:
        tempV.append(railV[index])
        if index != 0:
            tempE.append((railV[index - 1], railV[index]))
        index += 1
    tempV.append(xn)
    tempE.append((xi, xn))
    # endIndex run on railV, index run on tempV
    index += 1
    endIndex = len(railV) - 2
    while endIndex >= railV.index(xiplusone):
        tempV.append(railV[endIndex])
        tempE.append((railV[endIndex + 1], railV[endIndex]))  # How direct from railE?
        endIndex -= 1
        index += 1
    tempE.append((xiplusone, x0))
    railV = tempV
    railE = tempE
    return railV, railE

# --------------------------------------------------------------------------------
# Utility function, get rail and make it hamitonian

def rotExt(g, railV, railE):
    xt = railV[len(railV) - 1]
    # Run all over x's neighbors and insert them into arrays
    adjX = []
    for e in g.edges:
        if e[0] == xt:
            adjX.append(e[1])
        if e[1] == xt:
            adjX.append(e[0])

    # Do the extention rotation
    if len(adjX) <= 1:
        exit('algorithm failed to find a path!')  # algorithm failed
    flag = 0  # tell us if we did swap
    for xi in adjX:
        if xi == railV[len(railV) - 2]:
            continue
        if isAt(railE, (xi, xt)) == 1:
            continue
        xiplusone = railV[railV.index(xi) + 1]
        adjXiplusOne = []
        for e in g.edges:
            if e[0] == xiplusone:
                adjXiplusOne.append(e[1])
            if e[1] == xiplusone:
                adjXiplusOne.append(e[0])
        for xk in adjXiplusOne:
            # if isAt(railE, (xiplusone, xk)) == 1 or isAt(railE, (xk, xiplusone)) == 1:
            if isAt(railV, xk) == 1:
                continue
            # Call utility function that to the swap - add the edge (xi+1, xk), (xi,xt) and delete the edge (xi+1, xk)
            railV, railE = swapRail(xi, xiplusone, xk, xt, railV, railE)
            flag = 1  # we back from swap
            break
        break
    if flag == 0:
        exit('algorithm failed to find a path!')  # algorithm failed
    return railV, railE

# --------------------------------------------------------------------------------
# Utility function: do the swap of the rotation extenstion

def swapRail(xi, xiplusone, xk, xt, railV, railE):
    tempV = []
    tempE = []
    index = 0
    while railV[index] != xiplusone:
        tempV.append(railV[index])
        if index != 0:
            tempE.append((railV[index - 1], railV[index]))
        index += 1
    tempV.append(xt)
    tempE.append((xi, xt))
    # endIndex run on railV, index run on tempV
    index += 1
    endIndex = len(railV) - 2
    while endIndex >= railV.index(xiplusone):
        tempV.append(railV[endIndex])
        tempE.append((railV[endIndex + 1], railV[endIndex]))  # How direct from railE?
        endIndex -= 1
        index += 1
    tempV.append(xk)
    tempE.append((xiplusone, xk))
    railV = tempV
    railE = tempE
    return railV, railE

# --------------------------------------------------------------------------------

# Utility function: get node and rails, and insert the neighbors of the node into the rail
def insertToRail(g, x, railV, railE):
    # Run all over x's neighbors and insert them into array
    adjX = []
    for e in g.edges:
        if e[0] == x:
            adjX.append(e[1])
        if e[1] == x:
            adjX.append(e[0])
    # Run all over x's neighbors, choose one that is not in the rail, insert it and call recursion
    for y in adjX:
        if isAt(railV, y) == 0:
            railV.append(y)
            railE.append((x, y))
            insertToRail(g, y, railV, railE)
            break
    '''
    # Run all over x's neighbors and insert them into arrays
    adjXR = []
    adjXL = []
    for e in g.edges:
        if e[0] == x:
            adjXR.append(e[1])
        if e[1] == x:
            adjXL.append(e[0])
    print("x:")
    print(x)
    flag = 0
    # Choose one of x's neighbors right that not exists at railV
    for y in adjXR:
        print("y:")
        print(y)
        if isAt(railV, y) == 1:
            continue
        else:
            railV.append(y)
            railE.append((x, y))
            insertToRail(g, y, railV, railE)
            flag = 1
            break

    if flag != 1:
        # Choose one of x's neighbors left that not exists at railV
        for z in adjXL:
            print("z:")
            print(z)
            if isAt(railV, z) == 1:
                continue
            else:
                railV.append(z)
                railE.append((x, z))
                insertToRail(g, z, railV, railE)
                break
    '''

# Utility function: get element and arr, return 1 if the element is at the array and 0 if not
def isAt(arr, ele):
    for a in arr:
        if a == ele:
            return 1
    return 0