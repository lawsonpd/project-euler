####
# Starting in the top left corner of a 2×2 grid, and only being able to move to the 
# right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
####

def count_paths(n, m, cache={}):
    if (n,m) in cache:
        return cache[(n,m)]
    elif n == 0 or m == 0:
        return 1
    else:
        cache[(n,m)] = count_paths(n-1, m) + count_paths(n, m-1)
        return cache[(n,m)]

####
# Explanation:
# Let's use P(N) to denote the number of paths to a given node. At the start,
# I thought that a brute force solution may be cumbersome, and thought that
# it may be possible to find a function for P(N) that computes a formula
# based on the number of vertices in the lattice, the position of a node
# in the lattice, etc. But after the simple observation that
# P(n,m) == P(n-1, m) + P(n, m-1), it seemed the simplest method would be
# to recursively add the paths of the path-neighbors of the input node.

# For an explanation of why the memoization above works, and why the memo
# does not need to be passed to `count_paths` in the calls on line 13,
# see https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument

import time

if __name__ == '__main__':
    tick = time.time()
    count = count_paths(25,25)
    tock = time.time()
    elapsed = tock - tick
    print(f"{count} found in {elapsed} seconds")

# 126410606437752 found in 0.0013151168823242188 seconds
