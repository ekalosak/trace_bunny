# Author: Eric Kalosa-Kenyon
# Date: August 15, 2018
#
# This script encodes functions and tests for a greedy graph algorithm framed as
# a bunny in a field eating carrots. The bunny eats carrots at the current
# location, looks around, determines which adjacent cell has most carrots, hops
# there, eats those carrots, repeats until no carrots adjacent.
#
# Example usage:
#   BASH:   python eat_carrots.py
#   PYTHON: >>> bunny(test_field_1, test_start_loc_1)

### BEGIN CODE
import numpy as np
import pdb

# Test cases
test_field_1 = np.asarray(
            [[5, 7, 8, 6, 3],
            [0, 0, 7, 0, 4],
            [4, 6, 3, 4, 9],
            [3, 1, 0, 5, 8]]
            )
test_start_loc_1 = (1, 2)
test_answ_1 = 27

# Constants
# U, D, L, R, STOP = 0, 1, 2, 3, 4
STOP = 0

# Workhorse function
def bunny(field, start_loc):
    """Take a 2D np.array <field> and a tuple of integers <start_loc> and
    perform the bunny algorithm, returning the number of carrots the bunny ends
    up eating (int).

    Args:
        field (2D np.array of int) : field of carrots, number of carrots at a
            location indexed by (i,j) represented by the integer in each cell
            e.g.  the number of carrots at (i, j) is field[i, j].
        start_loc (tuple of int) :

    Returns:
        num_carrots (int) : number of carrots the bunny has eaten by the end.

    Side effects:
        1. prints intermediate output to IO
        2. could throw unexpected exception

    Notes:
    Todo:
        1. check inputs for type soundness - right now this relies on user to
            provide correct types.
        2. check that field has only non-negative integer elements
    """

    c = 0 # carrot counter aka the bunny belly
    fd = field.copy() # retain the original input for debugging
    loc = start_loc

    print("working on field:")
    print(fd)

    c = fd[loc] # eat the first carrot
    fd[loc] = 0

    while(nearby_carrots(fd, loc)): # until there are no carrots near the bunny

        print("working on field:")
        print(fd)

        nd = next_dir(fd, loc) # find the adjacency with most carrots
        print("next direction is: " + str(nd))

        if nd == STOP: # if there are no nearby carrots, quit
            print("no carrots nearby to loc: " + str(loc))
            break

        # update location with the next direction
        loc = loc[0] + nd[0], loc[1] + nd[1]
        pdb.set_trace()

        # eat that carrot!
        c = c + fd[loc]
        fd[loc] = 0

    return(c)

def nearby_carrots(f, l):
    for nl in nearby_locs(f, l):
        if f[nl] != 0: return(True)
    return(False)

def nearby_locs(f, l):
    n, m = f.shape
    nds = None

    # first, corners
    if l == (0, 0):
        nds = [(0, 1), (1, 0)]
    elif l == (n-1, 0):
        nds = [(n-1, 1), (n-2, 0)]
    elif l == (0, m-1):
        nds = [(0, m-2), (1, m-1)]
    elif l == (n-1, m-1):
        nds = [(n-2, m-1), (n-1, m-2)]

    # next, edges
    elif l[0] == 0: # top
        nds = [(0, l[1]-1), (0, l[1]+1), (1, l[1])]
    elif l[0] == n-1: # bottom
        nds = [(0, l[1]-1), (0, l[1]+1), (n-2, l[1])]
    elif l[1] == 0: # left
        nds = [(l[0], 1), (l[0]-1, 0), (l[0]+1, 0)]
    elif l[1] == m-1: # right
        nds = [(l[0], m-2), (l[0]-1, m-1), (l[0]+1, m-1)]

    # finally, an internal point
    else:
        nds = [
                (l[0], l[1]-1),
                (l[0], l[1]+1),
                (l[0]+1, l[1]),
                (l[0]-1, l[1])
            ]


    if nds == None: raise Exception("You missed a case in nearby_carrots")

    return(nds)

def next_dir(f, l):
    max_carrot = 0
    result_dir = STOP

    for nd in nearby_locs(f, l):
        if f[nd] > max_carrot:
            result_dir = nd
            max_carrot = f[nd]

    return(result_dir)

if __name__ == "__main__":
    print("running test 1 with field:")
    print(test_field_1)
    result = bunny(test_field_1, test_start_loc_1)
    print("got: " + str(result))
    if result == test_answ_1:
        print("passed test 1!")
    else:
        print("failed test 1")

### END CODE
