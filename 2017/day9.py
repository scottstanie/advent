import re


def clean_string(s):
    s = s.replace('!!', '')
    return re.sub(r'!.', '', s)


def count_groups(s):
    if not s:
        return 0
    garbage = False
    total = 0
    score = 0
    garb_count = 0
    for char in s:
        if char == '>':
            garbage = False
            continue
        if garbage:
            garb_count += 1
            continue
        if char == '{':
            score += 1
        elif char == '<':
            garbage = True
        elif char == '}':
            total += score
            score -= 1
    return total, garb_count


inp = open('day9_input.txt').read().strip()
count_groups(clean_string(inp))
