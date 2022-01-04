# INCOMPLETE

#### Problem:

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
####

def test_same_nums(n):
    for m in range(2,7):
        x = m * n
        if len(str(x)) != len(str(n)):
            return False
        for i in str(n):
            if not i in str(m):
                return False
    return True

def find():
    answer = None
    n = 1
    while answer == None:
        if test_same_nums(n):
            answer = n
        n += 1
    return answer
