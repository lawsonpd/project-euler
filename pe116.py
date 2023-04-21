# A row of five grey square tiles is to have a number of its tiles 
# replaced with coloured oblong tiles chosen from red (length two), 
# green (length three), or blue (length four).

# Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 
# ways of replacing the grey tiles in a row measuring five units in length.

# How many different ways can the grey tiles in a row measuring 
# fifty units in length be replaced if colours cannot be mixed and 
# at least one coloured tile must be used?

def tiles_mono(l, m, cache={}):
    '''
    @param l length of grey tile slots
    @param m length of color tile
    '''
    if l < m: return 0
    elif l == m: return 1
    else:
        count = cache.get(l, None)
        if not count:
            count = 1 + tiles_mono(l-1, m) + tiles_mono(l-m, m)
            cache[l] = count
            # print(f'Set cache of l={l}')
            # print(f'Count={count}\n')
        return count

def tiles_poly(l, ms):
    '''
    NOTE: tiles_mono memo remains during each of these calls,
    so the result is actually (a + b + c) + (b + c) + c,
    where those represent the sum for tiles_mono(a, m).
    '''
    return sum([tiles_mono(l, m) for m in ms])

# print(tiles_poly(5,[2, 3, 4]))
print(tiles_mono(50, 4))
