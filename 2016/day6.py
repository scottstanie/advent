from collections import Counter, defaultdict

def parse_input():
    letters = defaultdict(Counter)
    with open('day6_input.txt') as f:
        for line in f.read().splitlines():
            for idx, letter in enumerate(line):
                letters[idx][letter] += 1

    return letters


if __name__ == '__main__':
    letters = parse_input()
    print letters
    for counter in letters.values():
        print counter.most_common(1)[0][0]
        print counter.most_common()[-1][0]
