import math
from typing import List


def find_tree(row: List[str], index: int) -> int:
    if row[index] == '#':
        return 1
    return 0

def count_trees(data: List[str], right: int, down: int) -> int:
    row_len = len(data[0])
    indices = range(0, len(data) * right, right)

    tree_count = 0
    for row, i in zip(data[::down], indices):
        if i > (row_len - 1):
            i = i % (row_len)
        tree_count += find_tree(row, i)
    return tree_count


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [r.strip() for r in f.readlines()]

    combinations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    results = []
    for right, down in combinations:
        ans = count_trees(data, right, down)
        results.append(ans)
        print(f'Right {right}, down {down} = {ans}')

    print(f'Final result = {math.prod([r for r in results])}')
