#!/usr/bin/env python
import itertools

CITIES = {}


class City(object):
    def __init__(self, name):
        self.name = name
        self.distances = {}

    def __repr__(self):
        return '%s' % ', '.join('%s: %s' % (city, name)
                                for city, name in self.distances.iteritems())


def parse_input():
    global CITIES

    def parse_city_line(line):
        source_city, _, dest_city, _, value = line.split(' ')
        return source_city, dest_city, int(value)

    with open('day9.txt') as f:
        distance_lines = f.read().splitlines()
        city_set = set()
        for line in distance_lines:
            source_city, dest_city, _ = parse_city_line(line)
            city_set.add(source_city)
            city_set.add(dest_city)

        CITIES = {name: City(name) for name in city_set}
        for line in distance_lines:
            source_city, dest_city, distance = parse_city_line(line)
            # Include both directions to avoid key error
            CITIES[source_city].distances[dest_city] = distance
            CITIES[dest_city].distances[source_city] = distance

        return city_set


alltours = itertools.permutations


def alltours_tsp_short(city_set):
    return shortest_tour(alltours(city_set))


def alltours_tsp_long(city_set):
    return longest_tour(alltours(city_set))


def shortest_tour(tours):
    # Part 1: shortest tour is min tour length
    return min(tours, key=tour_length)


def longest_tour(tours):
    # Part 2: just change min to max
    return max(tours, key=tour_length)


def tour_length(tour):
    # length - 1, since there is no wraparound to the start
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))


def distance(source_city, dest_city):
    return CITIES[source_city].distances[dest_city]


if __name__ == '__main__':
    city_set = parse_input()
    tour_cities_short = alltours_tsp_short(city_set)
    tour_cities_long = alltours_tsp_long(city_set)
    print "part 1: ", tour_length(tour_cities_short)
    print "part 2: ", tour_length(tour_cities_long)
