# Author: Eric Kalosa-Kenyon
# Date: August 15, 2018
#
# This script encodes functions and tests for a greedy graph algorithm framed as
# a bunny in a field eating carrots. The bunny eats carrots at the current
# location, looks around, determines which adjacent 

### BEGIN CODE
import numpy as np

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

    Notes:
    Todo:
        1. check inputs for type soundness - right now this relies on user to
            provide correct types.
        2. check that field has only non-negative integer elements
    """

    c = 0 # carrot counter aka the bunny belly
    fd = field.copy() # retain the original input for debugging
    loc = start_loc

    while(nearby_carrots(fd, loc)): # until there are no carrots near the bunny
        nd = next_dir(fd, loc) # find the adjacency with most carrots
        if nd == STOP: # if there are no nearby carrots, quit
            break
        loc[0] = loc[0] + nd[0] # update location with the next direction
        loc[1] = loc[1] + nd[1]

        # eat that carrot!
        c = c + fd[loc]
        fd[loc] = 0

    return(c)

def nearby_carrots(f, l):
    # TODO
    return(False)

def next_dir(f, l):
    return(STOP)

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
