import numpy as np

with open('day1_input.txt') as f:
    commands = [l.strip('\n ') for l in f.read().split(',')]


def parse_command(command):
    # Returns (Letter, number of squares to move)
    return command[0], int(command[1:])


# Starting north, turning right
directions = [np.array(c) for c in ((0, 1), (1, 0), (0, -1), (-1, 0))]

current_direction_idx = 0
total = np.array([0, 0])
for command in commands:
    letter, number = parse_command(command)
    if letter == 'R':
        current_direction_idx += 1
    else:
        current_direction_idx -= 1
    current_direction_idx %= 4
    # import pdb; pdb.set_trace()
    new_move = number * directions[current_direction_idx]
    total += new_move

print total
print abs(total[0]) + abs(total[1])


current_direction_idx = 0
total = np.array([0, 0])
visited = set(total)
for command in commands:
    letter, number = parse_command(command)
    if letter == 'R':
        current_direction_idx += 1
    else:
        current_direction_idx -= 1
    current_direction_idx %= 4

    direction = directions[current_direction_idx]

    # The squares for this move are between the last stop,
    # and the last stop + new_move
    squares_visited = [total + (i * direction) for i in range(1, number + 1)]

    for square in squares_visited:
        if tuple(square) in visited:
            print 'Found! visited: ', square
            print squares_visited
            sys.exit()
            break
        else:
            visited.add(tuple(square))
    # total += squares_visited[-1]
    new_move = number * directions[current_direction_idx]
    total += new_move
