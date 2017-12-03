from itertools import combinations

def powerset(iterable):
    "Yield all subsets of items."
    items = list(iterable)
    for r in range(len(items)+1):
        for c in combinations(items, r):
            yield c

def neighbors4(point):
    "The four neighbors (without diagonals)."
    x, y = point
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1))


def neighbors8(point):
    "The eight neighbors (with diagonals)."
    x, y = point
    print(x)
    print(y)
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1),(x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1))


def read_input(day_num):
    with open('day%s_input.txt' % day_num) as f:
        return f.read().splitlines()


# 2-D points implemented using (x, y) tuples
def X(point): return point[0]
def Y(point): return point[1]
