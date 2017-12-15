import numpy as np
import functools
import operator
from itertools import zip_longest


def reduce_256(block256):
    return ''.join(int2hex(dense_hash(block)) for block in grouper(block256, 16))


def grouper(iterable, n, fillvalue=None):
    '''Used to iterate in chunks of size n over iterable'''
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def get_start_list(input_str):
    return np.array([ord(c) for c in input_str] + [17, 31, 73, 47, 23])


def dense_hash(block16):
    return functools.reduce(operator.xor, block16)


def int2hex(integer):
    return "{0:0{1}x}".format(integer, 2)


def rotate(cur_list, idxs):
    cur_list[idxs] = cur_list[idxs[::-1]]


def get_idxs(cur_list, cur_pos, length):
    return [n % len(cur_list) for n in range(cur_pos, cur_pos + length)]


def knot_hash(input_str):
    length_arr = get_start_list(input_str)
    cur_list = np.arange(0, 256)
    cur_pos = 0
    cur_skip = 0
    for _ in range(64):  # rounds
        for length in length_arr:
            idxs = get_idxs(cur_list, cur_pos, length)
            rotate(cur_list, idxs)
            cur_pos = (cur_pos + length + cur_skip) % len(cur_list)
            cur_skip += 1

    return reduce_256(cur_list)

if __name__ == '__main__':
    input_str = "183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88"
    # input_str = "3,4,1,5"  # testing
    length_arr = [int(a) for a in input_str.split(',')]

    cur_list = np.arange(0, 256)
    # cur_list = np.arange(0, 5)
    cur_pos = 0
    cur_skip = 0

    for length in length_arr:
        idxs = get_idxs(cur_list, cur_pos, length)
        rotate(cur_list, idxs)
        cur_pos = (cur_pos + length + cur_skip) % len(cur_list)
        cur_skip += 1

    print("Part 1:")
    print(cur_list)
    print(cur_list[0] * cur_list[1])

    print("Part 2:")
    print(knot_hash(input_str))
