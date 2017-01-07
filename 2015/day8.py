BACKSLASH = "\\"


def parse_input():
    with open('day8.txt') as f:
        return f.read().split()


def parse_line(line):
    code_count = 0
    escaped = False
    hex_flag = False
    hex_count = 0
    # Ignore first and last double quote
    for char in line[1:-1]:
        if escaped is False:
            if char == BACKSLASH:
                # Flip on the escaped char flag
                escaped = True
                continue
            else:
                code_count += 1
        else:
            # We are in an escaped region
            if char == 'x' and hex_flag is False:
                hex_flag = True
            elif char in (BACKSLASH, '"'):
                code_count += 1
                escaped = False
            else:
                hex_count += 1
                if hex_count >= 2:
                    hex_count = 0
                    hex_flag = False
                    escaped = False
                    code_count += 1

    return code_count


def encode(line):
    string = ''
    for char in line:
        if char == BACKSLASH:
            string += '\\\\'
        elif char == '"':
            string += '\\"'
        else:
            string += char

    # return '"\\"' + string + '\\""'
    return '"' + string + '"'


if __name__ == '__main__':
    strings = parse_input()
    final_sum = final_sum2 = 0
    for line in strings:
        new_line = encode(line)
        string_count = len(new_line)
        old_string_count = len(line)
        code_count = parse_line(line)
        final_sum += (string_count - code_count)
        final_sum2 += (string_count - old_string_count)

    print 'part 1: ', final_sum
    print 'part 2: ', final_sum2
