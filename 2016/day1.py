import numpy as np

with open('day1_input.txt') as f:
    commands = [l.strip('\n ') for l in f.read().split(',')]

# Starting north, turning right
dirs = [np.array(c) for c in ((0, 1), (1, 0), (0, -1), (-1, 0))]
cur_idx = 0
total = np.array([0, 0])
for command in commands:
    letter = command[0]
    if letter == 'R':
        cur_idx += 1
    else:
        cur_idx -= 1
    cur_idx %= 4
    number = int(command[1:])
    total += number * dirs[cur_idx]

print total
print abs(total[0]) + abs(total[1])
