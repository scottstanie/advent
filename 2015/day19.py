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
    search_str, replace_with = rule
    strings = []
    for occurrence in re.finditer(search_str, text_input):
        start, end = occurrence.start(), occurrence.end()
        new_string = text_input[:start] + replace_with + text_input[end:]
        strings.append(new_string)

    return strings


def build_string(cur_string, steps, rules, target_string):
    # Check for recursion termination
    if cur_string == target_string:
        print('FOUND!')
        print('%s steps taken' % steps)
        print(cur_string)
        return None  # Return none to end the search
    elif len(cur_string) >= len(target_string):
        return None

    for rule in rules:
        for new_string in run_rule(rule, cur_string):
            build_string(new_string,
                         steps + 1,
                         rules,
                         target_string)


def make_rule_dict(rules):
    # Reverse the keys and vals, go from finish to start
    return {end[::-1]: start[::-1] for (start, end) in rules}


def replace_one(whole_string, rule_dict):
    pat = '|'.join(rule_dict.keys())
    repl_func = lambda x: rule_dict[x.group()]
    # Replace the first match with the value from rule_dict
    return re.sub(pat, repl_func, whole_string, 1)

if __name__ == '__main__':
    rules, text_input = parse_input()
    # Test input
    all_strings = []
    # for rule in rules:
    #     all_strings.extend(run_rule(rule, text_input))

    # print len(set(all_strings))

    # rules = [('e', 'H'), ('e', 'O'), ('H', 'HO'), ('H', "OH"), ("O", "HH")]
    # target_string = 'HOHOHO'
    target_string = text_input
    starting_step = 0
    start_string = 'e'
    max_length = len(target_string)
    # import pdb; pdb.set_trace()
    # build_string(start_string,
    #              starting_step,
    #              rules,
    #              target_string)

    # Part 2 (somehow)
    rule_dict = make_rule_dict(rules)
    count = 0
    whole_string = target_string[::-1]
    while whole_string != 'e':
        whole_string = replace_one(whole_string, rule_dict)
        count += 1
    print(count)
