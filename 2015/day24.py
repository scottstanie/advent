from itertools import chain, combinations
from operator import mul


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def find_valid_weights(weights, per_sleigh_weight):
    return [s for s in powerset(weights) if sum(s) == per_sleigh_weight]


def quantum_enganglement(group):
    return reduce(mul, group)


def find_winner(valid_weights):
    return sorted(valid_weights, key=lambda group: (len(group), quantum_enganglement(group)))[0]

if __name__ == '__main__':
    weights = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    # Part 1
    winning_group = find_winner(find_valid_weights(weights, sum(weights) / 3))
    print("Part 1: ", quantum_enganglement(winning_group))
    # Part 2
    winning_group = find_winner(find_valid_weights(weights, sum(weights) / 4))
    print("Part 2: ", quantum_enganglement(winning_group))
