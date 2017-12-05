import utils

if __name__ == '__main__':
    lines = utils.read_input(5)
    nums = [int(n) for n in lines]

    num_steps = 0
    idx = 0
    while idx < len(nums):
        old_idx = idx
        step = nums[idx]
        idx += step
        nums[old_idx] = nums[old_idx] + 1 if nums[old_idx] < 3 else nums[old_idx] - 1
        num_steps += 1

    print(num_steps)
