def main():
    with open('day3.txt', 'rb') as f:
        x, x2 = 0, 0
        y, y2 = 0, 0
        visited = [(x, y)]
        instructions = f.read()
        for idx, dir_ in enumerate(instructions):
            # x, y = part1(dir_, x, y)
            x, y, x2, y2 = part2(dir_, idx, x, y, x2, y2)
            visited.append((x, y))
            visited.append((x2, y2))

        print 'Total unique houses: ', len(set(visited))

    return


def part2(dir_, idx, x, y, x2, y2):
    if idx % 2 == 0:
        if dir_ == '>':
            x += 1
        if dir_ == '<':
            x -= 1
        if dir_ == '^':
            y += 1
        if dir_ == 'v':
            y -= 1
    else:
        if dir_ == '>':
            x2 += 1
        if dir_ == '<':
            x2 -= 1
        if dir_ == '^':
            y2 += 1
        if dir_ == 'v':
            y2 -= 1

    return x, y, x2, y2


def part1(dir_, x, y):
    if dir_ == '>':
        x += 1
    if dir_ == '<':
        x -= 1
    if dir_ == '^':
        y += 1
    if dir_ == 'v':
        y -= 1
    return x, y

if __name__ == '__main__':
    main()
