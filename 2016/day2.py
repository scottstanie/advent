import numpy as np


def parse_input():
    with open('day2_input.txt') as f:
        return [line.strip('\n') for line in f.readlines()]


def map_dir(direction):
    dir_map = {
        'U': np.array((0, 1)),
        'D': np.array((0, -1)),
        'L': np.array((-1, 0)),
        'R': np.array((1, 0)),
    }
    return dir_map[direction]


def new_position(position, move):
    position += move
    position = np.maximum(position, np.array((-1, -1)))
    position = np.minimum(position, np.array((1, 1)))
    return position


def new_position2(position, move):

    if abs(sum(np.absolute(position + move))) > 2:
        return position
    else:
        return position + move


def number_map2(position):
    number_map = {
        (0, 2): 1,
        (-1, 1): 2, (0, 1): 3, (1, 1): 4,
        (-2, 0): 5, (-1, 0): 6, (0, 0): 7, (1, 0): 8, (2, 0): 9,
        (-1, -1): 'A', (0, -1): 'B', (1, -1): 'C',
        (0, -2): 'D'
    }
    return number_map[tuple(position)]


def number_map(position):
    number_map = {
        (-1, 1): 1, (0, 1): 2, (1, 1): 3,
        (0, -1): 4, (0, 0): 5, (1, 0): 6,
        (-1, -1): 7, (0, -1): 8, (1, -1): 9
    }
    return number_map[tuple(position)]

if __name__ == '__main__':
    commands = parse_input()
    position = np.array((-2, 0))
    positions = []
    for command in commands:
        for direction in command:
            move = map_dir(direction)
            position = new_position2(position, move)
        print position
        positions.append(number_map2(position))
    print positions
