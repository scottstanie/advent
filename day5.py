from itertools import groupby


def main():
    with open('day5.txt', 'rb') as f:
        instructions = f.read().split('\n')
        instructions = [i for i in instructions if len(i) > 1]
        good_strings = [s for s in instructions if cond1(s) and cond2(s)]

        print good_strings
        print len(good_strings)

    return


def cond1(string):
    for idx, letter in enumerate(string):
        try:
            if letter == string[idx + 2]:
                return True
        except IndexError:
            return False
    return False


def cond2(string):
    for idx, letter in enumerate(string):
        try:
            pair = letter + string[idx + 1]
            if pair in string[idx + 2:]:
                return True
        except IndexError:
            return False
    return False

if __name__ == '__main__':
    main()
