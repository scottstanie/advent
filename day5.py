from itertools import groupby
from collections import Counter


def at_least_3_vowels(string):
    vowels = 'aeiou'
    letter_counts = Counter(string)
    return sum(letter_counts[v] for v in vowels) >= 3


def contains_double_letter(string):
    for g in groupby(string):
        if len(list(g[1])) > 1:
            return True
    return False


def no_bad_strings(string):
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    return all(b not in string for b in bad_strings)


def contains_sandwich(string):
    for idx, letter in enumerate(string):
        try:
            if letter == string[idx + 2]:
                return True
        except IndexError:
            return False
    return False


def contains_two_pair(string):
    for idx, letter in enumerate(string):
        try:
            pair = letter + string[idx + 1]
            if pair in string[idx + 2:]:
                return True
        except IndexError:
            return False
    return False


def main():
    with open('day5.txt', 'rb') as f:
        instructions = f.read().split('\n')
        # Get rid of new lines/ blank lines
        instructions = [i for i in instructions if len(i) > 1]

        print "Part 1 number of good strings:"
        good_strings = [s for s in instructions if at_least_3_vowels(s) and
                        contains_double_letter(s) and no_bad_strings(s)]
        # print good_strings
        print len(good_strings)

        good_strings = [s for s in instructions if contains_sandwich(s) and contains_two_pair(s)]
        print "Part 2 number of good strings:"
        # print good_strings
        print len(good_strings)


if __name__ == '__main__':
    main()
