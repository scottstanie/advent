inp = read_input(13)
depth_ranges = [(int(line.split(':')[0]), int(line.split(':')[1].strip())) for line in inp]

s = 0
for (depth, ran) in depth_ranges:
    if depth % (2*(ran-1)) == 0:
        print(depth, ran)
        s += (depth*ran)

print(s)

def try_delay(delay):
    s = 0
    for (depth, ran) in depth_ranges:
        if (depth + delay) % (2*(ran-1)) == 0:
            return False
    return True

idx = 0
while True:
    if try_delay(idx):
        print(idx); break
    else:
        idx += 1
