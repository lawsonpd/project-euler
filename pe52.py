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
