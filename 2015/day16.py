import re

truth_data = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

if __name__ == '__main__':
    with open('day16.txt') as f:
        lines = f.read().splitlines()
        # Sample:
        # Sue 4: goldfish: 10, akitas: 2, perfumes: 9
        regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
        table = []
        for line in lines:
            for sue_num, att1, val1, att2, val2, att3, val3 in re.findall(regex, line):
                    table.append([sue_num, {att1: int(val1), att2: int(val2), att3: int(val3)}])

        for aunt, aunt_data in table:
            # if all((truth_data[k] == v for k, v in aunt_data.items())):  # Part 1
            checks = []
            for k, v in aunt_data.items():
                if k in ('cats', 'trees'):
                    checks.append(v > truth_data[k])
                elif k in ('pomeranians', 'goldfish'):
                    checks.append(v < truth_data[k])
                else:
                    checks.append(v == truth_data[k])

            if all(checks):
                print 'Sue', aunt, aunt_data
