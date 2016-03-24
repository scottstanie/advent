import itertools
import numpy as np


def main():

    with open('day6.txt', 'rb') as f:
        instructions = f.read().split('\n')
        ii = [i.split(' through ') for i in instructions if i != '']

        coords = [(i[0].split(' ')[-1].split(','), i[1].split(',')) for i in ii]

        switches = [f[0].split(' ')[0] if len(f[0].split(' ')) == 2 else f[0].split(' ')[1] for f in ii]

        cmd_coords = zip(switches, coords)

        final_lights = run_lights(np.zeros(shape=(1000, 1000)), cmd_coords)

        final_count = sum(sum(final_lights))

        print final_count, ' lights on'

        final_lights_2 = run_lights_part2(np.zeros(shape=(1000, 1000)), cmd_coords)

        brightness = sum(sum(final_lights_2))

        print 'total brightness: ', brightness
        return final_count


def run_lights(lights, cmd_coords):
    for cmd, (start, end) in cmd_coords:
        try:
            if cmd == 'toggle':
                lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ] = 1 - lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ]
            if cmd == 'on':
                lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ] = 1
            if cmd == 'off':
                lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ] = 0
        except:
            print cmd, start, end

    return lights


def run_lights_part2(lights, cmd_coords):
    for cmd, (start, end) in cmd_coords:
        try:
            if cmd == 'toggle':
                lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ] = 2 + lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ]
            if cmd == 'on':
                lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ] = 1 + lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ]
            if cmd == 'off':
                lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ] = np.maximum(lights[np.ix_(
                    xrange(int(start[0]), 1 + int(end[0])),
                    xrange(int(start[1]), 1 + int(end[1])))
                ] - 1, 0)
        except:
            print cmd, start, end

    return lights

if __name__ == '__main__':
    main()
