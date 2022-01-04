#### Problem:
# Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

# Consider the following two triangles:

# A(-340,495), B(-153,-910), C(835,-947)

# X(-175,41), Y(-421,-714), Z(574,-645)

# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
####

# I assume that the set of points "contained" in the triangle is inclusive with respect
# to the lines that form the sides of the triangle.

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

from itertools import combinations

points = [(-1.0,7.0), (4.0,7.0), (-1.0,-6.0)]

lines = map(linear_fn, combinations(points, 2))

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

def main():
    test_points = [(-2,2), (2,2), (4, -2)]
    