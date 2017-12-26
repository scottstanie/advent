import utils

inp = utils.read_input(24)
testinp = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""".splitlines()


def parse_input(inp):
    return [tuple(map(int, line.split('/'))) for line in inp]


def possible(domino):
    return [domino, (domino[1], domino[0])]


def score(domino_list):
    return sum((dom[0] + dom[1]) for dom in domino_list)


def last_entry(domino_list):
    return domino_list[-1][1]


def find_chains(cur_list, dominos_to_pick):
    if not dominos_to_pick:
        # Give the length as well as the list for part 2
        yield len(cur_list), cur_list
    else:
        for domino in dominos_to_pick:
            idx = dominos_to_pick.index(domino)
            remaining = dominos_to_pick[:idx] + dominos_to_pick[idx + 1:]
            for dom in possible(domino):
                if last_entry == dom[0]:
                    new_list = [*cur_list, dom]
                    yield len(new_list), new_list
                    yield from find_chains(new_list, remaining)


if __name__ == '__main__':
    dominos = parse_input(testinp)
    dominos = parse_input(inp)
    starts = [d_flip for domino in dominos for d_flip in possible(domino) if not d_flip[0]]

    for start in starts:
        idx = dominos.index(start)
        rest = dominos[:idx] + dominos[idx + 1:]
        print(start, rest)

        # Part 1
        # print(max(score(chain) for length, chain in find_chains([start], rest)))

        # Part 2
        print(max((length, score(chain)) for length, chain in find_chains([start], rest)))
