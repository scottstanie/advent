# coding: utf-8
import numpy as np
import re
import math
import requests

from collections import Counter, defaultdict, namedtuple, deque
from itertools import permutations, combinations, chain, cycle, product, islice
#[1518-03-18 00:03] Guard #3529 begins shift
# [1518-04-26 00:55] wakes up
#year-month-day hour:minute
from datetime import datetime

test = False
if test:
    lines = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".splitlines()
else:
    lines = open('input').read().splitlines()

entries = []

for line in lines:
    dt = line[1:17]
    txt = line[19:]
    entries.append((datetime.strptime(dt, '%Y-%m-%d %H:%M'), txt))

sorted_e = sorted(entries, key=lambda tup: tup[0])


def guard_num(s):
    pat = 'Guard #(\d+) begins shift'
    m = re.match(pat, s)
    if m:
        return int(m.groups()[0])


sleep_mins = Counter()
cur_g = None

for idx, (dt, s) in enumerate(sorted_e):
    if s == 'wakes up':
        sleep_mins[cur_g] += (sorted_e[idx][0] - sorted_e[idx - 1][0]).seconds
        # print(sleep_mins)
    elif guard_num(s):
        cur_g = guard_num(s)

print(sleep_mins.most_common())
max_guard = sleep_mins.most_common()[0][0]  #
print('max guard:', max_guard)

cur_g = None
asleeps = np.zeros(60)
for idx, (dt, s) in enumerate(sorted_e):
    if s == 'wakes up' and cur_g == max_guard:
        endm = sorted_e[idx][0].minute
        startm = sorted_e[idx - 1][0].minute
        # print(startm, endm)
        # print(sorted_e[idx][0])
        # print(sorted_e[idx - 1][0])
        asleeps[startm:endm] += 1
    elif guard_num(s):
        cur_g = guard_num(s)

print(asleeps)
print(np.argmax(asleeps))
print(np.argmax(asleeps) * max_guard)

# Part 2:
all_asleeps = defaultdict(lambda: np.zeros(60))

for idx, (dt, s) in enumerate(sorted_e):
    if s == 'wakes up':
        startm = sorted_e[idx - 1][0].minute
        endm = sorted_e[idx][0].minute
        all_asleeps[cur_g][startm:endm] += 1
    elif guard_num(s):
        cur_g = guard_num(s)

cur_max = 0
for g, asleep_arr in all_asleeps.items():
    if np.max(asleep_arr) > cur_max:
        cur_max = np.max(asleep_arr)
        max_min = np.argmax(asleep_arr)
        max_g = g

print(max_g, max_min)
print(max_g * max_min)
