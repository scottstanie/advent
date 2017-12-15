from day10 import knot_hash
from utils import neighbors4
import numpy as np


input_str = "wenycdww"
# input_str = "flqrgnkx"


grid = np.zeros((128, 128))
for idx in range(128):

    string_to_hash = "{}-{}".format(input_str, idx)
    hexstr = knot_hash(string_to_hash)
    binary_row = "{:0128b}".format(int(hexstr, 16))
    grid[idx, :] = np.array(list(binary_row)).astype(np.uint8)


print(np.sum(grid))

def flood_fill(grid, row, col, marked_grid, cur_region):
    marked_grid[row, col] = cur_region
    for nr, nc in neighbors4((row, col)):
        if grid[nr, nc] and not marked_grid[nr, nc]:
            marked_grid[nr, nc] = cur_region
            flood_fill(grid, nr, nc, marked_grid, cur_region)




tgrid = np.pad(grid, (1,1), 'constant', constant_values=(0,0))

regions = np.zeros((130, 130))

num_regions = 1
for r in range(1, 129):
    for c in range(1, 129):
        if tgrid[r, c] and not regions[r, c]:
            flood_fill(tgrid, r, c, regions, num_regions)
            num_regions += 1

print(regions)
print(np.max(regions))
