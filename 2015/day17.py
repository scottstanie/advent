import itertools

containers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]


def all_combos(containers):
    return (comb for r in range(1, len(containers))
            for comb in itertools.combinations(containers, r) if sum(comb) == 150)


# def all_combos_recursive(containers, length):
#     if length <= 0:
#         yield []
#     else:
#
#         for idx, item in enumerate(containers):
#             for comb in all_combos_recursive(containers[:idx] + containers[idx + 1:], length - 1):
#                 yield [item] + comb


# Part 1: brute force
print len(list(comb for comb in all_combos(containers)))

# Part 2:
min_length = len(min(all_combos(containers), key=len))
print len(list(comb for comb in itertools.combinations(containers, min_length) if sum(comb) == 150))
