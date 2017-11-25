import numpy as np

def parse_input(test=False):
    with open('day18.txt') as f:
        lines = f.read().splitlines()

    if test:
        lines = test_input().splitlines()
    lines = [list(line.replace('.', '0').replace('#', '1'))
             for line in lines]
    return np.array(lines).astype(np.uint8)


def test_input():
    return """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""


def neighbors(row, col, num_rows, num_cols):
    valid_rows = list(range(max(0, row-1), min(num_rows, row+2)))
    valid_cols = list(range(max(0, col-1), min(num_cols, col+2)))
    all_pairs = set((r, c) for r in valid_rows for c in valid_cols)
    return all_pairs - set([(row, col)])


def corners(grid):
    r, c= grid.shape
    max_r = r-1
    max_c = c-1

    return ((0, 0), (0, max_c), (max_r, 0), (max_r, max_c))


def flick_light(grid, new_grid, row, col):
    if grid[row, col]:
        new_grid[row, col] = test_on(grid, row, col)
    else:
        new_grid[row, col] = test_off(grid, row, col)


def neighbors_on(grid, row, col):
    test_idxs = neighbors(row, col, *grid.shape)
    return sum([grid[r, c] for (r, c) in test_idxs])


def test_on(grid, row, col):
    num_on = neighbors_on(grid, row, col)
    return int(num_on in (2, 3))


def test_off(grid, row, col):
    num_on = neighbors_on(grid, row, col)
    return int(num_on == 3)

def step(grid, new_grid):
    for (r, c) in np.ndindex(grid.shape):
        flick_light(grid, new_grid, r, c)

    # Part two: corners always on
    for (r, c) in corners(grid):
        new_grid[r, c] = 1


if __name__ == '__main__':
    grid = parse_input()
    # Part two starts the corners on
    for (r, c) in corners(grid):
        grid[r, c] = 1
    print(grid)
    for _ in range(100):
        new_grid = np.zeros_like(grid)
        step(grid, new_grid)
        grid = new_grid

    print(np.sum(grid))
