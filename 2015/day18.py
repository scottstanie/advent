import numpy as np

def parse_input(test=False):
    with open('day18.txt') as f:
        lines = f.read().splitlines()

    if test:
        lines = test_input().splitlines()
    lines = [list(line.replace('.', '0').replace('#', '1'))
             for line in lines]
    lights = np.array(lines).astype(np.uint8)
    return np.pad(lights, 1, 'constant', constant_values=(0,0))


def test_input():
    return """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""


def neighbors(row, col, num_rows, num_cols):
    # With padding, don't have to check bounds
    return {(row-1, col-1), (row-1, col), (row-1, col+1),
     (row, col-1),                  (row, col+1),
     (row+1, col-1), (row+1, col), (row+1, col+1)}


def corners(grid):
    # would be ((0, 0), (0, -1), (-1, 0), (-1, -1)), but zero padded
    return ((1, 1), (1, -2), (-2, 1), (-2, -2))


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
    for r in range(1, grid.shape[0]-1):
        for c in range(1, grid.shape[1]-1):
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
