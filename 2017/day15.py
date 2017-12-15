fa = 16807
fb = 48271
m = 2147483647

sa = 679
sb = 771

# sa = 65
# sb = 8921

def next_num(cur_num, factor, modulus):
    return (cur_num * factor) % modulus


def right16(integer):
    return "{:0b}".format(integer)[-16:]


def are_matching(na, nb):
    return (max(na, nb) - min(na, nb)) % (2**16) == 0


# num_iters = 40e6
max_iter2 = 5e6
iter2_count = 0
match_count = 0

multa = 4
multb = 8
total_iters = 0
while iter2_count < max_iter2:
# for _ in range(int(num_iters)):
    total_iters += 1
    sa = next_num(sa, fa, m)
    sb = next_num(sb, fb, m)
    # print(right16(sa), right16(sb))
    # Passes through to the judge
    while (sa % 4 > 0):
        sa = next_num(sa, fa, m)
    while (sb % 8 > 0):
        sb = next_num(sb, fb, m)

    iter2_count += 1

    # match_count += (right16(sa) == right16(sb))
    # faster way:
    match_count += are_matching(sa, sb)

print(match_count)
