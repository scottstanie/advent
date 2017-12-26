import utils
import collections


def propagate(pos, vel, accel):
    """point is [pos, vel, accel]"""
    vel += accel
    pos += vel
    return [pos, vel, accel]


if __name__ == '__main__':
    # inp = utils.read_input(20)
    inp = '''<3,0,-1>\n<2,2,-2>'''.splitlines()
    points = [list(map(int, p.strip('<>').split(','))) for p in inp]

    print(points)
    for _ in range(10):
        points = [propagate(*point) for point in points]
    print(points)


