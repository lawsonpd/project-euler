# INCOMPLETE

#### Problem:
# Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

# Consider the following two triangles:

# A(-340,495), B(-153,-910), C(835,-947)

# X(-175,41), Y(-421,-714), Z(574,-645)

# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
####

# I assume that the set of points "contained" in the triangle is inclusive with respect
# to the lines that form the sides of the triangle.

import math
import itertools

def slope(p1: tuple, p2: tuple) -> float:
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def linear_fn(p1: tuple, p2: tuple):
    '''
    Return function for calculating y = mx + b
    '''
    slope_ = slope(p1, p2)
    def f(x: float) -> float:
        x1 = p1[0]
        y1 = p1[1]
        return (slope_ * x) - (slope_ * x1) + y1
    return f

def in_same_quadrant(p1: tuple, p2: tuple) -> bool:
    x_sum_abs = abs(p1[0] + p2[0]) # Abs value of sum of x-coords
    y_sum_abs = abs(p1[1] + p2[1]) # Abs value of sum of y-coords

    # If points are in different quadrants along an axis,
    # then one of the coords will be negative and the sum will
    # be less than the max (the positive) of the two coords.
    # Just need this to be true of either the x- or y-coords.
    # If this condition doesn't hold for either set, then
    # the poits are in the same quadrant.
    if x_sum_abs < max(p1[0], p2[0]) or y_sum_abs < max(p1[1], p2[1]):
        return False
    else:
        return True

points = [(-1.0,7.0), (4.0,7.0), (-1.0,-6.0)]

lines = map(linear_fn, itertools.combinations(points, 2))

def is_between(x: tuple, pts: tuple) -> bool:
    '''
    This is primarily for determining whether the slope of the "naught line" (i.e.
    the line that passes through the point given and the origin) is between that 
    of two other lines.
    '''
    naught_slope_x = slope(x, (0,0))
    naught_slope_a = slope(pts[0], (0,0))
    naught_slope_b = slope(pts[1], (0,0))

    if (naught_slope_x <= naught_slope_a and naught_slope_x >= naught_slope_b) or \
       (naught_slope_x >= naught_slope_a and naught_slope_x <= naught_slope_b):
        return True
    else:
        return False

def euc_dist(point1:tuple, point2:tuple) -> float:
    '''
    For use with itertools.combinations, points is to be given as a tuple
    of two tuples each representing a point.
    '''
    return round( math.sqrt( (point2[1] - point1[1])**2 + (point2[0] - point1[0])**2 ), 5)

def polygon_height(polygon:tuple) -> float:
    '''
    Return "height" (distance from top vertex to baseline).
    NOTE: Assumes polygon has one side that's parallel to the x-axis.
    '''
    return max(polygon, key=lambda p: p[1])[1] - min(polygon, key=lambda p: p[1])[1]

def special_dist(polygon:tuple, point:tuple) -> bool:
    '''
    Determines whether a point is less than D distance from
    all vertices in polygon, where D is shortest distance
    across the polygon.
    '''
    d = polygon_height(polygon)
    for vertex in polygon:
        if euc_dist(point, vertex) > d:
            return False
    return True

def gamma(a:float, b:float, c:float):
    '''
    Returns angle given three points using law of cosines.
    '''
    return round(math.degrees(math.acos( (a**2 + b**2 - c**2) / (2 * a * b) )), 5)

def gamma_ext(points:tuple):
    '''
    Find gamma (as in `gamma` above) for an n-sided polygon.
    '''
    pass

def is_contained(triangle:tuple, test_point:tuple=(0,0)) -> bool:
    '''
    
    '''
    dists_to_origin = [euc_dist(vertex, test_point) for vertex in triangle]
    side_lengths = [euc_dist(p1, p2) for p1, p2 in itertools.combinations(triangle, 2)]
    inner_side_pairs = list(itertools.combinations(dists_to_origin, 2))
    inner_triangles = [inner_side_pairs[i] + (side_lengths[i],) for i in range(3)]
    
    # sum_of_angles = 0.0
    # for t in inner_triangles:
    #     angle = gamma(t[0], t[1], t[2])
    #     sum_of_angles += angle
    sum_of_angles = round(sum([gamma(t[0], t[1], t[2]) for t in inner_triangles]), 2)

    if sum_of_angles == 360:
        return True
    else:
        return False

def main():
    with open('p102_triangles.txt', 'r') as f:
        n = 0
        for line in f.readlines():
            coords = list(map(int, line.split(',')))
            vertices = tuple([(coords[i], coords[i+1]) for i in range(0, len(coords), 2)])
            print(f'Vertices: {vertices}')
            if is_contained(vertices):
                n += 1
    print(n)

def test():
    # test_triangle = ((2, 4), (0, -4), (-2, 0))
    # test_triangle = ((-340,495), (-153,-910), (835,-947)) # From PE; DOES contain origin
    # test_triangle = ((-175,41), (-421,-714), (575,-645)) # From PE; does NOT contain origin
    test_triangle = ((603/2,430/2),(598/2,585/2),(168/2,699/2))
    dists_to_origin = [euc_dist(vertex, (0,0)) for vertex in test_triangle]
    side_lengths = [euc_dist(p1, p2) for p1, p2 in itertools.combinations(test_triangle, 2)]
    inner_side_pairs = list(itertools.combinations(dists_to_origin, 2))
    print(dists_to_origin)
    print(side_lengths)
    print(inner_side_pairs)
    print([inner_side_pairs[i] + (side_lengths[i],) for i in range(3)])
    print(is_contained(test_triangle, (210, 290)))

if __name__ == '__main__':
    # test()
    main()
