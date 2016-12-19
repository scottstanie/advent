import itertools


def parse_input():
    trianges = []
    with open('day3_input.txt') as f:
        for line in f.readlines():
            sides = [int(s) for s in line.split(' ') if s]
            trianges.append(sides)

    return trianges


def parse_part2():
    original_triples = parse_input()
    one_line = []
    for i in (0, 1, 2):
        one_line += [triple[i] for triple in original_triples]

    for i in range(0, len(one_line), 3):
        yield one_line[i: i + 3]


def split_side_pairs(sides):
    indices = (0, 1, 2)
    for index_pairs in itertools.combinations(indices, 2):
        third_side = list(set(indices) - set(index_pairs))[0]
        yield (sides[index_pairs[0]], sides[index_pairs[1]]), sides[third_side]


def figure_triangle(sides):
    # if 156 in sides:
        # import pdb; pdb.set_trace()
    for (first, second), last_side in split_side_pairs(sides):
        if first + second <= last_side:
            return 0

    return 1


if __name__ == '__main__':
    trianges = parse_input()
    total_possible = 0
    for sides in trianges:
        total_possible += figure_triangle(sides)
    print 'part 1: ', total_possible

    total_possible = 0
    for sides in parse_part2():
        print sides
        total_possible += figure_triangle(sides)

    print 'part 2: ', total_possible
