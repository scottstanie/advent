import re


def parse_input():
    def _process_rule(line):
        inp, _, out = line.split(' ')
        return inp, out

    rules = []
    with open('day19.txt') as f:
        for line in f.read().splitlines():
            if '=' in line:
                rules.append(_process_rule(line))
            elif line:
                text_input = line

    return rules, text_input


def run_rule(rule, text_input):
    find, replace_with = rule
    strings = []
    for occurrence in re.finditer(find, text_input):
        start, end = occurrence.start(), occurrence.end()
        new_string = text_input[:start] + replace_with + text_input[end:]
        strings.append(new_string)

    return strings

if __name__ == '__main__':
    rules, text_input = parse_input()
    all_strings = []
    for rule in rules:
        all_strings.extend(run_rule(rule, text_input))

    print len(set(all_strings))
