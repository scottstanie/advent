import hashlib
import sys


def find_zeros(seed):
    print 'DECRYPTING...'
    idx = 0
    while True:
        hashed = hashlib.md5('%s%s' % (seed, idx)).hexdigest()
        if all(d == '0' for d in hashed[:5]):
            print 'hashed: ', hashed, 'idx: ', idx
            yield hashed
        idx += 1


def part1(seed):
    password = ''
    hash_generator = find_zeros(seed)
    while len(password) < 8:
        hashed = hash_generator.next()
        password += hashed[5]

    print password


def part2(seed):
    password = '_' * 8
    hash_generator = find_zeros(seed)
    while '_' in password:
        hashed = hash_generator.next()
        position, value = hashed[5:7]
        if ord(position) > ord('7') or password[int(position)] != '_':
            continue
        password = password[:int(position)] + value + password[int(position) + 1:]
        print password


if __name__ == '__main__':
    try:
        seed = open('day5_input.txt').read().strip('\n')
    except IOError:
        seed = 'abc'

    if sys.argv[1] == '1':
        part1(seed)
    elif sys.argv[1] == '2':
        part2(seed)
    else:
        print "Usage: python part4.py [1 or 2]"
        sys.exit(1)
