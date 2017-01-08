import json
import re


def parse_input():
    with open('day12.txt') as f:
        # Part 1: just read string
        # return f.read().strip()
        # Part 2: need json
        return json.loads(f.read())


def is_int(item):
    return isinstance(item, int)


def is_dict(item):
    return isinstance(item, dict)


def is_list(item):
    return isinstance(item, list)


def is_string(item):
    return isinstance(item, basestring)


def recurse(obj):
    if is_int(obj):
        return obj
    elif is_string(obj):
        return 0
    elif is_list(obj):
        return sum(recurse(o) for o in obj)
    elif is_dict:
        if 'red' in obj.values():
            return 0
        else:
            # Numbers won't be in the keys of the dict
            return recurse(obj.values())


if __name__ == '__main__':
    json_string = parse_input()
    tests = [
        ('[1,{"c":"red","b":2},3]', 4),
        ('[1,"red",5]', 6),
        ('[1,2,3]', 6),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
    ]
    # Part 1: no json decoding or searching needed:
    print 'Part 1: ', sum(int(num) for num in re.findall(r'([-]?[\d]+)', str(json_string)))
    for test_inp, val in tests:
        print 'input: ', test_inp
        answer = recurse(json.loads(test_inp))
        print 'returns:  ', answer
        print 'desired answer', val
        print '=' * 20

    print 'Part 2:', recurse(json_string)
