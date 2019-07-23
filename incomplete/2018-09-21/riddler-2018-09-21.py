# https://fivethirtyeight.com/features/two-paths-diverged-in-a-city-and-i-i-took-the-block-less-traveled-by/

# 5 blocks west and 10 blocks north
# how many possible paths?

# assuming the shortest-length path is always taken,
# a route can be represented by 15 different choices - north or east
# with 1 for north and 0 for east, one simple path (10 north then 5 east)
# can be represented by 11111 11111 00000
# where the sum of the route MUST == 10

import itertools as it
import numpy as np

# generate correct routes
all_routes = ['{0:015b}'.format(x) for x in range(2 ** 15)]
all_routes_lengthisok = [x.count('1') == 10 for x in all_routes]
correct_routes = list(it.compress(all_routes, all_routes_lengthisok))

# turn routes into 10 x 5 matrix
input1 = '011001100111111'

def gridmap(input_string, num_rows, num_cols):

    # parse input
    input_list = [int(x) for x in list(input_string)]

    # generate 10 x 5 matrix
    grid = np.zeros(shape = (num_rows, num_cols))
    x = 0
    y = 0

    # loop over input
    for i in range(len(input_list)):
        if input_list[i]:
            grid[x + 1][y] = 9
            x += 1
        else:
            grid[x][y + 1] = 9
            y += 1

    print(grid)

gridmap(input1, 11, 6)









        #
