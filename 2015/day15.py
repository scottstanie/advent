import itertools
import numpy as np


def parse_input(input_lines):
    lines = input_lines.split('\n')
    flavor_data = []
    for line in lines:
        name, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.strip().split(' ')
        flavor_data.append([
            int(capacity.strip(',')),
            int(durability.strip(',')),
            int(flavor.strip(',')),
            int(texture.strip(',')),
            int(calories.strip(','))  # Part 1: leave calories out
        ])
    print 'flavor data:'
    print np.matrix(flavor_data)
    return np.matrix(flavor_data)


def total_score(flavor_combo, flavor_data):
    w = np.matmul(flavor_combo, flavor_data[:, :-1])
    cals = np.matmul(flavor_combo, flavor_data[:, -1])  # Last column weighted sum
    if np.min(w) <= 0 or cals != 500:  # Part 1: leave out 500 cal constraint
        return 0
    return np.prod(w)


def all_teaspoon_combos(num_flavors):
    return (np.matrix(comb) for comb in itertools.product(range(101), repeat=num_flavors)
            if sum(comb) == 100)


def best_combo(all_combos, flavor_data):
    return max(all_combos, key=lambda x: total_score(x, flavor_data))

if __name__ == '__main__':
    inp = """Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
    PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
    Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
    Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8"""

    # Test input:
    # inp = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
    # Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
    flavor_data = parse_input(inp)
    all_combos = all_teaspoon_combos(len(flavor_data))
    best = best_combo(all_combos, flavor_data)
    print 'total score: ', total_score(best, flavor_data)
    print best
