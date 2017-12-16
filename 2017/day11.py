import utils
from collections import Counter


def east(stepcount):
    return (stepcount['ne'] - stepcount['sw']) + (stepcount['se'] - stepcount['nw'])


if __name__ == '__main__':
    inp = utils.read_input(11)
    steps=inp[0].split(',')
    stepcount = Counter(steps)

    print('north/south dist away:')
    print(stepcount['n'] - stepcount['s'])
    eastdist = 366 + 284
    # I guess this is the answer...
    # north/south is less, so only east matters
    print(eastdist)

    maxfar = 0
    for idx in range(len(steps)):
        maxfar = max(east(Counter(steps[:idx])), maxfar)
    print(maxfar)
