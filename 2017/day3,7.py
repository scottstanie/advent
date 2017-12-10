
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import re
import math
import requests

from collections import Counter, defaultdict, namedtuple, deque
from itertools   import permutations, combinations, chain, cycle, product, islice
from utils import read_input, powerset, neighbors4, neighbors8, X, Y



number = 368078
sz = math.ceil(math.sqrt(number))
print(sz)
grid = np.zeros((sz, sz))


start = sz//2 + 1
start


((607**2 - 368078) - 304) + 304  # answer!



#part 2
row = 304
col = 304
num = 1
grid = np.zeros((607, 607))
grid[row, col] = num
col += 1

dirs = cycle(('right','up', 'left','down'))
curdir = next(dirs)
while num < number:
    num = 0

    print(row, col)
    for r, c in neighbors8((row, col)):
       num += grid[r, c]

    print(num, curdir)
    grid[row, col] = num

    if curdir == 'right':
        if grid[row + 1, col] == 0:
            curdir = next(dirs)
            row += 1
        else:
            col += 1
    elif curdir == 'up':
        # check left
        if grid[row, col - 1] == 0:
            curdir = next(dirs)
            col -= 1
        else:
            row += 1
    elif curdir == 'left':
        # check down
        if grid[row - 1, col] == 0:
            curdir = next(dirs)
            row -= 1
        else:
            col -= 1
    elif curdir == 'down':
        # check right
        if grid[row, col + 1] == 0:
            curdir = next(dirs)
            col += 1
        else:
            row -= 1
    print('----')

print(num)


# ## Day 6

# In[44]:


banks = [int(n) for n in "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11".split()]
# banks = [0,2,7,0]
n_banks = len(banks)
configs = set()
cur_config = tuple(banks)
cur_config
count = 0
print(cur_config)
loop_ctr = 0
loop_start = False
while cur_config not in configs:
#     if cur_config == (2,4,1,2):
    if cur_config == (1, 0, 14, 14, 12, 12, 10, 10, 8, 8, 6, 6, 4, 3, 2, 1):
        loop_start = True

    if loop_start:
        loop_ctr += 1
    configs.add(cur_config)
    dist_idx = cur_config.index(max(cur_config))
    num_banks = cur_config[dist_idx]

    banks[dist_idx] = 0

    while num_banks > 0:
        dist_idx = (dist_idx + 1) % n_banks
#         if dist_idx == dist_idx:
#             continue
        banks[dist_idx] += 1
        num_banks -= 1

    count += 1
    cur_config = tuple(banks)
#     print(cur_config)


print(count)
print(loop_ctr)


# ## Day 8

# In[24]:


inp = read_input(7)
inp = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
words = Counter()
for line in inp:
    try:
        before, after = line.split(' -> ')
    except:
        before = line.split(' -> ')[0]
        after = ''

    word1 = before.split(' ')[0]
    words[word1] += 1
    for w in after.split(','):
        if w.strip():
            words[w.strip()]+= 1

words
words.most_common()[-1]

# Should have done this first :(
# Counter(re.findall(r"[a-zA-Z]+", inp)).most_common()[-1]


# In[ ]:


class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

