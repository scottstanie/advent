import re
import utils

def test_input():
    return """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""


def parse_input():
    node_dict = {}
    # for line in test_input().splitlines():
    for line in utils.read_input(12):
        start, others = re.match(r'([\d]*) <-> (.*)', line).groups()
        nums = [int(n.strip()) for n in others.split(',')]
        node_dict[int(start)] = nums

    return node_dict


def visit_nodes(start, visited, node_dict):
    visited.add(start)
    for n in node_dict[start]:
        if n not in visited:
            visit_nodes(n, visited, node_dict)

if __name__ == '__main__':
    node_dict = parse_input()
    visited = set()
    # group0 = set()
    num_groups = 2000   # From input
    # num_groups = 7
    visit_nodes(0, visited, node_dict)
    print('part 1:')
    print(len(visited))

    visited = []  # list of sets
    for n in range(num_groups):
        if not any(n in v_set for v_set in visited):
            new_set = set()
            visit_nodes(n, new_set, node_dict)
            visited.append(new_set)

    print(len(visited))


