from typing import List


def calc_non_complement(data: List[int]) -> int:
    for i, val in enumerate(data):
        if i < 25:
            continue

        chunk = data[i-25:i]
        complement = [val - c for c in chunk if c < val]
        diff = set(chunk) & set(complement)

        if len(diff) == 0:
            return val


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(i.strip()) for i in f.readlines()]

    print(calc_non_complement(data))
