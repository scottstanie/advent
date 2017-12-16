import itertools
import re
import numpy as np
import math
import random

from collections import Counter, defaultdict, namedtuple
inp = utils.read_input(16)
dances = [(d[0], d[1:].split('/')) for d in inp]

cat = ''.join
def exchange(mylist, pos1, pos2):
    t = mylist[pos1]
    mylist[pos1] = mylist[pos2]
    mylist[pos2] = t


def partner(mylist, pa, pb):
    i1 = mylist.index(pa)
    i2 = mylist.index(pb)
    mylist[i1] = pb
    mylist[i2] = pa

def spin(mylist, idx):
    mylist = mylist[-idx:] + mylist[:-idx]

def spin(mylist, idx):
    return mylist[-idx:] + mylist[:-idx]

def new_start():
    return list('abcdefghijklmnop')

def run(startlist, dances):
    for instr, others in dances:
        if instr == 's':
            startlist = spin(startlist, int(others[0]))
        elif instr == 'p':
            partner(startlist, *others)
        else:
            exchange(startlist, int(others[0]), int(others[1]))
    return startlist

s = set()
n = new_start()
for idx in range(2000):
    n = run(n, dances)
    if cat(n) in s:
        print(idx)
        break
    s.add(cat(n))


print(1000000000 % 63)

configs = [cat(new_start())]
n = new_start()
for idx in range(64):
    n = run(n, dances)
    configs.append(cat(n))

print(configs[55])
