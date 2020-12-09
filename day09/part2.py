from typing import List

from part1 import calc_non_complement


def calc_weakness(data: List[int]) -> int:
    prev_ans = calc_non_complement(data)

    for i in range(0, len(data)):
        # skip ahead if the first number is too big
        if data[i] >= prev_ans:
            continue

        # try up to 50 look aheads
        vals = []
        for k in range(0, 50):
            vals.append(data[i+k])
            curr_sum = sum(vals)

            # skip if sum gets too big
            if curr_sum > prev_ans:
                break
            if curr_sum == prev_ans:
                ans = min(vals) + max(vals)
                return ans


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(i.strip()) for i in f.readlines()]

    print(calc_weakness(data))
