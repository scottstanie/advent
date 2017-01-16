import re
import itertools
from collections import defaultdict


def read_input():
    with open('day13.txt') as f:
        return f.read().splitlines()


class Seat(object):
    def __init__(self, name, neighbor1, val1, neighbor2, val2):
        self.name = name
        self.neighbors = [(neighbor1, val1), (neighbor2, val2)]

    def __repr__(self):
        return '%s ( %s ) %s ( %s ) %s' % (
            self.neighbors[0][0],
            self.neighbors[0][1],
            self.name,
            self.neighbors[1][1],
            self.neighbors[1][0],
        )


def most_happiness(people, person_values):
    return max(all_seat_arrangements(people, person_values), key=total_happiness)


def all_seat_arrangements(people, person_values):
    return (arrangement_to_seats(arr, person_values) for arr in arrangements(people))


def total_happiness(arrangement):
    return sum(happiness(seat) for seat in arrangement)


def happiness(seat):
    """Neighbor tuples are structured as (neighbor_name, happiness_value)"""
    return sum(neighbor_tuple[1] for neighbor_tuple in seat.neighbors)


arrangements = itertools.permutations


def arrangement_to_seats(arrangement, person_values):
    """(A, B, C, D) -> [Seat(name=A, neighbor1 = D, neighbor2=B,...)]"""
    num_seats = len(arrangement)
    seats = []
    for idx in range(num_seats):
        name = arrangement[idx]
        n1 = arrangement[idx - 1]  # Let first index wrap back to -1
        n2 = arrangement[(idx + 1) % num_seats]
        val1 = person_values[name][n1]
        val2 = person_values[name][n2]
        seats.append(Seat(name, n1, val1, n2, val2))

    return seats


def create_person_values(input_lines):
    person_values = defaultdict(dict)
    for line in input_lines:
        name, val, neighbor = parse_line(line)
        person_values[name][neighbor] = val
    return person_values


def parse_line(input_line):
    def map_valence(word):
        possible = {'gain': 1, 'lose': -1}
        return possible[word]

    regex = r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).'
    name, valence_word, units, neighbor = re.match(regex, input_line).groups()

    value = units * map_valence(valence_word)
    return name, value, neighbor


def add_you(input_lines, people):
    lines = []
    for person in people:
        lines.append("%s would gain 0 happiness units by sitting next to You." % person)
        lines.append("You would gain 0 happiness units by sitting next to %s." % person)

    return input_lines + lines

if __name__ == '__main__':

    input_lines = read_input()
    person_values = create_person_values(input_lines)
    people = person_values.keys()
    optimal_arrangement = most_happiness(people, person_values)
    print optimal_arrangement
    print 'Happiness: ', total_happiness(optimal_arrangement)

    # # Part 2: recalculate person_values with you
    # extended_lines = add_you(input_lines, people)
    # person_values = create_person_values(extended_lines)
    # people = person_values.keys()

    # optimal_arrangement = most_happiness(people, person_values)
    # print optimal_arrangement
    # print 'Happiness: ', total_happiness(optimal_arrangement)
