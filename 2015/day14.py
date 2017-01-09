from collections import defaultdict

def parse_input():
    with open('day14.txt') as f:
        return (parse_line(l) for l in f.readlines())

test_inp = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""


def parse_line(line):

    reindeer, _, _, speed, _, _, on_duration, _, _, _, _, _, _, rest_time, _ = line.split(' ')
    return reindeer, int(speed), int(on_duration), int(rest_time)


def create_schedule(speed, on_duration, rest_time):
    distance = []
    flying = 1
    current_duration = on_duration
    current_position = 0
    idx = 0
    while idx < 2503:
        if flying:
            current_position += speed

        distance.append(current_position)
        current_duration -= 1
        if current_duration == 0:
            # Flip bit
            flying ^= 1
            current_duration = on_duration if flying else rest_time

        idx += 1

    return distance


def leader_distance(reindeer_distances):
    return [max(rd[i] for rd in reindeer_distances.values()) for i in range(2503)]


def scores2(reindeer_distances, leader):
    new_scores = defaultdict(list)
    for idx, score in enumerate(leader):
        for reindeer, dists in reindeer_distances.items():
            new_scores[reindeer].append(score == dists[idx])

    return new_scores


if __name__ == '__main__':
    lines = parse_input()
    reindeer_distances = {}
    for reindeer, speed, on_duration, rest_time in lines:
        reindeer_distances[reindeer] = create_schedule(speed, on_duration, rest_time)

    # print reindeer_distances
    m = max(reindeer_distances.values(), key=lambda d: d[2502])
    print 'part 1: ', m[2502]

    leader = leader_distance(reindeer_distances)
    new_counts = scores2(reindeer_distances, leader)
    new_scores = [sum(trues) for trues in new_counts.values()]

    print 'part 2: ', max(new_scores)
