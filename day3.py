import sys


def main(part):
    x, y = 0, 0
    if part == '2':
        x2, y2 = 0, 0

    visited = [(x, y)]
    with open('day3.txt', 'rb') as f:
        instructions = f.readline()
        for idx, direction in enumerate(instructions):
            if part == '1':
                x, y = part1(direction, x, y)
                visited.append((x, y))
            else:
                x, y, x2, y2 = part2(direction, idx, x, y, x2, y2)
                visited.append((x, y))
                visited.append((x2, y2))

        print 'Total unique houses: ', len(set(visited))

    return


def part2(direction, idx, x, y, x2, y2):
    if idx % 2 == 0:
        if direction == '>':
            x += 1
        if direction == '<':
            x -= 1
        if direction == '^':
            y += 1
        if direction == 'v':
            y -= 1
    else:
        if direction == '>':
            x2 += 1
        if direction == '<':
            x2 -= 1
        if direction == '^':
            y2 += 1
        if direction == 'v':
            y2 -= 1

    return x, y, x2, y2


def part1(direction, x, y):
    if direction == '>':
        x += 1
    if direction == '<':
        x -= 1
    if direction == '^':
        y += 1
    if direction == 'v':
        y -= 1
    return x, y


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ['1', '2']:
        print "Argument required: '1' or '2' to specify part 1 or part 2"
        sys.exit(1)

    part = sys.argv[1]
    main(part)
