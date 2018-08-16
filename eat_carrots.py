# Author: Eric Kalosa-Kenyon
#

### BEGIN CODE
import numpy as np

fd = np.array([])

test_1 = [[5, 7, 8, 6, 3],
            [0, 0, 7, 0, 4],
            [4, 6, 3, 4, 9],
            [3, 1, 0, 5, 8]]

def bunny(field, start_loc):
    """Take a 2D np.array <field> and a tuple of integers <start_loc> and
    perform the bunny algorithm, returning a tuple containing the end state of
    the field (np.array, 2D) and the number of carrots the bunny has eaten (int)

    Args:
        field (2D np.array of int) : field of carrots, number of carrots at a
            location indexed by (i,j) represented by the integer in each cell
            e.g.  the number of carrots at (i, j) is field[i, j].
        start_loc (tuple of int) :

    Returns:
        field_end (2D np.array of int) : field of carrots after the bunny has
            eaten his greedy fill.
        num_carrots (int) : number of carrots the bunny has eaten by the end.
    """


### END CODE
