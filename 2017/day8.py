import re
import utils
from collections import Counter

inp_lines = utils.read_input(8)

registers = Counter()
cur_max = 0
for line in inp_lines:
    reg, command, value, condition = \
            re.match(r'([A-Za-z]+) (inc|dec) ([-]*\d+) if (.+)', line).groups()
    value = int(value)

    check_reg = condition.split(' ')[0]
    reg_value = registers[check_reg]
    condition = condition.replace(check_reg, str(reg_value))

    result = eval(condition)
    if not result:
        continue
    if command == 'inc':
        registers[reg] += value
    else:
        registers[reg] -= value

    cur_max = max(cur_max, registers.most_common(1)[0][1])

print(registers.most_common(1))
print(cur_max)
