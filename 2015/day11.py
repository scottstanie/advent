from itertools import groupby


def rule1(password):
    """contains one increasing straight of at least 3"""
    for idx, num in enumerate(password):
        try:
            if password[idx + 1] == num + 1 and password[idx + 2] == num + 2:
                return True
        except IndexError:
            return False


def rule2(password):
    """doesn't contain i, o, or l"""
    return not any(letter == (ord(bad) - ord('a')) for letter in password
                   for bad in ('i', 'o', 'l'))


def rule3(password):
    """contains two different non-overlapping pairs of letters"""
    doubles = 0
    for g in groupby(password):
        if len(list(g[1])) > 1:
            doubles += 1
    return doubles >= 2


def string_to_nums(string):
    return [ord(letter) - ord('a') for letter in string]


def nums_to_string(password):
    return ''.join(chr(num + ord('a')) for num in password)


def inc(num_list, position=0):
    num_for_z = 25
    index = (len(num_list) - 1) - position
    if num_list[index] + 1 <= num_for_z:
        return num_list[:index] + [num_list[index] + 1] + num_list[index + 1:]
    else:
        return inc(num_list[:index] + [0] + num_list[index + 1:], position + 1)


if __name__ == '__main__':
    start = 'cqjxjnds'
    password = string_to_nums(start)
    # password will be a list of numbers from 0-25
    while not rule1(password) or not rule2(password) or not rule3(password):
        password = inc(password)

    print password
    print nums_to_string(password)
